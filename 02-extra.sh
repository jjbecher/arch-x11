#!/bin/bash

# Python
sudo pacman -S --noconfirm --needed python-pip python-rich python-click

# Codium
paru -S --noconfirm --needed vscodium-bin vscodium-bin-marketplace vscodium-bin-features 

# Office
sudo pacman -S --noconfirm --needed libreoffice-still chromium zathura

# Bluetooth
sudo pacman -S --noconfirm --needed bluez bluez-utils blueman
sudo systemctl enable bluetooth.service

# Docker
sudo pacman -S --noconfirm --needed docker docker-compose
sudo systemctl enable docker.service
