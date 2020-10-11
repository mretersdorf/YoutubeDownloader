from pytube import YouTube

# Downloads a video from YouTube
# Most Stream options will display only video or audio codecs. To download a video with both audio and video,
# progressive="True"

link = input("Enter the url of the video you would like to download: ")
yt = YouTube(link)

videos = yt.streams.all()

for video in videos:
    print(video)

tag = int(input("Enter itag which you want to download: "))
video = yt.streams.get_by_itag(itag=tag)

video.download("C:\\Users\\Michael\\Downloads\\DownloadedYoutubeVideos")

print("Completed.")