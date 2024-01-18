from gtts import gTTS
import os

text = "it is 6 AM and i am ready to give all of me"
output = gTTS(text=text, lang='en', slow=False)
output.save('output.mp3')
os.system("start output.mp3")