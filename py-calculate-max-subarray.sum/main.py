class CalculateMaxSubArraySum:
    
    # 
    #
    def sum_max_subarray_n3(self, arr):
        
        current_max = 0
        for i in range(len(arr) - 1):
            for j in range(i, len(arr) +1 ):
                current_max = max(current_max, sum(arr[i:j]))
        return current_max

    # Kadane's algorithm, using dynamic programming principle
    # O(n) time and O(1) space
    def sum_max_subarray_n(self, arr):
        max_ending_here = max_so_far = 0

        for x in arr:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

    #
    # 
    def maximum_circular_subarray(self, arr):
        max_subarray_sum_wraparound = sum(arr) - self.min_subarray_sum(arr)
        return max(self.max_subarray_sum(arr), max_subarray_sum_wraparound)

    def max_subarray_sum(self, arr):
        max_ending_here = max_so_far = 0

        for x in arr:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

    def min_subarray_sum(self, arr):
        min_ending_here = min_so_far = 0

        for x in arr:
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)

        return min_so_far