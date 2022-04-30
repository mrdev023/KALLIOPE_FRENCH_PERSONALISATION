#!/bin/bash

wget https://alphacephei.com/vosk/models/vosk-model-fr-0.22.zip
unzip vosk-model-fr-0.22.zip -d resources/stt/vosk/
mv resources/stt/vosk/vosk-model-fr-0.22 resources/stt/vosk/model-fr-full/
rm vosk-model-fr-0.22.zip