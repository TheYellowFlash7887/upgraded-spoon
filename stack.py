from typing import List

class Stack:
    def __init__(self):
        self.contents = []

    def push(self, item: Object):
        self.contents.append(item)

    def pop(self) -> Object:
        return self.contents.pop()

    def __len__(self) -> int:
        return len(self.contents)

    def __str__(self) -> str:
        return self.contents
    
    def __repr__(self) -> List:
        return repr(self.contents)
    
    def copy(self):
        return self.contents.copy()

    def empty(self):
        pass


if __name__ == '__main__':
    testStak = stack()
    testStak.push(0)
    testStak.push('test')
    testStak.push()
    
    secondStack = testStak.copy()
    
    print(testStak)
    print(len(testStak))

