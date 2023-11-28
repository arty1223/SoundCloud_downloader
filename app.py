from sclib import SoundcloudAPI, Track, Playlist
from os import mkdir, chdir, path
from datetime import datetime
api = SoundcloudAPI()
playlist = api.resolve('playlist link')

assert type(playlist) is Playlist

def fncheck(filename : str):
        result = filename
        for i in filename:
            if i in '<>:"/\|?*'+ "'":
                result = result.replace(i,"")     
        return result
print(playlist.title)
if __name__ == '__main__':
    try:
        chdir(playlist.title) #you can change "playlist.title" to desired directory name
    except:
        mkdir(playlist.title)
        chdir(playlist.title)
    time = datetime.now()
    amount = len(playlist)
    a = 0
    playlistfile = open("playlist.txt","w",encoding="utf-8")
    try:
        for track in playlist.tracks:
            a = a + 1            
            filename = fncheck(track.artist + ' - ' + track.title + '.mp3')    
            print(f"curent track: {filename} - {a} from {amount}, {round(a/(amount)*100,1)}%")
            playlistfile.write(filename + '\n')
            if path.exists(filename):continue
            with open(filename, 'wb+') as file:
                track.write_mp3_to(file)
        playlistfile.close()        
    except KeyboardInterrupt:
        playlistfile.close()
        print('interupt', filename, f'{round(a/(amount-1)*100,1)}%')
        exit()
    print(f"""done!
took {datetime.now() - time}""")
    exit()