# requirements
/!\ You need to have the [Kalliope Core](https://github.com/kalliope-project/kalliope) installed before cloning this starter kit.

This starter kit has been tested with the version v0.5.0 of Kalliope.

If you have error with _snowboydetect kalliope can not import _snowboydetect.so with you current version of python.
Too fix it, you can use script in bellow

```bash
sudo ./fix_snowboy_bin.sh
```

# pico2wave

```bash
sudo pamac install svox-pico-bin
```

# Arch linux

You must use pyenv because pyaudio crash with python3.10

```bash
pacman -S pyenv
```

# kalliope starter config fr

This is an out of the box working configuration for french kalliope user.

How to use
 ```bash
git clone https://github.com/kalliope-project/kalliope_starter_fr.git
cd kalliope_starter_fr
kalliope start
```

# Create custom awake term with 

https://github.com/rhasspy/snowboy-seasalt
