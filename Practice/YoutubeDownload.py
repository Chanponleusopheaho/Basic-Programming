# importing the module 
from pytube import YouTube 
  
# where to save 
SAVE_PATH = "Downloads" #to_do 
  
# link of the video to be downloaded 
link="https://youtu.be/2-ANJLC4ss0?list=RD2-ANJLC4ss0"
  
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
  
# filters out all the files with "mp4" extension 
mp4files = yt.filter('mp4') 

import pytube
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()

#to set the name of the file
yt.set_filename('Song Video')  
  
# get the video with the extension and
# resolution passed in the get() function 
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    # downloading the video 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!') 