print("Welcome")
print(
    """    Create a custom Array
    """)


class MyArray():
    
    _length =0
    _data={}
    
    def __init__(self) -> None:
        self._length=0
        self._data={}
    
    def push(self,element):
        self._data[self._length] =element
        self._length += 1
        pass
    
    def length(self):
        return self._length
    
    def pop(self):
        last_element = self._data[self._length-1]
        del self._data[self._length-1]
        self._length -=1
        return last_element
    
    def get(self,index):
        if index > self._length: return None
        return self._data[index]
        
        
        
myArray = MyArray()
myArray.push(123)
myArray.push(321)
myArray.push(421)
myArray.pop()
print(myArray.length())
print(myArray._data)
print(myArray.get(22))