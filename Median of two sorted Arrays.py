def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    while left <= right:
        partition1 = (left + right) // 2  
        partition2 = (m + n + 1) // 2 - partition1  
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]  
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 1:
                return max(maxLeft1, maxLeft2)
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1
    raise ValueError("Input arrays are not sorted or there is no solution.")
print(findMedianSortedArrays([1, 3], [2]))  
print(findMedianSortedArrays([1, 2], [3, 4]))  
print(findMedianSortedArrays([0, 0], [0, 0]))  
print(findMedianSortedArrays([], [1]))  
print(findMedianSortedArrays([2], []))  