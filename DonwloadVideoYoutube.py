import shutil
import os
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=El6OfTo6MJY'
dest = 'c:/tmp/'

yt = YouTube(url)
video_resolucao = yt.streams.get_highest_resolution()
titulo = yt.title
video = video_resolucao.download()
arq_video = os.path.basename(video)

if not os.path.exists(dest + arq_video):
    shutil.move(video, dest)
    print(f"Video '{titulo}' foi baixado em {dest + arq_video}")
else:
    print(f"Vídeo já existe em {dest + arq_video}")