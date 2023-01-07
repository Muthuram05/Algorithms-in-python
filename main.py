class sorting():
    def bubbleSort(self,arr):
        n = len(arr)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j + 1]:
                    swapped = True
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]           
            if not swapped:
                return
        return arr
    def insertionSort(self,arr):
        for i in range(1, len(arr)): 
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
            arr[j + 1] = key
        return arr

if __name__ == "__main__":
    detector = sorting()
