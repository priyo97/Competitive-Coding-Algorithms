import random
import sys

def main():
	# a = [int(x) for x in input("Enter array:").split()];
	sys.setrecursionlimit(10000);
	a = list(range(15000));
	n = len(a);

	quicksort(a,0,n-1);
	print("After Sorting...");
	print(a[:30]);

def quicksort(a,low,high):
	if low < high:
		index = random.randrange(low,high+1);
		pivot = a[index];
		index = arrange(a,low,high,pivot);
		quicksort(a,low,index-1);
		quicksort(a,index+1,high);


def arrange(a,low,high,pivot):
	i = low;
	j = low;

	while i <= high:
		if a[i] < pivot:
			a[i],a[j] = a[j],a[i];
			j += 1;

		i +=1 ;
	a[j] = pivot;

	return j;

main();