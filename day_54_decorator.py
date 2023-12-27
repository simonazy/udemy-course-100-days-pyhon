# from flask import Flask 

# app = Flask(__name__)

# @app.route('/')
# def landing():
#     return 'Hello!' 

# if __name__=='__main__':
#     app.run()


"""What is a decorator? 
Literally, it provides a wrapper for allowing something to happend before/after the 
the function is executed.""" 
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(5) #do somthing before
        function() 
        #do something after
    return wrapper_function 

@delay_decorator
def say_hello():
    start_time = time.time()
    print("Saying Hello~")
    print(f"Spending {time.time() - start_time}")

# @delay_decorator
def say_hi():
    start_time = time.time()
    print("Saying hi~") 
    print(f"Spending {time.time() - start_time}")

say_hello()
say_hi()