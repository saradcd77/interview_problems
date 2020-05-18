
""" Leet Code Easy Problem """
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
def merge_sorted_list(nums1, nums2):

    index = 0
    while nums2:
        index -= 1
        nums1[index] = nums2.pop()
    nums1.sort()
    return nums1

print(merge_sorted_list([1,3,4,0,0,0],[2,3,5]))
print(merge_sorted_list([1,2,3,0,0,0],[2,5,6]))
