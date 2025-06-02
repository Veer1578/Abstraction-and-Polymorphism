from abc import ABC, abstractmethod

class ABsclass(ABC):
    def print(self, x):
        print('Passed value:', x)

    @abstractmethod
    def task(self):
        print('We are inside ABsclass task method')

class test_class(ABsclass):
    def task(self):
        print("We are inside test_class task")

obj = test_class()
obj.task()
obj.print(100)