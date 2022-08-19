import collections
nums = [1, 2, 3]
# creating deque collection from the list
deque = collections.deque(nums)
print(deque)
print(collections.Counter(nums))
print(collections.UserList(nums))