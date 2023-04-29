# This algorithm locate the smallest window in an array that must be sorted. 
# The return is two indexes: left and right.
# This algorithm takes O(nlogn) time and space, for a new array is created using sorted() function.

class LocateSmallestWindowToBeSorted:

    def is_eq(self, value_from_arr, value_from_sorted_arr):
        if(value_from_arr == value_from_sorted_arr):
            return True
        else:
            return False
    
    def is_none(self, value):
        return value is None

    def window_nlogn(self, array):
        left, right = None, None
        s = sorted(array)
        
        for i in range(len(array)):
            if not self.is_eq(array[i], s[i]) and self.is_none(left):
                left = i
            elif not self.is_eq(array[i], s[i]):
                right = i

        return left, right
    
# This algorithm locate the smallest window in an array that must be sorted. 
# The return is two indexes: left and right.
# The complexity of time and space of this algorithm is, respectively, O(n) and O(1). 
# O(1) space complexity because no new array is created.
# O(n) time complexity because the array is traversed linearly.
    def window_n(self, array):
        left, right= None, None
        n = len(array)
        max_seen, min_seen = -float("inf"), float("inf")
        
        for i in range(n):
            max_seen = max(max_seen, array[i])
            if array[i] < max_seen:
                right= i
        
        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, array[i])
            if array[i] > min_seen:
                left= i
        
        return left, right