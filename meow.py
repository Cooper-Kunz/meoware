from PIL import Image
import webbrowser
import threading
import time

# Repetitive array instead of webscraping, or perhaps I'll create a database lol
theImages = ["cat_test1.jpeg", "cat_test2.jpeg", "cat_test3.jpeg", "cat_test4.jpeg", "cat_test5.jpeg",
             "cat_test6.jpeg",
             "cat_test1.jpeg", "cat_test2.jpeg", "cat_test3.jpeg", "cat_test4.jpeg", "cat_test5.jpeg",
             "cat_test6.jpeg"]

def gimmeCats():
    time.sleep(5)
    for image in theImages:
        display = Image.open("./images/"+image)
        display.show()

def gimmeMoreCats():
    #This thread will eventually open alternative types of media, ie, videos, audio, webbrowsers, etc...
    #We want 2x the cats at the same time
    for image in theImages:
        display = Image.open("./images/"+image)
        display.show()
        #webbrowser doesn't work yet lolz
        url = "https://www.youtube.com/watch?v=HxM46vRJMZs"
        webbrowser.open_new(url)


if __name__ == '__main__':
    
    aFew = threading.Thread(target=gimmeCats)
    aFew.start()
    
    lotsNlots = threading.Thread(target=gimmeMoreCats)
    lotsNlots.start()


