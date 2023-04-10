import time
import os
import sys
import requests
import json

#colores facheritos xd :)
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


print("""\033[32m
▄▄▌ ▐ ▄▌.▄▄ ·      
██· █▌▐█▐█ ▀.     
██▪▐█▐▐▌▄▀▀▀█▄  \033[31m  WS VERSION 1.0 \033[32m
▐█▌██▐█▌▐█▄▪▐█    
 ▀▀▀▀ ▀▪ ▀▀▀▀     
 \033[35m
   """)
api_key = 'a34d97f03e51e991d6699b9de0b8694c'
number = input('Número: ')
print("")

   # Petición

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

      print("%s: %s" % (key, value))
      print("")
