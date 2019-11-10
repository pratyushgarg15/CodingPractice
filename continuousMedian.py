import math

class MinHeap:
	
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        self.heap = array
        for i in range(len(self.heap)//2,-1,-1):
            self.minHeapify(i)
            
        return array    

			
    def minHeapify(self,i):
        minimum = i
        
        if(self.left(i) < len(self.heap) and self.heap[self.left(i)] < self.heap[i] ):
            minimum = self.left(i)
        else:
            minimum = i
        if(self.right(i) < len(self.heap) and self.heap[self.right(i)] < self.heap[minimum] ):
            minimum = self.right(i)
			
        if(minimum != i):
            self.heap[i], self.heap[minimum] = self.heap[minimum], self.heap[i]
            self.minHeapify(minimum)
			
			
    def siftDown(self):
        self.minHeapify(0)

    def siftUp(self):
        i= len(self.heap)-1
        while(self.parent(i)>=0 and self.heap[i] < self.heap[self.parent(i)]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
			
    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop()
        self.siftDown()
        return val

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()
        
    def heapSort(self):
        arr = []
        while(len(self.heap) != 0):
            arr.append(self.remove())
            
        print(arr)    
		
    def parent(self, i):
        return math.floor((i-1)/2)
    
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2

    def size(self):	
        return len(self.heap)

class MaxHeap:
    
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        self.heap = array
        for i in range(len(self.heap)//2,-1,-1):
            self.maxHeapify(i)
            
        return array    

            
    def maxHeapify(self,i):
        maximum = i
        
        if(self.left(i) < len(self.heap) and self.heap[self.left(i)] > self.heap[i] ):
            maximum = self.left(i)
        else:
            maximum = i
        if(self.right(i) < len(self.heap) and self.heap[self.right(i)] > self.heap[maximum] ):
            maximum = self.right(i)
            
        if(maximum != i):
            self.heap[i], self.heap[maximum] = self.heap[maximum], self.heap[i]
            self.maxHeapify(maximum)
            
            
    def siftDown(self):
        self.maxHeapify(0)

    def siftUp(self):
        i= len(self.heap)-1
        while(self.parent(i)>=0 and self.heap[i] > self.heap[self.parent(i)]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
            
    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop()
        self.siftDown()
        return val

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()
        
    def heapSort(self):
        arr = []
        while(len(self.heap) != 0):
            arr.append(self.remove())
            
        print(arr)    
        
    def parent(self, i):
        return math.floor((i-1)/2)
    
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2 

    def size(self):	
        return len(self.heap)        


class continuousMedianHandler:
            
    def __init__(self):
        self.median = None
        self.lowerHalf = MaxHeap([])
        self.upperHalf = MinHeap([])

    def insertVal(self, val):
        if(self.lowerHalf.size() == 0):
            self.lowerHalf.insert(val)
            
        elif(val > self.lowerHalf.peek()):
            self.upperHalf.insert(val)
        else:
            self.lowerHalf.insert(val)
            
        #Balacing both the halves    

        if(self.lowerHalf.size() - self.upperHalf.size() >= 2):
            self.upperHalf.insert(self.lowerHalf.remove())

        if(self.upperHalf.size() - self.lowerHalf.size() >= 2):
            self.lowerHalf.insert(self.upperHalf.remove())

        # Calculating Median
        
        if(self.lowerHalf.size() < self.upperHalf.size()):
            self.median = self.upperHalf.peek()

        elif(self.lowerHalf.size() > self.upperHalf.size()):
            self.median = self.lowerHalf.peek()

        else:
            #self.median = (self.lowerHalf.peek() + self.upperHalf.peek())/2
            self.median = self.lowerHalf.peek()

    def getMedian(self):
        return self.median            

                        


if __name__ == '__main__':
    
    with open('Median.txt') as file:
        arr = [int(line) for line in file]

    med = continuousMedianHandler()  
    res = 0
        
    for i in range(len(arr)):
        med.insertVal(arr[i])
        res += med.getMedian()
        #print(med.getMedian(),end =',')
        
    print(res%10000)    

