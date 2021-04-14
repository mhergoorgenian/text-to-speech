import os
from gtts import gTTS

mytext=""
lange='en'
output=gTTS(text=mytext,lang=lange,slow=False)
output.save("player.mp3")
os.system("player.mp3")
