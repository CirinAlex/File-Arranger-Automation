import os
import shutil
import file_format as f
import time


while True:
    fnum = os.listdir("C:\\Users\\PC\\Downloads")
    
    while True:
        num = os.listdir("C:\\Users\\PC\\Downloads")
        
        if len(fnum) < len(num):    
            fnum1 = num
            break
        
        elif len(fnum) > len(num):
            fnum = num
            
    for x in num:
        if x not in fnum:
            file = x
            break

    
    fnum = fnum1
    
    fileform = f.file_format(file)

    time.sleep(1)
    
    src = f"C:\\Users\\PC\\Downloads\\{file}"
    
    
    
    if fileform == "image":
        
        shutil.copy2(src , "F:\\images")
        
    
    elif fileform == "video":
        
        shutil.copy2(src, "F:\\video")
        
        
    elif fileform == "audio":
        
        shutil.copy2(src, "F:\\audio")
        
        
    elif fileform == "document":
        
        shutil.copy2(src, "F:\\documents")


    else:
        
        pass
