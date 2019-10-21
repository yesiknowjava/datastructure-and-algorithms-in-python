def sort(array):
    if len(array) <= 1:
        return array
    midpoint = int(len(array) / 2)
    left, right = sort(array[:midpoint]), sort(array[midpoint:])
    return merge(left, right)


def merge(left, right):
    result = []
    left_pointer = right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

def create_array(size=10, max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

def main():
    array = create_array()
    print(array)
    result = sort(array)
    print(result)

if __name__ == "__main__":
    main()