#real Example
import time


def note_time_decorator(func): # func is called by log_function()
    def wrapper():
        start_time = time.time() # start time will be noted
        func() #calling the function
        end_time = time.time() #end time is noted
        result = end_time - start_time
        print(f"Function {func.__name__} took {result} seconds to execute")
        print("time taken" +str(end_time-start_time))
        return result
    return wrapper

@note_time_decorator
def log_function():
    time.sleep(2)
    print("Executing log_function")

# Calling the decorated function
log_function()
@note_time_decorator
def reporting_function():
    time.sleep(3)
    print("Generating report")
reporting_function()