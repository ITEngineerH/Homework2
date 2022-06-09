from ListCDE  import *
Opt = ListCDE()  



class Menu:
    def __init__(self):
        self.app()

    def app(self):
        option = 0
        while option <5:
            print(" ")
            print("****************Principal Menu**************")
            print("1. Enter Digits")
            print("2. Get LIst")
            print("3. Get Values")
            print("4. Get All")
            print("5. Exit")
            option=int(input("**************Select an option:  "))
            print(" ")

            if (option == 1):
                data=int(input("enter the first number:  "))
                #CircularList(data)
                Opt.finalAdd(data)

                data=int(input("enter the second number:  "))
                #CircularList(data)
                Opt.finalAdd(data)

                data=int(input("enter the third number:  "))
                #CircularList(data)
                Opt.finalAdd(data)


                data=int(input("enter the fourth number:  "))
                #CircularList(data)
                Opt.finalAdd(data)


                data=int(input("enter the fifth number:  "))
                #CircularList(data)
                Opt.finalAdd(data)
               

            elif(option == 2):
                #CircularList.printing(data)
                Opt.printing()

            elif(option == 3):
                dataS=int(input("enter the numbers:  "))
                Opt.search(dataS)

            elif(option == 4):
                Opt.printing()
                Opt.search(dataS)
                #print(Opt.first.prev.data)
                #print(Opt.last.next.data)

            elif(option == 5):
                print("If needed start the program again")


launch = Menu()