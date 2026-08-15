class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []

        for i in range(n):
            maxval = -1

            for j in range(i + 1, n):
                maxval = max(maxval, arr[j])

            ans.append(maxval)
            
        return ans