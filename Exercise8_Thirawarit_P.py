if __name__ == '__main__' :
    print("====Login...====")
    username = input("Username : ")
    password = input("Password : ")
    if username == "Thirawarit" and password == "1234" :
        print("Welcome back! ",username,", Please select item in a cart..")
        print("----List----")
        print("1. Donut --5$-- per piece")
        print("2. Hotdog --10$-- per piece")
        print("3. Cookie --15$-- per piece")
        num = int(input("Select : "))
        print("You order : ",num, '\n', "-------------------")
        unit = int(input("Input Unit :"))
        if num == 1 :
            total = 5*unit
        elif num == 2 :
            total = 10*unit
        elif num == 3 :
            total = 15*unit
        else :
            total = "N/A"
            print("error!!")
            
            
        print("Total cost is ",total, "$")
    else :
        print("Usename and Password is not correct. Please try again.")