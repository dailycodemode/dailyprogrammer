main_list = ["a", "b", "c", 1, 4]
secondary_list = ["a", "x", 34, "4"]

for item in secondary_list:
    if item not in main_list:
        main_list.append(item)

print(main_list)

print(main_list[:])