import multiprocessing
import threading
from multiprocessing import Process,Manager
import subprocess

def MainLoopConsole(cVar) :
    print("[+] Main Loop Console Process Started")
    x = " "
    while(x.lower()!='exit') :
        try:
            x = input(">>> ")
        except :
            print("[!] InputError")
        print("[Echo] :",x)
    cVar['exit'] = 1 

def BackGroundHandle(cVar) :
    print("[+] BackGround Handle Process Started")
    while(cVar['exit']!=1) :
        if(cVar['entered']==1) :
            print("[+] Backgroung Handle Running !")
            cVar['entered'] = 0 
    print("[*] Exit Background Handle !")

def main() :
    manager = Manager()
    cVar = manager.dict()
    cVar['exit'] = 0 
    cVar['errors'] = [0,0,0,0,0]
    cVar['entered'] = 0

    mainLoopProcess = Process(target=MainLoopConsole,args=(cVar,))
    bgProcess = Process(target=BackGroundHandle,args=(cVar,))

    Procs = [mainLoopProcess,bgProcess]

    for p in Procs :
        p.start()
        print("[+] Start",p)
    for p in Procs :
        p.join()
        print("[+] Join",p)
    

if __name__ == "__main__" :
    main()
