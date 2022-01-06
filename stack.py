import typing
from typing import TypeVar, Generic, List

# adding a parameterized type to your stack
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.contents: List[T] = []

    def push(self, item: T) -> None:
        self.contents.append(item)

    def pop(self) -> T:
        return self.contents.pop()

    def __len__(self) -> int:
        return len(self.contents)

    def __str__(self) -> str:
        return str(self.contents)
    
    def __repr__(self) -> str:
        return repr(self.contents)
    
    def copy(self) -> List[T]:
        return self.contents.copy()

    def empty(self):
        return not self.contents


if __name__ == '__main__':
    
    # now you want a stack of ints
    testingStack = Stack[int]()
    testingStack.push(0)
    
    # and you, as a lazy developer, tries to push a string
    testingStack.push('item')
    
    # now install mypy
    # pip install mypy
    
    # and do a type check. During build time, you would see a bug in the code
    # but, without the type checking system, python would run and your program may have a bug in runtime. You would spend hours troubleshooting
    # to find out that someone pushed the wrong type to stack. This is the relevance/importance of a type system/type check on a programming language
    # It doesn't solve all the bugs, but it can catch quite a few during development, and not in production.
    
    # mypy stack.py
    
