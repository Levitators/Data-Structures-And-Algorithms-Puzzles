#Set Apart ODD Numbers on RIght and Even Numbers on Left in a List


Input  = [12, 34, 45, 9, 8, 90, 3]

def sepearte(arr):

	left = 0
	right = len(arr)-1

	while(left < right):
		while(arr[left]%2==1 and left < right):
			#print arr[left]
			left += 1

		while(arr[right]%2==0 and left < right):
			#print arr[left]
			right -= 1

		if (left < right):
			arr[left],arr[right] = arr[right],arr[left]
			left += 1
			right -= 1


sepearte(Input)
print Input
