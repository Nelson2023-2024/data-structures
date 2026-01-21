class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * 7

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    def print_table(self):
        for index, value in enumerate(self.data_map):
            print(index, ": ", value)

    def set_item(self, key, value):
        index = self.__hash(key) # produces an index
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None


my_hash_table = HashTable()
my_hash_table.set_item("cats", 200)
my_hash_table.set_item("dogs", 400)
my_hash_table.set_item("crocodiles", 600)
my_hash_table.set_item("washers", 690)
print(my_hash_table.get_item("cats"))
my_hash_table.print_table()