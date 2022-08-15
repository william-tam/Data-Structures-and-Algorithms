# Insertion Sort Algorithm

A = [4,7,89,90,32,45,3,44]

n = len(A)
def insertion_sort():
    for j in range(n): 
        key = A[j]
        i = j - 1
        while i > 0 and A[i]> key: 
            A[i+1]=A[i]
            i=i-1
            A[i+1]=key
    return key

def main():
    key = insertion_sort()
    print(key)

if __name__ == '__main__':
    main()