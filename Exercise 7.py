import urllib2
import json

print "Welcome to openweathermap.org p15151 version..."
print "Since you are reading this,you wish to learn about the weather for a specific region..."
print "------------------------------------------------------------"
print "Please input the coordinates of the region you desire...then leave the rest to me..."

c=0
while c==0:
    #User inputs longitude...
    c0=0
    while (c0==0):
        c1=0
        while (c1==0):
            x=input ("What's the longitude (x) of the coordinates???")
            if (type(x)==int):    #making sure x is an integer smaller than 180 and bigger than -180...
                if (x<180 and x>-180):
                    c1=1
        #User inputs latitude...
        c2=0
        while (c2==0):
            y=input ("What's the latitude (y) of the coordinates???")
            if (type(y)==int):    #making sure y is an integer smaller than 90 and bigger than -90...
                if (y<90 and y>-90):
                    c2=1

        #User gets a chance to correct the coordinates of the region...
        c3=0
        while (c3==0):
            print "Are you sure the longitude(x) is %s and the latitude(y) is %s ???" % (x,y)
            answer=raw_input("Press 'Y' for Yes or 'N' for No...")
            if (answer=="N" or answer=="n"):
                c3=1
            if(answer=="Y" or answer=="y"):
                c3=1
                c0=1

    #Taking information from openweathermap.org for the coordinates...
    x=str(x)
    y=str(y)
    url="http://api.openweathermap.org/data/2.5/weather?lat=" +y+ "&lon=" +x+ "&appid=01e7a487b0c262921260c09b84bdb456"
    a=urllib2.urlopen(url)
    info = json.load(a)

    if(info["weather"][0]["main"]=="rain"):
        print "I'm singing in the rain!"
    tempk=info["main"]["temp"]
    #Diverting the temperature from Kelvin to Celsius...
    tempc=tempk-273.15
    print "Planet Earth,huh???"
    if (tempc>20):
        print "nice...%s Degrees of Celsius" %(tempc)
    elif (tempc<5):
        print "brrrr...%s Degrees of Celsius" %(tempc)
    else:
        print "Meh...%s Degrees of Celsius" %(tempc)
    print "------------------------------------------------------------"

    #User can choose between terminating the program or re-inputing coordinates...
    c4=0
    while (c4==0):
        print "Would you like to learn about the weather in another region?"
        answer1=raw_input("Press 'Y' for Yes or 'N' for No...")
        if (answer1=="N" or answer1=="n"):
            c4=1
            c=1
        if(answer1=="Y" or answer1=="y"):
            c4=1

print "Thanks for visiting us!!!"
bye=input("\m/ (^_^) \m/")
bye="Bye!"
