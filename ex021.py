# faça um programa em python que abra e reproduza o audio de um arquivo em mp3
from pygame import mixer

input('aperte enter pra tocar')

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()

input("ouça a musica")

