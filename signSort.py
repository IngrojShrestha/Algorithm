def signSort(A, n):
    """
    Reorder the elements of A so that all negative integers are positioned to the left of all non-negative integers.

    Time complexity: O(n)

    :param A: an Array of integers
    :param n: size of array
    :return: an array with  all negative integers positioned to left of all non-negative integers.
    """
    j = 0
    for i in range(0, n):
        if A[i] < 0:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            j = j + 1
    return A


def main():
    A = [1, 4, -5, -8, 3, 8, -9]

    print("Array before signSort: ", A)

    signSort(A, len(A))

    print("Array after signSort: ", A)


main()
