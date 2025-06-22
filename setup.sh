#!/usr/bin/env sh

# You need to install anaconda - https://www.anaconda.com/docs/getting-started/anaconda/install#mac-os-command-line-installer
conda create -n tinytroupe python=3.10

conda activate tinytroupe

pip install git+https://github.com/microsoft/TinyTroupe.git@main