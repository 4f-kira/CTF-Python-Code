#!/usr/bin/env python 
import time,sys,os
tchar = [
'''  ___   
 / _ \  
| | | | 
| | | | 
| |_| | 
 \___/  
        ''',''' __  
/_ | 
 | | 
 | | 
 | | 
 |_| ''',''' ___   
|__ \  
   ) | 
  / /  
 / /_  
|____| ''',''' ____   
|___ \  
  __) | 
 |__ <  
 ___) | 
|____/  ''',''' _  _    
| || |   
| || |_  
|__   _| 
   | |   
   |_|   ''',''' _____  
| ____| 
| |__   
|___ \  
 ___) | 
|____/  ''','''   __   
  / /   
 / /_   
| '_ \  
| (_) | 
 \___/  ''',''' ______  
|____  | 
    / /  
   / /   
  / /    
 /_/     ''','''  ___   
 / _ \  
| (_) | 
 > _ <  
| (_) | 
 \___/  ''','''  ___   
 / _ \  
| (_) | 
 \__, | 
   / /  
  /_/   '''
]
db = ''' _  
(_) 
    
 _  
(_) 
    '''

while(1):
  print '\n'.join([''.join([' '.join(((tchar[int(c)] if c.isdigit() else db).split('\n'))[i]) for c in time.strftime('%H:%M:%S',time.localtime(time.time()))]) for i in range(6)])
  time.sleep(0.1)
  os.system('cls' if os.name == 'nt' else 'clear')