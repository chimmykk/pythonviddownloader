import pytube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

link = str(input("enter your link"))
yt= pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print("download succesful")