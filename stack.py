class stack():
    def __init__(self):
        self.contents = []

    def push(self, item):
        print('weird {0}'.format(item))
        if item is not None:
            self.contents.insert(0, item)
        else:
            return 'Cant push empty item'

    def remove(self):
        return self.contents.pop(0)

    def size(self):
        return self.contents.count()

    # return the top item of the stack
    def peak(self):
        return self.contents[0]

    def list_Items(self):
        return self.contents.copy()

    def empty(self):
        pass


if __name__ == '__main__':
    testStak = stack()
    testStak.push(0)
    testStak.push('test')
    testStak.push()
    print(testStak.list_Items())

