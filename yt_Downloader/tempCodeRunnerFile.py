
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

print(tab(l, headers=['Format', 'Filesize