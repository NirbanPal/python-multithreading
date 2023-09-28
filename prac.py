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




class Employee:
    @staticmethod
    def display(n):
        print("Current Thread",current_thread())
        for i in range(n):
            print("ASD")


t1=Thread(target=Employee.display,args=(5,))
t1.start()

print("current thread name",current_thread())
for i in range(5):
    print("wow")


