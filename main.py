try :
    import threading
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

def MainLoopConsole(cVar,lock) :
    print("[+] Main Loop Console Process Started")
    x = " "
    while(x.lower()!='exit') :
        lock.acquire()
        try:
            x = input(">>> ")
        except :
            print("[!] InputError")
        print("[Echo] :",x)
    lock.release()
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

    lock = Lock()
    
    mainLoopProcess = Process(target=MainLoopConsole,args=(cVar,lock))
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
