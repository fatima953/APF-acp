nums1 = [4,5,7]
nums2 = [3,8,9]
resault = map(lambda x,y: x + y, nums1, nums2)
print("Addition of two lists")
print(list(resault))
a1 = {1,2,3,4}
a2 = {5,6,7,8}
a3 = list(zip(a1,a2))
print(a3)