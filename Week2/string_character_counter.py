

def main():
    string_value = "prabhakar"
    counter_dict = {}
    for i in string_value:
        if i in counter_dict:
            counter_dict[i] = counter_dict[i] + 1
        else:
            counter_dict[i] = 1
    print(counter_dict)

if __name__ == '__main__':
    main()