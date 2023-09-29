#threads-> 1.Each thread has a unique name 
# 2.Naming:-Thread-[%d] First thread:- Thread-1 second thread: Thread - 2 etc(except main thread. Name of main thread is MainThread)
# 3. Name of the thread is stored in 'name' attribute of thread object

from threading import Thread,current_thread,main_thread,active_count,enumerate
from time import sleep
def display():
    # If you have to use the information of main Thread in the running thread in this situation you can use the main_thread function in the running thread
    print("Main thread details",main_thread())
    for i in range(4):
        print("hello world")
        # sleep(1)
def show():
    for i in range(4):
        print("moto")

t1=Thread(target=display)
t2=Thread(target=show)
#to rename the thread name. Here we have chaned the thread1 name to Nirban
t1.name="Nirban"
#you also can change the name of main thread. To change the name of main thread you have to call the current_thread() object

print(current_thread().name)
current_thread().name="Nirban Main"
print("After renaming main thread",current_thread().name)

print("name",t1.name)
print("name",t2.name)

# if you use enumarate. This will return the details list of active threads

print("After renaming main thread enumerate",enumerate())


#Thread Identifiers
# -> Thread identifier -> 1.this is given by process 2. Each thread has a unique identifier(id) with in a pythonprocess. 3. id number is given by python interpreter 4. Read-only positive integer only and unique id number in process 4. assigned after thread is started 5. this id is stored in an instance variable called ident. 
# -> Native Identifier -> 1. this is given by operating system.
# 2. Each thread has a unique identifier assigned by the operating system.
# 3. property name:- native_id (assigned after thread has started.)
# Note:- generally, ident and native_id are same.but they are from different identifiers


# if we want to get the id we have to start the thread atfirst.
print("Before",t1.is_alive())
t1.start()
print("Number of running threads",active_count())
print("After",t1.is_alive())
t2.start()
print("Number of running threads after t2",active_count())
print(t1.ident,t1.native_id)
print(t2.ident,t2.native_id)




#pid (identifier os your process or program). to see this import os module and print(os.getpid())
import os
print("process or program id in os",os.getpid())


#Count of current running threads
#details of all threads

#built-in functions for threads
#1. is_alive() :- Checks thread is running or not
#2. main_thread() :- Returns main threads details
#3. active_count() :- Number of running threads
#4. enumerate() :- List of all running threads
#5. get_native_id() :- know the native id of thread












