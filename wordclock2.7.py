# -*- coding: utf-8 -*-
#/usr/bin/python2.7
from datetime import datetime
#from neopixel import *
import ConfigParser
import time
import os.path



# LED strip configuration:
LED_COUNT      = 114            # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)



def clock(wait_ms=5000):
        

    try:
        color4 = 0
        colorFile = ConfigParser.ConfigParser()
        colorFile.read('color.ini')
        DEFAULT = colorFile.get('COLOR', 'ccolor')
        print (DEFAULT)
    except:
        print ("color.ini not found")
        DEFAULT = '255, 0, 0'
        print (DEFAULT)


    colorFile = DEFAULT.split(",")
    color0 = colorFile[0]
    color1 = colorFile[1]
    color2 = colorFile[2]
    color = (int(color0), int(color1), int(color2))
    print (color)
    print (color0)
    print (color1)
    print (color2)    

    config = ConfigParser.RawConfigParser()
    config.read('deutsch.ini')

    # get value from ini file

    es = config.get('DEFAULT', 'es')
    ist = config.get('DEFAULT', 'ist')
    print ("Es ist ", es + ist)

    mi = datetime.now().strftime('%M')
    hour = datetime.now().strftime('%I')

    print ("##########################################")
    print ("Stunde " + hour)
    print ("minute " + mi)

    hourint = int(hour)


    if int(mi) >= 20 and hourint <= 8:
        hour = int(hour) + 1
        x = "0"
        hour = ((x) + str(hour))
        print ("Stunde plus eins gleich kleiner 8 " +hour)	

    if int(mi) >= 20 and hourint >= 9 and hourint <= 11:
        hour = int(hour) + 1
        hour = (str(hour))
        print ("Stunde plus eins nach 9 " +hour)
 
    if int(mi) >= 20 and hourint == 12:
        hour = ("01")
        print ("Stunde plus eins nach 9 " +hour)


    hour = config.get('DEFAULT', hour)
    h = hour.split(",")
    #print (h)

    #Es ist (color z.B. 255, 255, 0)
    
    #strip.setPixelColor(4, color)
    #strip.setPixelColor(5, color)
    #strip.setPixelColor(7, color)
    #strip.setPixelColor(8, color)
    #strip.setPixelColor(9, color)

    # Volle Stunden anzeigen aus ini file

    try:
        #strip.setPixelColor(int(h[0]), color)
        print (int(h[0]))
    except:
        print ("")
    try:
        #strip.setPixelColor(int(h[0]), color)
        print (int(h[1]))
    except:
        print ("")
    try:
        #strip.setPixelColor(int(h[0]), color)
        print (int(h[2]))
    except:
        print ("")
    try:
        #strip.setPixelColor(int(h[0]), color)
        print (int(h[3]))
    except:
        print ("")
    try:
        #strip.setPixelColor(int(h[0]), color)
        print (int(h[4]))
    except:
        print ("")
    try:
        #strip.setPixelColor(int(h[0]), color)
        print (int(h[5]))
    except:
        print ("")

    # ab hier beginnt vor
    if int(mi) in range (20,30) or int(mi) in range (45,60):
        fvor = ("vor")
        fvor = config.get('DEFAULT', 'vor')
        
        h = fvor.split(",")

        try:
            #strip.setPixelColor(int(h[0]), color)
            #strip.setPixelColor(int(h[1]), color)
            #strip.setPixelColor(int(h[2]), color)
            print ("vor als Wort Wert1", h[0])
            print ("vor als Wort Wert1", h[1])
            print ("vor als Wort Wert1", h[2])
        except:
            print ("vor kein Wert")
        

    if int(mi) in range (35,45) or int(mi) in range (5,15):
        
        fnach = config.get('DEFAULT','nach')
        h = fnach.split(",")
        try:
            print ("nach als Wort")
            #strip.setPixelColor(int(h[0]), color)
            #strip.setPixelColor(int(h[1]), color)
            #strip.setPixelColor(int(h[2]), color)
            #strip.setPixelColor(int(h[3]), color)
        except:
            print ("vor kein Wert") 

    for a in range (20,45):
         halb = config.get('DEFAULT','halb')
         h = halb.split(",")
         
         if a == int(mi):
             try:
                 #strip.setPixelColor(int(h[0]), color)
                 #strip.setPixelColor(int(h[1]), color)
                 #strip.setPixelColor(int(h[2]), color)
                 #strip.setPixelColor(int(h[3]), color)
                 print ("halb als Wort")
             except:
                 print ("halb kein Wert 4")

      # fuenf minuten als Wort anzeigen
        
    if int(mi) in range (5,10) or int(mi) in range (35,40) or int(mi) in range (25,30) or int(mi) in range (55,60):
        ffuenf = config.get('DEFAULT','fuenf')
        h = ffuenf.split(",")
        try:
           #strip.setPixelColor(int(h[0]), color)
           #strip.setPixelColor(int(h[1]), color)
           #strip.setPixelColor(int(h[2]), color)
           #strip.setPixelColor(int(h[3]), color)
           print ("fuenf als Wort") 
        except:
           print ("fuenf als Wort kein Wert 4") 


# zehn minuten als Wort anzeigen
        
    if int(mi) in range (10,15) or int(mi) in range (40,45) or int(mi) in range (20,25) or int(mi) in range (50,55):
        
        fzehn = config.get('DEFAULT','zehn')
        h = fzehn.split(",")
        try:
            #strip.setPixelColor(int(h[0]), color)
            #strip.setPixelColor(int(h[1]), color)
            #strip.setPixelColor(int(h[2]), color)
            #strip.setPixelColor(int(h[3]), color)
            print ("zehn als Wort")
        except:
             print ("zehn als Wort no value 4") 



# viertel als Wort anzeigen
    if int(mi) in range (15,20) or int(mi) in range (45,50):
        fviertel = config.get('DEFAULT','viertel')
        h = fviertel.split(",")
        try:
            #strip.setPixelColor(int(h[0]), color)
            #strip.setPixelColor(int(h[1]), color)
            #strip.setPixelColor(int(h[2]), color)
            #strip.setPixelColor(int(h[3]), color)
            print ("viertel als Wort")
        except:
            print ("fuenf als Wort no value 4") 

    if (mi[1:] == "1") or (mi[1:] == "6"):
        #strip.setPixelColor(0, color)
        print ("Eine Minute")
                
    elif mi[1:] == "2" or (mi[1:] == "7"):
        #strip.setPixelColor(0, color)
        #strip.setPixelColor(1, color)
        print ("Zwei Minute")        

    elif mi[1:] == "3" or (mi[1:] == "8"):
        #strip.setPixelColor(0, color)
        #strip.setPixelColor(1, color)
        #strip.setPixelColor(2, color)
        print ("Drei Minute")       

    elif mi[1:] == "4" or (mi[1:] == "9"):
        #strip.setPixelColor(0, color)
        #strip.setPixelColor(1, color)
        #strip.setPixelColor(2, color)
        #strip.setPixelColor(3, color)
        print ("Vier Minute")


    #strip.show()
    time.sleep(wait_ms/1000.0)

if __name__ == '__main__':        

	#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	#strip.begin()

    while True:                  
        clock()