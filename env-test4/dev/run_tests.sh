# tests
nosetests tests -x

# runtime tests
./tests/test_server_package.sh
./tests/test_tts_train.sh
./tests/test_vocoder_train.sh

# linter check
cardboardlinter --refspec master