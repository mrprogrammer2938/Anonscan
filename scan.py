#!/usr/bin/python3
# This code write by (Ms.nope)
# anonscan
# version 
from colorama import Fore,init
import os
import subprocess
import time
import socket
init()
class color:
    green = '\033[92m'
    red = '\033[91m'
    End = '\033[0m'
    orn = '\033[33m'
ip = color.green + "Enter ip: " + color.End
ext = color.green + "Exiting... " + color.End
def anonscan():
    time.sleep(1)
    os.system("clear")
    print("""
              
                                                  
                    ....'',,;;;;,,'...                
            .;coxk0KKXNNWWWMMMMWWWNXK0Oxol;'.        
         ,o0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0x;.     
       .oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.    
       oWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.   
      ,KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:   
      oWMMWXkdooodk0NWMMMMMMMMMMMMMN0xollldkKWMMMx.  
     .kMWOdol;...  .':kNMMMMMMMMNkc'. ....;cldONMO'  
     ,KWKOKWMXxoc'...  ,OMMMMMM0;  ...,coxXMWXOKWX;  
     :NMMMMMMMMMWXd;'..'xWMMMMMk,'..;dKWMMMMMMMMMN:  
     cWMMMMMMMMMMMMNk,.lXMMMMMMNd,:xNMMMMMMMMMMMMWc  
     lWMMWKxl:;;:coONK; cNMMMMM0okNNOoc;;;:cdKWMMWl  
     oMNOc.         'ol..xMMMMMMMXd'         .cx0Xl  
     oMO'..'',,;;:::cko. oMMMMMMMNklcclllllloodxxO: 
     oWX0KXNWWWMMMMMMMd  oMMMMMMMMMMMMMMMMMMMMMMMMo  
     ,KMMMMMMMMMMMMMMNc  oMMMMMMMMMMMMMMMMMMMMMMMWl 
      ;KMMMMMMMMMMMMM0'  dMMMMMMMMMMMMMMMMMMMMMMMK,   
     .,:xNMMMMMMMMMW0:   dMMMMMMNXWMMMMMMMMMMMMXx'     
      cd.'cldxxxk00c... .kMMMMMMXkxKMWKOOOOOkdcc:.   
      .do.'..d0KNW0,.xc ,KMMMMMMMM0OWWXOkx; ''.oc    
       .xd:c..o0WMWK0No :NMMMMMMMMMMMMMMKc.,x:lx.    
        .kk:;. .,lx0KKo..lxxkxc:xNMWNKkc. :x:lk,     
         .k0c,:;.   ..    ;;'.   ';;'.  ,lc,oO,      
          .xKc.;odo:,....cO0Oo.   ..':oOKl'xk'       
           .oXd. ;xKNNXK0OOkkkkkOO0XWMMNxlOx.        
             cKx. :0KK00OOO0000NMMMMMMXxd0o.         
              ;0x.oMMWNKd.    ;0MMMMMKxk0:           
               'kdoXMMMMK,    dMMMMMW00k'            
                .l0WMMMWo     cNMMMMMNd.             
                  ,OWMMN:     ,KMMMMK:               
                   .dNMWo     :NMMNx'                
                     ,xXO'   .xWKd,                  
                       .'.    ',.                    
                                        """ + Fore.GREEN + """          
                   █▓▒░░Anon scan░░▒▓█ """ + Fore.BLUE + """
             ---[ Code writer : Ms.nope ] -------
        ------[ github : https://github.com/msprogrammer2938/ ] -------- """ + Fore.WHITE + """
                         version : 1.2.0 \n""")
    web = str(input(ip))
    time.sleep(1)
    print(color.red + "\n===================================port scanning==================================" + color.End)
    work1 = subprocess.getoutput("nmap -Pn " + web).replace("Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times will be slower.","openning: " + web).replace("Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-25 06:03 MDT","All ports: ")
    print(work1)
    print(color.red + "===================================ping test======================================" + color.End)
    print(color.orn)
    os.system("ping -w 4 " + web)
    time.sleep(1)
    print(color.red + "===================================web info=======================================" + color.End)                     
    work2 = subprocess.getoutput("whois " + web).replace("% [whois.apnic.net]","openning: " + web).replace("% Whois data copyright terms    http://www.apnic.net/db/dbcopyright.html","starting AnonScan!")
    print(work2)
    time.sleep(1)
    print(color.red + "===================================nslookup=======================================" + color.End)
    time.sleep(1)
    work3 = subprocess.getoutput("nslookup " + web)
    print(work3)
    time.sleep(1)
    print(color.red + "===================================web location===================================" + color.End)
    work4 = subprocess.getoutput("curl https://api.hackertarget.com/geoip/?q=" + web).replace("  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current","searching...").replace("IP Address:","\nIP Address:")
    print(work4)
    con()
def con():
    try1 = str(input("Do you want to try again? [y/n] "))
    if(str(try1) == 'y'):
      anonscan()
    elif(str(try1) == 'n'):
        os.system("clear")
        time.sleep(1)
        print(ext)
        exit(1)
    else:
        con()
anonscan()


    
