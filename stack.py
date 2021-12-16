
class Stack:
    def __init__(self):
        self.contents = []

    def push(self, item: object):
        self.contents.append(item)

    def pop(self) -> object:
        return self.contents.pop()

    def __len__(self) -> int:
        return len(self.contents)

    def __str__(self) -> str:
        return str(self.contents)
    
    def __repr__(self) -> str:
        return repr(self.contents)
    
    def copy(self):
        return self.contents.copy()

    def empty(self):
        pass


if __name__ == '__main__':
    testingStack = Stack()
    testingStack.push('item')
    print(testingStack)
    testingStack.push('item2')
    print(testingStack)
    stack2 = testingStack.copy()
    testingStack.pop()
    print(testingStack)
    print(stack2)