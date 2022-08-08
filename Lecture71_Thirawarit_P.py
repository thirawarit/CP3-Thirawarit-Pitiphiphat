manulist = {"hotdog":'10$',"omlet":'15$'}
while True :
    print("This is manu, sir..",'\n',manulist.item())
    Name = input("Name : ")
    if Name.lower() == "done" :
        break
    else :
        print(manulist[Name])
        manulist.values()
