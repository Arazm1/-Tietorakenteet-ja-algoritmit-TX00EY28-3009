def combine_lists(list1, list2):
    work_in_progress = list1

#i = 1
    for i in list2:
#j = 2
        inserted = False
        for j in work_in_progress:
            if i < j:
                work_in_progress.insert(work_in_progress.index(j), i)
                inserted = True
                break
    
        if not inserted:
            work_in_progress.append(i)

    return work_in_progress

#list1 = [1, 3, 5]
#list2 = [2, 4, 6]

#combined_list = combine_lists(list1, list2)

#print(combined_list)


