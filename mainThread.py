# Main thread - > When a python script execute, Python Virtual Machine(PVM) creates a thread to run that program that is called main thread. Main thread is automatically called at the time of execution

# if you have a python code to run after starting the program python interpreter starts and it needs a thread to run the program and python interpreter request OS to create one thread called as main thread

# In your program there will be minimum one thread called as main thread. 

# The main thread is created by PVM

#thread are python objects of threading.Thread() class

import threading

# current thread object 
print(threading.current_thread())

# current thread object name (name attribute in current_thread object)
print(threading.current_thread().name)

# current thread identity (name attribute in current_thread object)
print(threading.current_thread().ident)

#current thread is started or not (name attribute in current_thread object) 
print(threading.current_thread().is_alive())


# print(t.currentThread().getName())