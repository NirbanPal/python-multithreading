from threading import Thread
from time import sleep
def upload():
    print("uploading")
    sleep(3)
    print("Video uploaded")

def notificaions():
    print("sending notifications to subscribers")

t1=Thread(target=upload)
t2=Thread(target=notificaions)
t1.start()
# t1.join() means it will hold the execution of t2. After completion of t1 then t2 and main thread will be executed
t1.join()
t2.start()

#main thread
for i in range(4):
    print("hello")


# Here the code of sending notification is dependent on uploading video. In this case you can use join method. You can keep the notification function waiting till uploads gets completed.

# When to use join method? If a thread wants to wait for some other thread , then we should go for join method   



print("******************another example*********************")
def uploading():
    for i in range(5):
        print("Uploaded")
        # sleep(1)
        print("Done")

def notifications():
    for i in range(5):
        print("New video uploaded")


#if you want to hold a thread until a thread is completed tehn you have to use t1.join().for instance of i want to execute the thread 1 completely and then the thread 2 and main thread will be executed then we have to use t1.join() only. But if we want that thread 1 will completly excuted and then thread 2 so in this case we have to use t1.join() and t2.join() after declaring the start function of both the threads. if i want to execute the thread 1 and thread 2 together then after complete execution of both threads main thread will run. In this case we have to use t2.join() only  
t1=Thread(target=uploading)
t1.start()
# t1.join()
t2=Thread(target=notifications)
t2.start()
t2.join()



    
for i in range(5):
    print("welcome")



    