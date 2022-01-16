class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_to_idx = {}
        self.list = []
        self.size = 0


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_idx:
            return False

        self.val_to_idx[val] = len(self.list)
        self.list.append(val)
        self.size += 1
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_to_idx:
            return False

        cur_idx = self.val_to_idx[val]
        last_val = self.list[self.size - 1]

        self.list[cur_idx] = last_val
        self.val_to_idx[last_val] = cur_idx

        del self.val_to_idx[val]
        self.list.pop()
        self.size -= 1

        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()