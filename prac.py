from threading import Thread,current_thread

# class Employee:
#     @classmethod
#     def display(self,n):
#         print("Current Thread",current_thread())
#         for i in range(n):
#             print("ASD")


# t1=Thread(target=Employee.display,args=(5,))
# t1.start()

# print("current thread name",current_thread())
# for i in range(5):
#     print("wow")




# class Employee:
#     @staticmethod
#     def display(n):
#         print("Current Thread",current_thread())
#         for i in range(n):
#             print("ASD")


# t1=Thread(target=Employee.display,args=(5,))
# t1.start()

# print("current thread name",current_thread())
# for i in range(5):
#     print("wow")
from time import sleep

videos=["Inheritance","Polymorphism","Constructor","Destructor"]

class MyClass(Thread):
    def __init__(self,val):
        self.kid=val
        Thread.__init__(self)

    def compressor(self):
        print("Compressing")

    def run(self):
        a=2
        b=3
        self.res=a+b
        if self.kid is True:
            print("Video is for kid")
        for i in videos:
            print(f"{i}uploading")
            self.compressor()
            sleep(1)
            print("Checking")


t2=MyClass(False)
t2.start()
sleep(10)
print("res",t2.res)

for i in range(4):
    print("Completed")










