import torch
import numpy as np
from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self, ids, path, mel_len, hop_length, mode, pad, ap, eval=False):
        self.path = path
        self.metadata = ids
        self.eval = eval
        self.mel_len = mel_len
        self.pad = pad 
        self.hop_length = hop_length
        self.mode = mode
        self.ap = ap

    def __getitem__(self, index):
        file = self.metadata[index]
        m = np.load(f"{self.path}mel/{file}.npy")
        if self.mode in ['gauss', 'mold']:
            x = self.ap.load_wav(f"{self.path}wavs/{file}.wav")
        elif type(self.mode) is int:
            x = self.ap.load_wav(f"{self.path}quant/{file}.npy")
        else:
            raise RuntimeError("Unknown dataset mode - ", self.mode)
        return m, x

    def __len__(self):
        return len(self.metadata)

    def collate(self, batch):
        seq_len = self.mel_len * self.hop_length
        pad = self.pad  # kernel size 5
        mel_win = seq_len // self.hop_length + 2 * pad
        max_offsets = [x[0].shape[-1] - (mel_win + 2 * pad) for x in batch]
        if self.eval:
            mel_offsets = [100] * len(batch)
        else:
            mel_offsets = [np.random.randint(0, offset) for offset in max_offsets]
        sig_offsets = [(offset + pad) * self.hop_length for offset in mel_offsets]

        mels = [
            x[0][:, mel_offsets[i] : mel_offsets[i] + mel_win]
            for i, x in enumerate(batch)
        ]

        coarse = [
            x[1][sig_offsets[i] : sig_offsets[i] + seq_len + 1]
            for i, x in enumerate(batch)
        ]
        mels = np.stack(mels).astype(np.float32)
        if self.mode in ['gauss', 'mold']:
            coarse = np.stack(coarse).astype(np.float32)
            coarse = torch.FloatTensor(coarse)
            x_input = coarse[:, :seq_len]
        elif type(self.mode) is int:
            coarse = np.stack(coarse).astype(np.int64)
            coarse = torch.LongTensor(coarse)
            x_input = 2 * coarse[:, :seq_len].float() / (2 ** self.mode - 1.0) - 1.0
        y_coarse = coarse[:, 1:]
        mels = torch.FloatTensor(mels)
        return x_input, mels, y_coarse