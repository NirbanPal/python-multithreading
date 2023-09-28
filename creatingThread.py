# There are two ways of creating threads 
# -using Thread class present in threading module
# 1.import thread class from threading module 
# 2.Create a function containing code to be executed parally
# 3. create a object of that THread class
# 4.Start created thread using start() method



# -using Thread class present in threading module
# 1.import thread class from threading module 
from threading import Thread,current_thread
# # 2.Create a function containing code to be executed parally
# def display(n,msg):
#     for i in range(n):
#         print(msg)
# # 3. create a object of that THread class
# t1=Thread(target=display,args=(4,"hello"))
# # 4.Start created thread using start() method
# t1.start()
# print(t1)


# def display(n,msg):
#     for i in range(n):
#         print(msg)
# t1=Thread(target=display,kwargs={'n':5,'msg':'hello pc'})
# t1.start()
# print(t1)


# def display(n):
#     #excured by tq thread
#     print("t1 thread details",current_thread())
#     for i in range(n):
#         print("Hello pc")
# t1=Thread(target=display,args=(5,))

# t1.start()

# # Executed by main thread
# for i in range(3):
#     print("Executed by main thread")


#if your code in a method in a class
#so how to create threads for methods

# class Example:
#     def display(self,n):
#         for i in range(n):
#             print("Home")


# e1=Example()
# t1=Thread(target=e1.display,args=(5,))
# t1.start()
# #executed by main thread
# for i in range(5):
#     print("Welcome")


# class Example:
#     @classmethod
#     def display(self,n):
#         for i in range(n):
#             print("Home")


# e1=Example()
# t1=Thread(target=Example.display,args=(5,))
# t1.start()
# #executed by main thread
# for i in range(5):
#     print("Welcome")



# class Example:
#     @staticmethod
#     #for the static method we need to remoce self and pass only the arguments
#     def display(n):
#         for i in range(n):
#             print("Home")


# e1=Example()
# t1=Thread(target=Example.display,args=(5,))
# t1.start()
# #executed by main thread
# for i in range(5):
#     print("Welcome")



# - by extending a the Thread class. Means you have to make a child class by inheriting the Thread class

from time import sleep
from threading import Thread
videos = ['oops syllabus', 'constructor','destructor','file handling']

#we are here inheriting the Thread method after inheriting that we will cretae the run method also. Here we are doing overwriting cause there is also a runmethod in the Thread which is inherited by Myclass

# class Myclass(Thread):
#     def run(self):
#         for vid in videos:
#             print(f"{vid} starting uploading")
#             sleep(3)
#             print(f"{vid} uploaded.")
        

# #here if we are creating an object of myclass that will be called a thread
# t1=Myclass()
# #to execute that thread
# t1.start()


# for i in range(4):
#     sleep(0.5)
#     print("Checking copyrights")


# in this class you also can use constructer but you need to handle an error. You have to inherite the constuctor from the Thread class then you can do use consrtuctor
class Myclass(Thread):
    def run(self):
        for vid in videos:
            print(f"{vid} starting uploading")
            sleep(3)
            print(f"{vid} uploaded.")
        

#here if we are creating an object of myclass that will be called a thread
t1=Myclass()
#to execute that thread
t1.start()


for i in range(4):
    sleep(0.5)
    print("Checking copyrights")










