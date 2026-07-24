class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)

        # Count zeros
        zeros = arr.count(0)

        # i -> original array
        # j -> imaginary array after duplication
        i = n - 1
        j = n + zeros - 1

        while i < j:
            # Copy current element if it's within bounds
            if j < n:
                arr[j] = arr[i]

            # Duplicate zero
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0

            i -= 1
            j -= 1
                