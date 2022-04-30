#!/bin/bash

# Use to install first time
pyenv install
export PYENV_ROOT="$HOME/.pyenv"     
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
pip install kalliope
kalliope install --git-url https://github.com/veka-server/kalliope-vosk.git
# wget https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip
unzip -j vosk-model-fr-0.22.zip -d resources/stt/vosk/model-fr-full/
# cp /usr/lib/python3.10/site-packages/snowboy/_snowboydetect.so  $HOME/.pyenv/versions/3.9.11/lib/python3.9/site-packages/kalliope/trigger/snowboy/$(uname -m)/python39/