#BY Joker Developer @LKDeveloper
#Join Our Telegram Group - t.me/lkdeveloper

from asyncio import streams
from pytube import YouTube

print("LK Developers YouTube Downloader Bot)

url = input("π β   ππ»ππ²πΏ π¬πΌππΏ π¨π₯π ππ²πΏπ² πΈ β : ")
my_video = YouTube(url)

#get video title
print("ππ²  ππΈπ³π΄πΎ ππΈππ»π΄  πβ") 
print(my_video.title)

#get thumbnail image
print("π¨π  π»πο½π«ο½ΰΉεβ Ε€Δ€β¬ Ε¦ββ€πΞ²ΰΈ Ξ±ππ  ππ²βπ₯  (ΝCΝLΝIΝCΝKΝ TΝHΝEΝ LΝIΝNΝKΝ TΝOΝ DΝOΝWΝNΝLΝOΝAΝDΝ)Ν  βπ") 
print(my_video.thumbnail_url)

#set streame resolution
print("π²β  α΅οΌ―π°ΰΈ ππ ππ‘ΞΉβπ π³α₯πΡπ π£π  οΌ€πΠΊπΌβππ  ππ")

#set stream resolution

my_video = my_video.streams.get_highest_resolution()

my_video.download()

print("π β π π¦ππ°π°π²πππ³ππΉπΉπ ππͺπ°π§π₯π΅ππππ ππ’πππ¬ π β π")

#BY LK DEVELOPERS
