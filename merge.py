def main():
	a = [int(x) for x in input("Enter array:").split()];
	n = len(a);

	mergesort(a,0,n-1);

	print("After Sorting...");
	print(a);

def mergesort(a,low,high):
	if(low<high):
		mid = (low+high)//2;
		mergesort(a,low,mid);
		mergesort(a,mid+1,high);
		merge(a,low,mid,high);

def merge(a,low,mid,high):
	temp = [];
	j = low;
	k = mid+1;
	
	while True:
		if(j>mid):
			temp.extend(a[k:high+1]);
			break;
		elif(k>high):
			temp.extend(a[j:mid+1]);
			break;
		elif(a[j]<=a[k]):
			temp.append(a[j]);
			j += 1;
		elif(a[k]<=a[j]):
			temp.append(a[k]);
			k += 1;
	

	a[low:high+1] = temp;

main()
