class Both:
    def __init__(self):
        self.sum = 0
        self.product = 1

    def calculate_both(self,array):
        for val in array:
            self.sum+=val
            self.product*=val

        print(f"The sum is {self.sum}")
        print(f"The product is {self.product}")

instance = Both()
array = [2,4,5,2,9,7]
instance.calculate_both(array)
