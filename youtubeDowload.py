from pytube import YouTube

import moviepy.editor as mp
import re
import os 

sair=True

while(sair):
    #Adicione em path a pasta que você deseja fazer o download
    path = '/home/cicero/Desktop' 
    link = input('Link do youtube: \n')
    yt= YouTube(link)
    
    print('Baixando')

    ys = yt.streams.filter(only_audio=True).first().download(path)

    print('Download completo')

    print('Convertendo para mp3')

    for file in os.listdir(path):
        if re.search('mp4',file):
            mp4 = os.path.join(path, file)
            mp3 = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4)
            new_file.write_audiofile(mp3)
            os.remove(mp4)
    vai_sair = input('Para sair digite SAIR, para continuar pressione Enter\n') 
     
    if(vai_sair == 'SAIR'):
        sair = False
    else:
        sair = True        
