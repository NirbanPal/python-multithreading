from threading import Thread
import time

print("Using multi threading")

def squre(n):
    print("Finding squre")
    time.sleep(1)
    print(n*n)

def cube(n):
    print("Finding cube")
    time.sleep(1)
    print(n**3)

st=time.time()
t1=Thread(target=squre,args=(2,))
t2=Thread(target=cube,args=(2,))
t1.start()
# t1.join()
t2.start()
t2.join()
print("Time taken",time.time()-st)




print("***************not using multi threading**********************")

def squre(n):
    print("Finding squre")
    time.sleep(1)
    print(n*n)

def cube(n):
    print("Finding cube")
    time.sleep(1)
    print(n**3)

stn=time.time()
squre(2)
cube(2)
print("Time taken",time.time()-stn)

