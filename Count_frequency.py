# it returns a dictionary data structure whose keys are array elements and values are their 
# corresponding frequencies {1: 4, 2: 4, 3: 2, 5: 2, 4: 1} 
import collections 

def CountFrequency(arr): 
	return collections.Counter(arr) 

if __name__ == "__main__":
	arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5] 
	freq = CountFrequency(arr) 
	# iterate dictionary named as freq to print count of each element  
	for key, value in freq.iteritems(): 
		print(key, " -> ", value)
