from moviepy.editor import *
from pyfiglet import Figlet

print(Figlet(font="slant").renderText("from mp4 to mp3"))
mp4_file = input('Введите деректорию: ')

mp3_file = 'audio.mp3'

videoclip = VideoFileClip(mp4_file)

audioclip = videoclip.audio

audioclip.write_audiofile(mp3_file)

audioclip.close()

videoclip.close()