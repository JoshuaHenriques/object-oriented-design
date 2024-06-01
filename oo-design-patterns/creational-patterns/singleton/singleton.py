# whenever a class is instantiated __new__ and __init__ methods are called
# __new__ method will be called when an object is created
# __init__ method will be called to initialize the object

# __call__ method enables the ability to write classes where the instances 
# behave like functions and can be called like a function

"""
Basic Class Implementation

In this example, the __new__ method is overridden to ensure that only one instance
of the class is created. If the instance does not exist, a new one is created; 
otherwise, the existing instance is returned.
"""
class SingletonA:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    
"""
MetaClass Implementation (thread-safe)

In this example, the SingletonMeta Metaclass manages instances, ensuring only 
one instance exists per class. The __call__ method intercepts class instantiation, 
creating and storing instances as needed. By applying the SingletonMeta Metaclass 
to classes the Singleton pattern is effortlessly enforced, allowing classes to 
concentrate solely on their business logic.
"""
from threading import Lock, Thread
class SingletonMeta(type):

    _instances = {}
    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument
        do not affect the returned instance.
        """
        
        # to prevent expensive lock operations every time 
        if cls not in cls._instances:
            """
            Now, imagine that the program has just been launched. Since there's no
            Singleton instance yet, multiple threads can simultaneously pass the
            previous conditional and reach this point almost at the same time. The
            first of them will acquire lock and will proceed further, while the
            rest will wait here.
            """
            with cls._lock:          
                """
                The first thread to acquire the lock, reaches this conditional,
                goes inside and creates the Singleton instance. Once it leaves the
                lock block, a thread that might have been waiting for the lock
                release may then enter this section. But since the Singleton field
                is already initialized, the thread won't create a new object.
                """
                if cls not in cls._instances:      
                    instance= super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        
        return cls._instances[cls]


class SingletonB(metaclass=SingletonMeta):
    """
    Here goes our class's business logic without concerning about
    handling the intricacies of the singleton pattern.
    """
    def __init__(self, value: str) -> None:
        self.value = value
        
def test_singleton(value: str) -> None:
    singleton = SingletonB(value)
    print(singleton.value)

"""
Decorator Implementation

In this example, the singleton decorator function manages instances of decorated 
classes. It ensures that only one instance of each class exists and returns the same 
instance when the class is instantiated. The SingletonClass is decorated with 
@singleton, turning it into a singleton, and any attempts to create new instances will 
return the existing instance.
"""

def singleton(cls):
    instances = {}  # Dictionary to store instances of different classes

    def get_instance(*args, **kwargs):
        # If class instance doesn't exist in the dictionary
        if cls not in instances:
            # Create a new instance and store it
            instances[cls] = cls(*args, **kwargs)  
        return instances[cls]  # Return the existing instance
    
    # Return the closure function for class instantiation
    return get_instance  


@singleton  # Applying the singleton decorator
class SingletonC:
    pass

if __name__ == "__main__":
    s1 = SingletonA()
    s2 = SingletonA()    
    print(id(s1) == id(s2))

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()

    s5 = SingletonC()
    s6 = SingletonC()
    print(id(s5) == id(s6))