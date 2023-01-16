from pytube import YouTube
def download(link):
    youtubeObjective = YouTube(link)
    youtubeObjective = youtubeObjective.streams.get_highest_resolution()
    try:
        youtubeObjective.download()
    except:
        print("Error")
    print("Download completed")
link = input("Enter your youtube link or url: ")
download(link)