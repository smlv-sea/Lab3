#!/bin/bash

python3 qs.py

# Создание видео из изображений
ffmpeg -framerate 5 -i step_%d.png -c:v libx264 -r 30 -pix_fmt yuv420p qs.mp4
