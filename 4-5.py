def find_unique_elements(array):
    result = []

    def unpack(array):
        for item in array:
            if isinstance(item, list):
                unpack(item)
            else:
                result.append(item)

    unpack(array)

    return len(result) == len(set(result))

if __name__ == '__main__':
    print(find_unique_elements([[433, 2, 2, 9, 231, 543], [323, 534, 577], [0, 4678, -6], [1, 5, 7]]))
    print(find_unique_elements([[433, [2, 777, 9], 231, 543], [323, 534, 577], [0, 4678, -6], [1, 5, 7]]))
    print(find_unique_elements([[433, [2, -77, 9], 231, 543], [323, 534, 577], [0, 4678, -6], [1, 5, 7]]))
    print find_unique_elements([3, 2, 2])
    print find_unique_elements([2, 3, 4, 5])
