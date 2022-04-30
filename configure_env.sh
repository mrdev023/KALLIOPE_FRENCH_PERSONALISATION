#!/bin/bash

# Use to install first time
pyenv install
export PYENV_ROOT="$HOME/.pyenv"     
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
pip install kalliope
kalliope install --git-url https://github.com/mrdev023/kalliope-vosk.git
# cp /usr/lib/python3.10/site-packages/snowboy/_snowboydetect.so  $HOME/.pyenv/versions/3.9.11/lib/python3.9/site-packages/kalliope/trigger/snowboy/$(uname -m)/python39/