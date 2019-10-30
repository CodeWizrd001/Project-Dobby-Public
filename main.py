import time

try :
    import threading
    from threading import Thread
except ImportError as error :
    print(error)
    print("Please Try Again After Installing 'threading'")
try :
    import multiprocessing
    from multiprocessing import Process,Manager,Lock,Queue
except ImportError as error :
    print(error)
    print("Please Try Again After Installing 'multiprocessing'")
try :
    import subprocess
    import os
except ImportError as error :
    print(error)
    print("Please Try Again After Installing Required Packages")

def MainLoopConsole(cVar) :
    time.sleep(1)
    print("[+] Main Loop Console Process Started")
    x = " "
    while(x.lower()!='exit') :
        try:
            x = input(">>> ")
        except :
            print("[!] InputError")
        print("[Dobby] : You Said",x)
    cVar['exit'] = 1 
    print("[*] Exit MainLoop Handle !") 

def BackGroundHandle(cVar) :
    print("[+] BackGround Handle Process Started")
    while(cVar['exit']!=1) :
        if(cVar['entered']==1) :
            print("[+] Backgroung Handle Running !")
            cVar['entered'] = 0 
    print("[*] Exit Background Handle !")

def main() :
    cVar = {}
    cVar['exit'] = 0 
    cVar['errors'] = [0,0,0,0,0]
    cVar['entered'] = 0
    
    mainLoopThread = Thread(target=MainLoopConsole,args=(cVar,))
    bgThread = Thread(target=BackGroundHandle,args=(cVar,))

    global Procs
    Procs = [mainLoopThread,bgThread]

    for p in Procs :
        p.start()
        print("[+] Start",p)
    

if __name__ == "__main__" :
    main()
    for p in Procs :
        while p.isAlive() :
            pass
        print("[+] Stopped",p) 
