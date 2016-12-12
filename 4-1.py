def avg_negatine_mean(source_list):
    lst = []
    for j in range(len(source_list)):
        for i in range(len(source_list[j])):
            if source_list[j][i] < 0:
                lst.append(source_list[j][i])
    if len(lst) == 0:
        return 'No negative value in source list'
    else:
        pass
    return round(sum(lst)/len(lst))

if __name__ == '__main__':
    print avg_negatine_mean([[0, -5, -7], [-2, 4, -3], [-7, 0, 7]])
    print avg_negatine_mean([[0, 5, 7], [2, 4, 3], [7, 0, 7]])