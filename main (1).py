# Enter your code here. Read input from STDIN. Print output to STDOUT

class Set():
    def __init__(self, size_of_arr, size_of_set, arr, set_a, set_b):
        self.size_of_arr = size_of_arr
        self.size_of_set = size_of_set
        self.arr = arr
        self.set_a = set_a
        self.set_b = set_b
    
    def calculate_happiness(self):
        counter = 0
        for item in arr:
            if item in set_a:
                counter += 1
            elif item in set_b:
                counter -= 1
        
        print(counter)

if __name__ == '__main__':
    size_of_arr, size_of_set = input().split()
    size_of_arr = int(size_of_arr)
    size_of_set = int(size_of_set)
    arr = input().split()
    set_a = set(input().split())
    set_b = set(input().split())
    counter = 0

    my_object = Set(size_of_arr, size_of_set, arr, set_a, set_b)
    my_object.calculate_happiness()