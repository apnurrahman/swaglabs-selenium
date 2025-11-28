class sort:
    def sort(self, array):
        pass

class insertion_sort(sort):
    def sort(self, array):
        #set two counter, x and y. x is always higher than y
        for x in range(1, len(array)):
            check = array[x]
            y = x - 1
            #swap to left if x is lesser than y
            while y >= 0 and check < array[y]:
                array[y+1] = array[y]
                #swap to left until x is greater than y
                y -= 1
            array[y+1] = check
            print(array)

class merge_sort(sort):
    def sort(self, array):
        pass
    def merge(self, left_side, right_side):
        pass
    
arr = [6, 1, 3, 5, 4, 7]
sort_c = insertion_sort()
sort_c.sort(arr)
#print(arr)