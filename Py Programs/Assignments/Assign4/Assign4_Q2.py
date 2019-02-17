class Assign4_Q2:
   def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num] + 1, i + 1)
            lookup[num] = i
print("Output: %d, %d" % Assign4_Q2().twoSum((10,20,10,40,50,60,70),50))

#original pythonanywhere
class py_solution:
   def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num] + 1, i + 1)
            lookup[num] = i
print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))