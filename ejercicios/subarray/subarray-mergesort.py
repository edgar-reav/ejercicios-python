from random import randint
from timeit import default_timer

def generaLista(n):
  Lista = [randint(-100,100) for i in range(2**n)]
  return Lista

# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:
		# Finding the mid of the array
		mid = len(arr)//2
		# Dividing the array elements
		L = arr[:mid]
		# into 2 halves
		R = arr[mid:]
		# Sorting the first half
		mergeSort(L)
		# Sorting the second half
		mergeSort(R)
		i = j = k = 0
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
# Code to print the list

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


n = randint(1,20)
arr = generaLista(n)
print(n)
#print("Given array is", end="\n")
print(arr)
#printList(arr)
mergeSort(arr)
#print("Sorted array is: ", end="\n")
#printList(arr)
print(arr)