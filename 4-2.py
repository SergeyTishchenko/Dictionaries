def is_unique_list(source_list):
    list_of_unique = []
    count = 0
    for j in range(len(source_list)):
        for i in range(len(source_list[j])):
            count += 1
            if source_list[j][i] not in list_of_unique:
                list_of_unique.append(source_list[j][i])
            else:
                pass
    if len(list_of_unique) == count:
        return 'Source list is unique'
    else:
        return 'Source list is not unique'


if __name__ == '__main__':
    print is_unique_list([[2, 3, 4], [5, 6], [7, 8, 9, 10]])
    print is_unique_list([[2, 3, 4], [6, 6, 7], [8, 9, 10]])
