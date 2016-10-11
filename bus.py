import hashlib
import time
from time import sleep
import requests
from gpiozero import LED




#Seven segment number configurations
#      A
#    -----
# F |  G  | B
#    -----
# E |     | C
#    -----
#      D
# [A,B,C,D,E,F,G]
#Initialize pins
pins = [0, 18, 21, 17, 4, 1, 22]
leds = [LED(pin,active_high=False) for pin in pins]

one = [0,1,1,0,0,0,0]
two = [1,1,0,1,1,0,1]
three = [1,1,1,1,0,0,1]
four = [0,1,1,0,0,1,1]
five = [1,0,1,1,0,1,1]
six = [1,0,1,1,1,1,1]
seven = [1,1,1,0,0,0,0]
eight = [1,1,1,1,1,1,1]
nine = [1,1,1,0,0,1,1]
zero = [1,1,1,1,1,1,0]
none = [0,0,0,0,0,0,0]


#function to set LEDs
def segShow(numb):
        for i, led in enumerate(leds):
                if numb[i] == 1:
                        led.on()
                else:
                        led.off()

#Main loop
while True:

   #put together URL
   key = "#########################" + time.strftime("%Y%m%d%H")
   key_bytes = key.encode('utf-8')
   m = hashlib.md5(key_bytes).hexdigest()
   stopId = "36232658"
   service = "69"
   urlRequest = "http://ws.mybustracker.co.uk/?module=json&key=" + m + "&function=getBusTimes&stopId=" + stopId + "&refService=" + service
   
   # just for sebug
   #print(urlRequest);

   #Make requests
   r = requests.get(urlRequest)
   j = r.json()
   first = j['busTimes'][0]['timeDatas'][0]['minutes']

   #Display
   for service in j['busTimes']:
      print "======" + service['mnemoService'] + "======"
      for bus in service['timeDatas']:
         print(bus['nameDest'] + " - " + str(bus['minutes']))
         print("---------")

   #Set pins

   if first == 0:
      segShow(zero)
   elif first == 1:
      segShow(one)
   elif first == 2:
      segShow(two)
   elif first == 3:
      segShow(three)
   elif first == 4:
      segShow(four)
   elif first == 5:
      segShow(five)
   elif first == 6:
      segShow(six)
   elif first == 7:
      segShow(seven)
   elif first == 8:
      segShow(eight)
   elif first == 9:
      segShow(nine)
   else:
      segShow(none)

   sleep(20)
