
cab_type = {
    1: "Micro",
    2: "Mini",
    3: "Prime",
    4: "Suv"
}

cab_rate = {
    1: 10,
    2: 20,
    3: 30,
    4: 40
}

cabs_available = {
    1: [1111, 2222, 3333, 4444],
    2: [5555, 6666],
    3: [7777],
    4: [8888]
}

def start_app():
    start = raw_input("Would you like to book a cab : 1. Yes, 2. No ")
    return start

def cab_rate_calc(cab_type, start_km, end_km):
    total_km = int(end_km) - int(start_km)
    total_rate = total_km * cab_rate[int(cab_type)]
    return total_rate

def get_cab_type():
    cab_type = raw_input("Enter the cab type you require : 1. Micro, 2. Mini, 3. Prime, 4. Suv. Ex: Enter 1 for Micro and 2 or Mini ")
    return cab_type

def get_km(type="start"):
    if type=="start":
        km = raw_input("Enter start km ")
    else:
        km = raw_input("Enter end km ")
    return km

def get_details():    
    cab_type = get_cab_type()
    start_km = get_km(type="start")
    end_km = get_km(type="end")
    book_a_cab = ""
    if cab_type in ["1", "2", "3", "4"]:        
        total_rate = cab_rate_calc(cab_type, start_km, end_km)
        print "Your total fare would be : {} ".format(total_rate)
        book_a_cab = raw_input("Would you like to book this cab. Press any key to continue. ")
    return cab_type, start_km, end_km, book_a_cab

# def main():
#     print "main"


if __name__ == "__main__":
    user_input = start_app()
    while user_input == "1":
        cab_type, start_km, end_km, book_a_cab = get_details()          
        if book_a_cab:
            if len(cabs_available[int(cab_type)]) > 0:
                print "The cab number you have booked is {}".format(cabs_available[int(cab_type)].pop())
                user_input = start_app()
            else:
                print "The requested cab type is not available."
    