expense_track=dict()
option=0
budget=0

while option<=7:
    try:
        print("1.INITIAL AMOUNT")
        print("2.ADD INITIAL AMOUNT")
        print("3.ENTER EXPENSE")
        print("4.VIEW EXPENSE")
        print("5.EDIT EXPENSE")
        print("6.DELETE EXPENSE")
        print("7.EXIT")
        option=int(input("enter your option:"))
        if option==1:
            if budget!=0:
                print("You already initialed budget...!!!")
            else:
                while True:
                    try:
                        budget=int(input("enter your budget"))
                        if budget>0:
                            break
                        else:
                            print("Invali input!!")
                    except:
                        print("invalid input! please enetr an integer for budget")
                print("initial amount",budget)
                print("============================")
                print("Expense"," Amount")
                print("--------" , "-------")
                for x,y in expense_track.items():
                    print(x,"     ",y)
            

        elif option==2:
            while True:
                try:
                    extra_budget=int(input("enter your extra_budget"))
                    if extra_budget>0:
                        break
                    else:
                        print("invalid input!!")
                except:
                    print("invalid input!,please enter an integer")
            if extra_budget<0:
                print("enter a positive number:")
            else:
                budget=budget+extra_budget
                print("your current budget=",budget)
                print("initial amount",budget)
                print("============================")
                print("Expense"," Amount")
                print("--------" , "-------")
                bal=0
                for x,y in expense_track.items():
                    print(x,"     ",y)
                    bal=bal+y
                print("----------------")
                print("balance=",budget-bal)
            
            
        elif option==3:

            
            if budget==0:
                print("you must enter the budget first")
            else:
                bal=0
                for x,y in expense_track.items():
                    bal=bal+y
                bal=budget-bal
                if bal==0:
                        print("Your budget is low!!")
                else:
                    while True:
                        expense=input("enter your expense:")
                        if expense=="":
                            print("its invalid!!!\nTry again:")
                        else:
                            if expense in expense_track:
                                print("name already exist,enter another name")
                            else:
                                break
                    while True:
                        try:
                            amount=int(input("enter amount:"))
                            if amount>0:
                                break
                            else:
                                print("invalid input!!!")
                        except:
                            print("invalid input!!,please enter an integer for the amount")       
                    if bal<amount:
                        print("Your budget is low,try again after adding budget!!")
                    else:
                        expense_track[expense]=amount
                        bal=0
                        print("initial amount",budget)
                        print("==========================")
                        print("Expense"," Amount")
                        print("-------" , "-------")
                        for x,y in expense_track.items():
                            print(x,"     ",y)
                            bal=bal+y
                        print("----------------")
                        print("balance=",budget-bal)
        elif option==4:
            print("initial amount",budget)
            print("===========================")
            print("Expense"," Amount")
            print("-------" , "-------")
            for x,y in expense_track.items():
                print(x,"     ",y)
            print("----------------")
            print("balance=",budget-bal)
        elif option==5:
            if budget==0:
                print("you must enter the budget first")
            else:
                old_expense=input("enter the name of expanse to edit:")
                if old_expense in expense_track:
                    while True:
                        new_expense=input("enter the new_expense:")
                        if new_expense in expense_track:
                            print("name is already exist,enter another name")
                        else:
                            if new_expense=="":
                                print("You must enter a expense")
                            else:
                                break
                
                    expense_track[new_expense]=expense_track[old_expense]
                    expense_track.pop(old_expense) 
                    print("edited successfully")       
                    '''print("initial amount",budget)
                    print("===============================")
                    print("Expense"," Amount")
                    print("-------" , "-------")
                    for x,y in expense_track.items():
                        print(x,"     ",y)
                    print("----------------")
                    print("balance=",budget-bal)'''
                else:
                    print("expense not found")
        elif option==6:
            if budget==0:
                print("You must enter the budget first!")
            else:
                while True:
                    name=input("which expense you want to delete:")
                    if name in expense_track:
                        print("name is found")
                        break
                    else:
                        print("invalid input,Try again!")
                expense_track.pop(name)     
                print("expense deleted")
                bal=0
                print("initial amount",budget)
                print("=================================")
                print("Expense"," Amount")
                print("-------" , "-------")
                for x,y in expense_track.items():
                    print(x,"     ",y)
                    bal=bal+y
                print("----------------")
                print("balance=",budget-bal)
            '''else:
                print("expense not found")'''
        elif option==7:
            print(exit)
            break
    except:
        print("invalid")
    

        
            
                
                    