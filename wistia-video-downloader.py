import urllib, json 
import requests
import io
from csv import DictReader
import time
import argparse
from termcolor import colored
import ffmpeg

by = colored("Created by: Mohamed Yaser","blue")
text = """Get multiple wvideoid from text/csv file and download all the videos (format 720p or 1080p)\n"""+str(by)
parser = argparse.ArgumentParser(description=text)
#parser = argparse.ArgumentParser(description=)
parser.add_argument("file", type=str, help="set file text/csv file location")
args = parser.parse_args()

with open(args.file) as f:
    link = [row["id"] for row in DictReader(f)]


download1 =[]
a = 0
b = 0
video_name = []
a1 = []
b1 =[]
video_namecheck =[]

for i in link:
    ts_rem = "https://fast.wistia.com/embed/medias/"+str(i)+".json"
    b1.append(ts_rem)


for b1 in b1:
    with urllib.request.urlopen(b1) as url:
        data = json.loads(url.read().decode())
        if data['media']['assets']['ext' == "mp4"]:
            a1.append(data['media']['assets']['height' == "1080" or 'height' == "720"]['url'])
            video_name.append(data['media']['name'])


print("Current Total links:",len(a1))

format = ".mp4"
for i in video_name:
    if format in i:
        video_namecheck.append(i)
    else:
        i += ".mp4"
        video_namecheck.append(i)


b = 1
for i, j in zip(a1, video_namecheck):
    print("Downloading file "+str(b)+": "+str(b)+"_"+str(j))
    (
        ffmpeg
        .input(str(i))
        .output(str(b)+"_"+str(j), vcodec='copy', **{'loglevel': "panic"})
        .run()
    )
    time.sleep(2)
    b +=1

print("Download Complete, total links:",len(a1))

