from functools import wraps
from typing import Callable, Any
import time 

def get_time(func: Callable) -> Callable:
    """gets the time of the given function"""
    
    def wrapper(*args,**kwargs)-> Any:
        """wrapper docstring"""
        
        start_time: float = time.perf_counter()
        result: Any = func(*args,**kwargs)
        end_time: float = time.perf_counter()
        print(f"Ran:{func.__name__} in {end_time - start_time: .2f} second")

        return result
    return wrapper

@get_time
def expensive_function() -> None:
    """expensive_function() docstring"""
    time.sleep(5)
    print("done")

def main() -> None:
    expensive_function()

if __name__ == "__main__":
    main()