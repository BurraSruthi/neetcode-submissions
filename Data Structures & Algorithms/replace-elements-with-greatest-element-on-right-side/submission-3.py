class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1] * n
        maxval = arr[n - 1]

        for i in range(n - 2, -1, -1):
            res[i] = maxval
            maxval = max(maxval, arr[i])
        return res