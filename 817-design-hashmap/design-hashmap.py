class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.arr)):
            if self.arr[i][0] == key :
                self.arr[i][1] = value 
                break
        else :
            self.arr.append([key,value])

    def get(self, key: int) -> int:
        # check if the key exists or not , if present then return its values or otherwise return -1 
        for i in range(len(self.arr)):
            if self.arr[i][0] == key :
                return self.arr[i][1]
        else :
            return -1 

    def remove(self, key: int) -> None:
        # check if the key exists or not , if present then remove the entire pair
        remove_index = -1 
        for i in range(len(self.arr)):
            if self.arr[i][0] == key :
                remove_index = i 
        if remove_index != -1 :
            self.arr.pop(remove_index)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)