#!/bin/bash

ARCH=$(uname -m)
PYTHON_VERSION=$(python -V | cut -d " " -f 2)
PYTHON_VERSION_MAJOR=$(echo $PYTHON_VERSION | cut -d "." -f 1)
PYTHON_VERSION_MINOR=$(echo $PYTHON_VERSION | cut -d "." -f 2)
PYTHON_PATH=/usr/lib/python$PYTHON_VERSION_MAJOR.$PYTHON_VERSION_MINOR
SNOWBOY_PYTHON=python$PYTHON_VERSION_MAJOR$PYTHON_VERSION_MINOR
mkdir -p $PYTHON_PATH/site-packages/kalliope/trigger/snowboy/$ARCH/$SNOWBOY_PYTHON
cp $PYTHON_PATH/site-packages/snowboy/_snowboydetect.so $PYTHON_PATH/site-packages/kalliope/trigger/snowboy/$ARCH/$SNOWBOY_PYTHON/

