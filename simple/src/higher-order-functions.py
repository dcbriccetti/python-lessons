def map(nums_list, operation):
    ''' Return a sequence of values obtained by applying the operation
    function to each number in nums_list. '''
    return [operation(num) for num in nums_list]

def double(num):
    return num * 2

def triple(num):
    return num * 3

nums_list = (1, 3, -10)

for operation in (double, triple):
    print(map(nums_list, operation))
