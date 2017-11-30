import os
import threading
import time
from hurry.filesize import size

PATH = "/"

fileCounter = {"all":0, "text":0, "apps":0, "audios":0, "videos":0, "photos":0, "other":0}
formatMemoryCounter = {"all":0, "text":0, "apps":0, "audios":0, "videos":0, "photos":0, "other":0} 
textExtensions = [".txt", ".pdf"]
audioExtensions = [".mp3", ".mid", ".midi", ".wav", ".wmv", ".cda", ".ogg", ".ogm", ".aac", ".ac3", ".flac"]
videoExtensions = [".avi", ".flv", ".wmv", ".mov", ".mp4"]
photoExtensions = [".bmp", ".gif", ".jpg", ".png", ".psd", ".ai", ".svg", ".raw"]

def searchFileType(fileType, extensions = None):
    for root, dirs, files in os.walk(PATH):
        for name in files:
            #if name.endswith(".py"):
            #    txtFiles += 1
            newPath = os.path.join(root, name)
            if os.path.exists(newPath):
                if fileType == "apps" and ("." not in name):
                    fileCounter["apps"] += os.stat(newPath).st_size
                elif fileType == "all":
                    fileCounter["all"] += os.stat(newPath).st_size
                elif extensions is not None and any(x in name for x in extensions):
                    fileCounter[fileType] += os.stat(newPath).st_size

def classifyFiles():
    #initialize dictionaries
    global fileCounter, formatMemoryCounter
    fileCounter = {"all":0, "text":0, "apps":0, "audios":0, "videos":0, "photos":0, "other":0}
    formatMemoryCounter = {"all":0, "text":0, "apps":0, "audios":0, "videos":0, "photos":0, "other":0}


    threadTxt = threading.Thread(target = searchFileType, args = ("text", textExtensions,))
    threadApp = threading.Thread(target = searchFileType, args = ("apps", ))
    threadAudio = threading.Thread(target = searchFileType, args = ("audios", audioExtensions,))
    threadPhoto = threading.Thread(target = searchFileType, args = ("photos", photoExtensions,))
    threadAll = threading.Thread(target = searchFileType, args = ("all", ))

    threads = []
    threads.append(threadTxt)
    threads.append(threadApp)
    threads.append(threadAudio)
    threads.append(threadPhoto)
    threads.append(threadAll)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    fileCounter["other"] = fileCounter["all"] - sum((list(fileCounter.values()))[1:-1])
    for key in list(fileCounter.keys()):
        formatMemoryCounter[key] = size(fileCounter[key])

#start = time.time()
#classifyFiles()

#print(fileCounter)
#print(time.time() - start)
