# wistia-video-downloader

This code allows you to download multiple videos from wistia based videos. 
Git clone the repo. go to wistia-video-downloader edit new.csv.
Add wistia id to the file.

<code>pip3 install -r ./requirements.txt<code>
To get all the required dependencies

<code>python3 ./wistia-video-downloader.py -h<code>
Get multiple wvideoid from text/csv file and download all the videos (format
720p or 1080p)

positional arguments:
  file        set file text/csv file location

optional arguments:
  -h, --help  show this help message and exit

To run the command:
<code>python3 ./wistia-video-downloader.py new.csv<code>