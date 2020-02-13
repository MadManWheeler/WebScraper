import requests
import serial 
import time
from bs4 import BeautifulSoup
price = 0

def Gled_on():
    ser.write(b'1')

def Rled_on():
    ser.write(b'0')

def Bled_on():
    ser.write(b'2')

ser = serial.Serial('com4',9600)
while 1==1:
        
    page = requests.get('https://www.ebay.co.uk/itm/Toshiba-65VL5A63DB-65-Direct-LED-4K-Smart-TV-Black/392646432470?epid=9035013285&hash=item5b6b8d16d6%3Ag%3Ac8gAAOSwbTVeJbUb&LH_Auction=1')
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.find_all('p'))
    
    oldPrice = price
   
    price = soup.find(class_='notranslate')
    price = str(price)
    
    print(price)
    
    price = (price[82:-7])
    
    print (price)

    oldPrice = float(oldPrice)
    price = float(price)

   # file = open('priceCheck.txt','a')
    #file.write('\n' + price)
   # file.close()

    

    buffer = 0
    while(buffer<30000000):
        buffer+=1

    if(oldPrice > price):
        Gled_on()

    elif(oldPrice < price):
        Rled_on()

    elif (oldPrice == price):
        Bled_on()
        

    print('done')

    time.sleep(6)





ser = serial.Serial('com4',9600)

time = 0
while(time<30000000):
    time+=1

if(oldPrice > price):
    Gled_on()

elif(oldPrice < price):
    Rled_on()

elif (oldPrice == price):
    Gled_on()
    Rled_on()

print('done')




#ser = serial.Serial('/dev/tty.usbserial', 9600) >>> while True: ... print ser.readline() '1 Hello world!\r\n' '2 Hello world!\r\n' '3 Hello world!\r\n' 


