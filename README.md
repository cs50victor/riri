# “Formal education will make you a living; self-education will make you a fortune.” --Jim Rohn
# Media Synthesis
**Synthetic media describes the use of artificial intelligence to generate and manipulate data, most often to automate the creation of entertainment.**
This field encompasses deepfakes, image synthesis, audio synthesis, text synthesis, style transfer, speech synthesis, and much more.

4k video upscale: https://youtube.com/watch?v=aJzmCUvLNrI&feature=youtu.be
Deep fake voice:  https://www.youtube.com/watch?v=BkH2zEHJ2Ng
Deep fake face: https://www.youtube.com/watch?v=3vHvOyZ0GbY
Image synthesis: https://www.reddit.com/r/MediaSynthesis/comments/hqpcb9/ive_been_having_way_too_much_fun_and_wasting_way/
Website building : debuild.co



# ~~S~~RiRi
Neural TextToSpeech 
Goal- Her(2013)
Tutorial - https://levelup.gitconnected.com/installing-mozilla-tts-on-a-raspberry-pi-4-e6af16459ab9

https://www.orangenarwhals.com/2020/06/town-announcer-npc-for-online-town-icra2020-virtual-happy-hour/

# TTS
     -    Download espeak
     -    Download this [Zip] https://github.com/mozilla/TTS/tree/53b24625a7b898447b0cda2929503b96752d9eae rename it to TTS
     -  Download model (config and ) from  https://drive.google.com/drive/folders/10ymOlWHutqTtfDYhIbHULn2IKDKP0O9m into a folder "d" into TTS
     -    make sure you're using a conda env
     -    python setup.py develop [for pip TTS]
     -    python setup.py build
     -    pip install -r requirements.txt
     -    python setup.py bdist_wheel --checkpoint .\d\checkpoint_name.tar --model_config .\d\config.json
     -    pip uninstall tensorflow(if needed)
     -    cd ..
     -    pip install ./TTS/dist/TTS-0.0.1+4f61539-py3-none-any.whl (your filename will differ)
     -    [Downlaod WaveRNN from github and checkout to required branch - link path to server.py    (lib_path)
     -    pip uninstall numba
     -    pip install numba==0.48
     -    python -m TTS.server.server
     -    Anything else read this https://github.com/mozilla/TTS/issues/423
     -     and https://gist.github.com/jcc10/d6d68df2204e239ce1e6960a9b107aac


Python and C++
-WaveRNN and Tacotron2 **

- 24 hours of cleaned voice data | Neural Voice
(https://speech.microsoft.com/customvoice)
- Give it alot of synchronous text and speech to train a neural network (Resemble Ai)
- Deep Learning
- Selection of diffrent combinations of  Phonemes


# Deep Neural networks- a lot of neurons (deep) 
# Genertive Model
# Machine Learning - a way for computers to lear patterns from a lot of examples- used when you cn't explicitly write an algorithm to solve a problem 
- Download netflix shows and their script
