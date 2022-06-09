

def file_format(file):
    video_formats = ["mp4","mov","wmv","flv","avi","avchd","webm","mkv","f4v","swf","qt","mpg","mpeg","mp2","mpe","mpv","m4p","m4v"]

    audio_formats = ["pcm","wav","aiff","mp3","acc","wma","flac","alac","wma"]

    doc_formats = ["doc","docx","html","htm","odt","pdf","xls","xlsx","ods","ppt","pptx","txt"]

    image_formats =["tif","jpg","gif","png"]

    temp = []
    
    for x in range(len(file)):
        x +=1
        
        if file[-x] != ".":
            temp.append(file[-x])
            format1 = "".join(temp)
            
        else:
            break
    
    format1 = format1[::-1]
    
    if format1 in video_formats:
        return "video"
    
    elif format1 in audio_formats:
        return "audio"
    
    elif format1 in doc_formats:
        return "document"
    
    elif format1 in image_formats:
        return "image"
    
    else:
        return None
    
