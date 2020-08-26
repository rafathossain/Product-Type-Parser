type_list = []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("source.txt", "r")
    for data in file:
        if data.strip() != "" and data.strip() not in type_list:
            type_list.append(data.strip())
            type_list = sorted(type_list)

    output = open("type.txt", "w")
    output.write(",".join(type_list))
    output.close()
    print(type_list)
