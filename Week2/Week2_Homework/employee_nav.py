import sys
def form_dict(data):
    data_dict = {}
    for item in data:
        data_dict[item[0]] = {
            'worth': item[1],
            'subordinate_ids': item[2]
        }
    return data_dict

def calculate_worth(data_dict, id, worth_list=[]):
    try:
        worth_list.append(data_dict[id]['worth'])
        if data_dict[id]['subordinate_ids']:
            for sub_id in data_dict[id]['subordinate_ids']:
                calculate_worth(data_dict, sub_id, worth_list)
    except:
        print("Unexpected error: invalid key")
    return worth_list

def main():
    data = [[1, 5, [2, 3]], [2, 3, [4]], [3, 3, []], [4, 2, []]]
    data_dict = form_dict(data)
    print(data_dict)
    
    print(sum(calculate_worth(data_dict, 1, [])))
    

if __name__ == "__main__":
    main()