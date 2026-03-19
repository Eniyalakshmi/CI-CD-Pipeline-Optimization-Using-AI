def calculate_sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total


if __name__ == '__main__':
    nums = [10, 20, 30, 40, 50]
    result = calculate_sum(nums)
    print('Sum is:', result)
