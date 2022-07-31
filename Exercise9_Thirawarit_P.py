if __name__ == '__main__' :
    user = input("Username : ")
    pw = input("Password : ")
    while user != "admin" or pw != "1234" :
        print("Username and Passwrod is not correct!")
        user = input("Username : ")
        pw = input("Password : ")
    print("Welcome back! ", user, ".")
