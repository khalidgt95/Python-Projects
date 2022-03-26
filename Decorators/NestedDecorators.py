import functools
from typing import Any, Callable, Dict, Tuple


def decorator_1(func: Callable) -> Callable:
    def wrapper(*args: Tuple[Any], **kwargs: Dict[Any, Any]) -> None:
        print(f"Inside decorator_1")
        func(*args, **kwargs)    
        print(f"Inside decorator_1")
    return wrapper

def decorator_2(func: Callable) -> Callable:
    def wrapper(*args: Tuple[Any], **kwargs: Dict[Any, Any]) -> None:
        print(f"Inside decorator_2")
        func(*args, **kwargs)    
        print(f"Inside decorator_2")
    return wrapper

def decorator_3(func: Callable) -> Callable:
    def wrapper(*args: Tuple[Any], **kwargs: Dict[Any, Any]) -> None:
        print(f"Inside decorator_3")
        func(*args, **kwargs)    
        print(f"Inside decorator_3")
    return wrapper

#--------- increment any value by 'n' times -----------#

def show_result_decorator(func: Callable) -> Callable:
    def wrapper(*args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
        print(f"Inside wrapper")
        v = func(*args, **kwargs)    
        print(f"Outside wrapper")
        return v
    return wrapper

def multiplier(number: int) -> Callable: 
    def decorator_multiplier(func: Callable) -> Callable:
        def wrapper(*args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
            return number * func(*args, **kwargs)
        return wrapper
    return decorator_multiplier

def increment10Times(num_times: int) -> Callable:

    def decorator_incrementer_1(func: Callable) -> Callable:
    
        @functools.wraps(func)
        def wrapper(*args: Tuple[Any], **kwargs: Dict[Any, Any]) -> int:
            
            val: int = 0
            
            for _ in range(num_times):
                val += func(*args, **kwargs)

            return val

        return wrapper
    
    return decorator_incrementer_1 

@decorator_3
@decorator_2
@decorator_1
def func() -> None:
    print("func")

#---------- Incremented Demo -----------#
@show_result_decorator
@multiplier(number=5)
@increment10Times(num_times=10)
def inc(val: int) -> int:
    return val
