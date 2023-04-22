#
# Considering the array a = [3, 2, 1]. This algorithm computes as follow:
# a[0] = a[1] * a[2], which means a[0] = 2 * 1;
# a[1] = a[0] * a[2], which means a[1] = 3 * 1;
# a[2] = a[0] * a[1], which means a[2] = 3 * 2;
# The result is: [2, 3, 6]
#
# O(n) time and space, since iterating over the input array takes O(n)
# time and the prefix and suffix arrays take up 0( n) space.

class GetProductOfAllOtherElements:

    def is_less_than_two_elements(self, nums):
        if len(nums) < 2:
            return True

        return False
    
    def compute_element_and_insert(self, products, num):
        if products:
            return products[-1] * num
        else:
            return num

    def compute_prefix_products(self, nums):
        # prefix products
        prefix_products = []
        for num in nums:
            prefix_products.append(self.compute_element_and_insert(prefix_products, num))

        return prefix_products
    
    def compute_suffix_products(self, nums):
        
        # suffix products
        suffix_products = []
        for num in reversed(nums):
            suffix_products.append(self.compute_element_and_insert(suffix_products, num))
        
        suffix_products = list(reversed(suffix_products))
        return suffix_products
    
    def get_element(self, i, prefix_products, suffix_products, nums):
        if i == 0:
            return suffix_products[i + 1]
        elif i == len(nums) - 1:
            return prefix_products[i - 1]
        else:
            return prefix_products[i-1] * suffix_products[i + 1]
        
    def is_first_element(self, i):
        return i == 0
    
    def is_last_element(self, i, nums):
        return i == len(nums) - 1

    def compute_product(self, nums):

        if self.is_less_than_two_elements(nums):
            return nums

        prefix_products = self.compute_prefix_products(nums)
        suffix_products = self.compute_suffix_products(nums)
        
        result = []
        for i in range(len(nums)):
            if self.is_first_element(i):
                result.append(self.get_element(i, prefix_products, suffix_products, nums))
            elif self.is_last_element(i, nums):
                result.append(self.get_element(i, prefix_products, suffix_products, nums))
            else:
                result.append(self.get_element(i, prefix_products, suffix_products, nums))

        return result