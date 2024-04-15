import pygame
import os

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Caminho absoluto do arquivo mp3
audio_file = "Hidrogenio.mp3"

# Chama a função para reproduzir o áudio
play_audio(audio_file)
