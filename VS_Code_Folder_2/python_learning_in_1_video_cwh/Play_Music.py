import subprocess

print("\n")
print('  Enter:')
print('\t1 to play "Cartoon - On & On"')
print('\t2 to play "Disfigure - Blank"')
print('\t3 to play "Adventure"')
print('\t4 to play "Heros Tonight"')
print('\t5 to play "Jumbo"')
print('\t6 to play "Simbolism N Tell"')
print('\t7 to play "Heart Afire"')
print('\t8 to play "Alan Walker"')
print('\t9 to play "Taki Taki"')
print('\t10 to play "Despacito"')
print('\t11 to play "Mere mehboob Qayamat Hogi"')
print('\t12 to play "Coffin Dance Song"')
print("\n")
a = int(input("  Enter your choice here: "))
if a == 1:
    print("\n")
    print("  Playing Cartoon On & On...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Cartoon - On & On (feat. Daniel Levi) [NCS Release].mp3"])
    
elif a == 2:
    print("\n")
    print("  Playing Disfigure - Blank...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Disfigure - Blank [NCS Release].mp3"])
elif a == 3:
    print("\n")
    print("  Playing Adventure...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Izzamuzzic - Adventure (Original Mix).mp3"])
elif a == 4:
    print("\n")
    print("  Playing Heros Tonight...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Janji - Heroes Tonight (feat. Johnning) [NCS Release].mp3"])
elif a == 5:
    print("\n")
    print("  Playing Jumbo...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Jumbo, Jay De La Cueva - Fotografía (En Directo).mp3"])
elif a == 6:
    print("\n")
    print("  Playing Simbolism N Tell...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Symbolism N Tell - Electro-Light & Ke Ha RaveDj.mp3"])
elif a == 7:
    print("\n")
    print("  Playing Heart Afire...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Defqwop - Heart Afire (feat. Strix).mp3"])
elif a == 8:
    print("\n")
    print("  Playing Alan Walker...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Alan Walker - Fade [NCS Release].mp3"])
elif a == 9:
    print("\n")
    print("  Playing Taki Taki...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/DJ Snake, Selena Gomez, Cardi B, Ozuna - Taki Taki.mp3"])
elif a == 10:
    print("\n")
    print("  Playing Despacito...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Justin Bieber – Despacito 🎤 ft. Luis Fonsi & Daddy Yankee [Pop].mp3"])
elif a == 11:
    print("\n")
    print("  Playing Mere Mehboob...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/Mere Mehboob Qayamat Hogi Full Song With Mr. X in Bombay Kishore Kumar Hit Songs.mp3"])
elif a == 12:
    print("\n")
    print("  Playing Coffin Dance Song...")
    subprocess.run(["afplay", "/Users/avneeshpundir/Documents/Songs_for_programming/COFFIN DANCE MEME SONG Tony Igy - ASTRONOMIA (Remix).mp3"])

else:
    print("\n")
    print("Please enter a valid choice!!")
    print("\n")
