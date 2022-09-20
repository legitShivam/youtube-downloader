from __future__ import unicode_literals
from tabulate import tabulate as tab
import youtube_dl

ydl_opts = {}
link = 'https://www.youtube.com/watch?v=OP2monpbJkg'  # Video
# 'https://www.youtube.com/playlist?list=PLsEtM1pbiHlheS2HmiBl_wq77rPekYKxo']  # Playlist
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(link)


data = youtube_dl.YoutubeDL().extract_info(link, download=False)
l = []
for dataDict in data['formats']:
    temp = []
    temp.append(dataDict['format'])
    if dataDict['filesize'] != None:
        temp.append(f"{round(dataDict['filesize']/1048576)}MB")
    else:
        temp.append('')
    temp.append(dataDict['format_id'])
    # temp.append(dataDict['url'])
    if dataDict['width'] != None:
        size = f"{dataDict['width']} x {dataDict['height']}p"
    else:
        size = "Audio"
    temp.append(size)
    temp.append(dataDict['ext'])
    temp.append(dataDict['format_note'])
    l.append(temp)

print(tab(l, headers=['Format', 'Filesize', 'Format_id', 'Size', 'Extension', 'Format Note']))

# for i in data['formats'][19].items():
#     print(i)