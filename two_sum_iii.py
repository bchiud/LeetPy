class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.occurances = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.occurances[number] = self.occurances.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for k in self.occurances.keys():
            complement = value - k
            if complement in self.occurances:
                if complement != k or (complement == k and self.occurances[k] >= 2):
                    return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
