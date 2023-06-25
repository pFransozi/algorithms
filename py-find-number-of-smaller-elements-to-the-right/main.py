# This algorithm counts how many numbers are smaller 
# to the right of a number in the array

class FindNumbersOfSmallerElementsToTheRight:

    def smaller_counts_in_naive_way(list):
        result = []

        for item, element_value in enumerate(list):                                              #O(n)
            count = sum(current_value < element_value for current_value in list[item + 1:])      #O(n)
            result.append(count)
                                                                                                #O(n²)
        
        return result
    
    def smaller_counts(list_arg):
        import bisect

        result_list = []
        seen = []

        for num in reversed(list_arg):
            i = bisect.bisect_left(seen, num)
            result_list.append(i)
            bisect.insort(seen, num)

        return list(reversed(result_list))
    

