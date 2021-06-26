from pytube import YouTube

video = YouTube("https://youtu.be/LiqIQ5He7_4")



print(video.title)
print(video.thumbnail_url)
print(video.streams)
streams = video.streams
for stream in streams:
    print(stream)

#video.streams.first().download()

video.streams.get_highest_resolution().download()
