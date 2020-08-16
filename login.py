username = "User_Name"
password = "12345"
un = ""
pw = ""
tries = 0
try_limit = 3
out_of_tries = False
while un != username and not(out_of_tries):
    un = input("Input username: ")
    tries +=1
    if tries == try_limit:
        out_of_tries = True
while pw != password and not(out_of_tries):
    pw = input("Input password: ")
    tries +=1
    if tries == try_limit:
        out_of_tries = True
if out_of_tries == True:
    print("INCORRECT")
else:
    print("CORRECT")
