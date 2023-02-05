with open('../mbox-short.txt', 'r') as file:
    lines = file.readlines()
    list1 = []
    counter = 0
    new_dict = {}

    for i in lines:
        if i.find("Received") == 0:
            counter += 1
            list1.append(i)
            continue
    new_dict["the number of found items"] = counter
    new_dict["all found items"] = list1
print(new_dict)