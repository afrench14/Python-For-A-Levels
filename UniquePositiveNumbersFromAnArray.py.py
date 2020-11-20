#take ten integer inputs and pront only the unique positive ones

import append

def positive_unique_list():
    list_of_ten = []
    temp_list = []
    final_list = []
    list_input = False
    while list_input == False:
        add_to_list = int(input("choose an integer to be put into the list to sort: ")
        list_of_ten.append(add_to_list)
        if len(list_of_ten) == 10:
            list_input = True
    for i in list_of_ten:
        if i > 0:
            temp_list.append(i)
    for i in temp_list:
        if i not in final_list:
            final_list.append(i)

positive_unique_list()
        
