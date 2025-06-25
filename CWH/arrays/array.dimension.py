import numpy as np
list1=([1,2,3])
list2=([[1,2,3],[4,5,6]])
list3=([[[1,2,3],[4,5,6],[7,8,9]]])
array1=np.array(list1)
array2=np.array(list2)
array3=np.array(list3)
print("Array 1D:-\n",array1)
print("Array 2D:-\n",array2)
print("Array 3D:-\n",array3)

print(array1.ndim)
print(array2.ndim)
print(array3.ndim)