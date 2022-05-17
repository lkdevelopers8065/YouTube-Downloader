#BY Joker Developer @LKDeveloper
#Join Our Telegram Group - t.me/lkdeveloper

from asyncio import streams
from pytube import YouTube

url = input("🍓 ☠  𝗘𝗻𝘁𝗲𝗿 𝗬𝗼𝘂𝗿 𝗨𝗥𝗟 𝗛𝗲𝗿𝗲 🐸 ♚ : ")
my_video = YouTube(url)

#get video title
print("💞💲  𝚅𝙸𝙳𝙴𝙾 𝚃𝙸𝚃𝙻𝙴  🐝♟") 
print(my_video.title)

#get thumbnail image
print("🐨💚  𝔻𝑜ｗ𝔫ｌ๏卂∂ ŤĤ€ Ŧℍⓤ𝐌βภα𝐈𝓁  💛💲♔💥  (͎C͎L͎I͎C͎K͎ T͎H͎E͎ L͎I͎N͎K͎ T͎O͎ D͎O͎W͎N͎L͎O͎A͎D͎)͎  ✋🎁") 
print(my_video.thumbnail_url)

#set streame resolution
print("💲♚  ᵈＯ𝐰ภ𝐋𝕠𝔞𝔡ιⓝ𝕘 𝔳Ꭵ𝓓є𝐎 𝓣𝕠 Ｄ𝐞к𝓼Ⓣ𝕆𝐏  👌😂")

#set stream resolution

my_video = my_video.streams.get_highest_resolution()

my_video.download()

print("🍉 ⋆ 🍉 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝐃🍪𝐰𝐧𝐥🏵𝐚𝐝𝐞𝐝 𝐕𝐢𝐝𝐞🍬 🍉 ⋆ 🍉")

#BY LK DEVELOPERS