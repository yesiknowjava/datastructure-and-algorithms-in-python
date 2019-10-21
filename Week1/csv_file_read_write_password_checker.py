import sys, csv, re, getpass 
if __name__ == "__main__":
    username = raw_input("Enter the username : ")
    password = getpass.getpass("Enter the password : ", stream=None)

    if not re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', password) \
    or not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", username):        
        print "Invalid Username / Password"
        exit()
    else:
        authenticated = False
        with open('credentials.csv','rt') as readfile:
            data = csv.reader(readfile)
            for row in data:
                if username == row[0] and password == row[1]:
                    authenticated = True
        readfile.close()
        if authenticated:
            print "User Authenticated"
        else:
            print "User Not Authenticated"
            print ""
            new_user = raw_input("\nDo you want to add this to the file ?")
            if new_user:
                with open('credentials.csv','a') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerow([username, password])
                writeFile.close()

            
            
        
                
                    
            