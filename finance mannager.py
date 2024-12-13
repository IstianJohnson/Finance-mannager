# A persional finance mannager 
users = {} 
# Username and Password checking
def register(username, Password):
   if username in users:
      return False
   else:
      users[username] = Password
      return True

def authenticate(username, Password):
   if username in users and users[username] == Password:
      return True
   else:
      return False

# Choice making by user

value = 'y'

while(value == 'y' or value == 'Y'):
   print("Welcome To Your Finance Mannager")
   print("To login to Your Account Press 1 \nTo Creat a new Account Press 2")
   choice = int(input("Enter Your Choice : "))

   if choice == 1:
      username = input("Enter The Username : ")
      Password = input("Enter Your Password : ")
      if authenticate(username, Password):
         v = 'Y'
         while(v == 'y' or v == 'Y'):
            print("\nWelcome Back", username, )
            print("To check Income Record Press 1")
            print("To  Check Your Expences Press 2")
            print("To Set Your Budgeting Press 3")
            print("To logout Press 4")
            cho = int(input("Enter Your Choice : "))
            bfood = 0
            btransport = 0
            bentertainment = 0
            bother = 0
            food = 0
            transportation = 0
            Entertainment = 0
            other = 0
            freelance = 0
            salary = 0
            investment = 0
#Income Record Of User
            if cho == 1:
               loop = 'Y'
               while (loop == 'y' or loop == 'Y'):
                  
                  print("\nYour Freelance Amount :", freelance, "\nYour Salary Left : ", salary, "\nYour Total Investment : ", investment)
                  print("To Add Money In Freelance press 1 ", "\nTo Add Money In Salary press 2 ", "\nTo Add Money In Investment press 3")
                  print("To Remove Money from Freelance press 4 ", "\nTo Remove Money From Salary press 5 ", "\nTo Remove Money from Investment press 6")
                  print("To Go Back Press 7")
                  decision = int(input("Enter Your Choice : "))
                  

#Add or Remove Money From Income 
                  if decision == 1:
                     amount = int(input("Enter The Money : "))
                     freelance += amount
                     loop = 'y'
                  elif  decision == 2:
                     amount = int(input("Enter The Money : "))
                     salary +=  amount
                     loop = 'y'
                  elif decision == 3:
                     amount = int(input("Enter The Money : "))
                     investment +=  amount
                     loop = 'y'
                  elif decision == 4:
                     amount = int(input("Enter The Money : "))
                     freelance -= amount
                     loop = 'y' 
                  elif decision == 5:
                     amount = int(input("Enter The Money : "))
                     salary -= amount
                     loop = 'y'
                  elif decision == 6:
                     amount = int(input("Enter The Money : "))
                     investment -= amount
                     loop = 'y'
                  elif decision == 7:
                     break
                  else:
                     print ("Wrong choice")
                     loop = 'y'
            elif cho == 2:
               loop2 = 'Y'
               while(loop2 == 'Y' or loop == 'y'):
                  print("\nThe Remaning Budget For Your Food Is :",  bfood)
                  print("The Remaining Budget For Your Transportation Is :",  btransport)
                  print("The Remaining Budget For Your Entertainment Is : ",  bentertainment)
                  print("The Remaining Budget For Other Expences Is : ",  bother)
                  
                  print("\nTo Add Money To Your Budget Press 1")
                  print("To Remove Money From Your Budget Press 2")

                  cho2 = int(input("Enter Your Choice : "))

                  if cho2 == 1:
                     print("\nTo Add Money to Food's Budget Enter 1 \nTo Add Money to Transportation's Budget Enter 2 \nTo Add Money to Entertainment's Budget Enter 3 \nTo Add Money to Miscellaneous Expences's Budget Enter 4 ")
                     print("To Go Back Press 5")
                     cho1 = int(input("Enter Your Choice : "))
         
                  #adding Money To The Budget
                     
                     if cho1 == 1:
                           amount1 = int(input("Enter The Amount : "))
                           amount1 += food
                           loop2 = 'Y'
                     elif cho1 == 2:
                           amount1 = int(input("Enter The Amount : "))
                           amount1 += transportation
                           loop2 = 'Y'
                     elif cho1 == 3:
                           amount1 = int(input("Enter The Amount : "))
                           amount1 += Entertainment
                           loop2 = 'Y'
                     elif cho1 == 4:
                           amount1 = int(input("Enter The Amount : "))
                           amount1 += other
                           loop2 = 'Y'
                     elif cho1 == 5:
                        break
                     else :
                           print("Wrong Choice")
                           loop2 = 'Y'
                  elif cho2 == 2:
                     loop3 = 'Y'
                     while(loop3 == 'y' or loop3 == 'Y' ):
                        print("\nTo Remove Money From Your Food's Budget Press 1 \nTo Remove Money From Your Transportation's Budget Press 2 \nTo Remove Money From Your Entertainment's Budget Press 3 \nTo Remove Money From Your Miscellaneous Expences's Budget Press 4")
                        print("To Go Back press 5")
                        des = int(input("Enter Your Choice : "))

                        if des == 1:
                           amount2 = int(input("Enter Your Amount : "))
                           food -= amount2
                           loop3 = 'y'
                        elif des == 2 :
                           amount2 = int(input("Enter Your Amount : "))
                           transportation -= amount2
                           loop3 = 'y'
                        elif des == 3:
                           amount2 = int(input("Enter Your Amount : "))
                           Entertainment -=  amount2
                           loop3 = 'y'
                        elif des == 4:
                           amount2 = int(input("Enter Your Amount : "))
                           other -=  amount2
                           loop3 = 'y'
                        elif des == 5:
                           break
                        else :
                           print("Wrong Choice")
                           loop3 = 'y'

#Budgeting Of The User 
            elif cho == 3:

               if food < bfood :
                  print("Alert: Your budget for food is over!")
                  print("The Remaining Budget :", food + bfood)
                  break
               if transportation < btransport:
                  print("Alert: Your budget for transportation is over!") 
                  print("The Remaining budget :", transportation + btransport)
                  break
               if bentertainment < Entertainment:
                  print("Alert: Your budget for Entertainment is over!") 
                  print("The Remaining budget :", Entertainment + bentertainment)
                  break
               if other < bother:
                  print("Alert: Your budget for other expences is over!")
                  print("The Reaming Budget :", other + bother)
                  break
               else:
                  print("The Remaning Budget For Your Food Is :", food - bfood)
                  print("The Remaining Budget For Your Transportation Is :", transportation - btransport)
                  print("The Remaining Budget For Your Entertainment Is : ", Entertainment - bentertainment)
                  print("The Remaining Budget For Other Expences Is : ", other - bother)
                  break
              
               
            elif cho == 4:

               value = input("Are You Sure You, Want To Logout (y/n) : ")


      else :
         print("Authentication Failed Please Check Back")
         value = input("Do you want to continue (y/n) : ")

   elif choice == 2:
      username = input("Enter Your Username : ")
      Password = input("Enter Your password ")
      if register(username, Password):
         print("Username and Password Registerd Successfully")
         value = input("Do you want to continue (y/n) : ")
      else:
         print("Print Username Already Exist")
         value = input("Do you want to continue (y/n) : ")


   else:
      print("Wrong Choice Please Check Back")
      value = 'Y'
