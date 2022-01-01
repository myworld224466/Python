#Digital Clock in Console Mode

import time, os

while True:
    lt=time.localtime()
    result=time.strftime('%I:%M:%S %p',lt)
    os.system('cls')
    print('Local Time:',result)
    time.sleep(3) #To perform after 3 seconds
