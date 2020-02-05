import math


def mergeSort(A, l, h):
    """
    Performs merge Sort on an array A

    :param A: an array
    :param l: start index of array
    :param h: end index of array
    """

    if l < h:
        mid = (l + h) // 2

        mergeSort(A, l, mid)

        mergeSort(A, mid + 1, h)

        merge(A, l, mid, h)
    else:
        return A  # base case


def merge(A, l, mid, h):
    """
    Merge operation of two sub arrays
    where first sub-array includes elements in the index range[l, mid+1), and
    second sub-array includes elements in the index range [mid+1,h+1)

    :param A: an Array
    :param l: start index of the array
    :param mid: mid index of the array
    :param h: end index of the array
    """

    # copy elements of first sub-array to L and second sub-array to R
    L = A[l:mid + 1]
    R = A[mid + 1:h + 1]

    L.append(math.inf)
    R.append(math.inf)

    i = 0  # initial index of first sub-array
    j = 0  # initial index of second sub-array

    # combine elements in first sub-array and sub-array to array A sorted in ascending order
    for k in range(l, h + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def main():
    A = [1, 5, 9, 2, 6, 8, 7, 4, 0, 3]
    mergeSort(A, 0, len(A) - 1)
    print(A)


main()
