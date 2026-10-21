import numpy as np

python_list = [1,2,3,4,5]
numpy_array = np.array(python_list)

float_array = np.array(python_list, dtype=float)
print(float_array)

bool_array= np.array([0,1,-1,0,0], dtype=bool)
print(bool_array)
print(numpy_array)


two_dimensional_list=[[0,1,2],[3,4,5],[6,7,8]]
numpy_two_d = np.array(two_dimensional_list)
print(numpy_two_d)
print('shape:', numpy_two_d.shape)

arr = np.array([1,2,3,4,5])
print(arr + 10)
print(arr - 10)
print(arr * 10)
print(arr / 10)
print(arr ** 2)

two_d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print('First row:', two_d[0])
print('Second row:', two_d[1])
print('Third row:', two_d[2])

print('First column:', two_d[:,0])
print('Second column:', two_d[:,1])
print('Third column:', two_d[:,2])
print(two_d[0:2, 0:2])

arr = np.array([1,2,3,4,5])
arr[0] = 100
print(arr)

two_d[0][0] = 99
print(two_d)

zeros = np.zeros((3,3))
ones = np.ones((3,3))

print(zeros)
print(ones)

flat = np.arange(1,10)
print('flat:', flat)

reshaped = flat.reshape(3,3)
print('reshaped:')
print(reshaped)

grid = np.array([[1,2,3],[4,5,6],[7,8,9]])
flat_again = grid.flatten()
print(flat_again)

a = np.array([1,2,3])
b = np.array([4,5,6])

print('hstack:', np.hstack((a,b)))
print('vstack:')
print(np.vstack((a,b)))

print(np.random.rand(3,3))
print(np.random.randint(0,10, (3,3)))

nums = np.array([2,4,6,8,10])

print('min:', np.min(nums))
print('max:', np.max(nums))
print('mean:', np.mean(nums))
print('median:', np.median(nums))
print('std:', np.std(nums))
print('sum:', np.sum(nums))

print(np.linspace(0,10,5))
print(np.linspace(0,1,6))