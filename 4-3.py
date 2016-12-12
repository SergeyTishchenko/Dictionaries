def add_sum_to_the_last_element(source_list):

    for i in range(len(source_list)):
        source_list[i][-1] = sum(source_list[i][:-1])
    return source_list


if __name__ == '__main__':
    print add_sum_to_the_last_element([[1, 5, 7, 9], [5, 7, 7]])
