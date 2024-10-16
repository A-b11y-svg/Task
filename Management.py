print("Software is the solution")


print("**********")
print("**********")
print("**********")
print("**********")
choice = int(input("Enter Your Choice :"))

if choice == 1:
    print("Welcome to Registration Site")

    with open("rgstr.txt", "w") as file:

        first=file.write(input("Enter Your Name : " + "\n"))
        second=file.write(input("Enter Your Surname :" + "\n"))
        last=file.write(input("Enter Your Last Name :" + "\n"))
        apply=file.write(input("Enter JOb You Want Apply :" + "\n"))
        quali=file.write(input("What Is Your Qualification :" +"\n"))
        year=file.write(input("How many years of Experience do you have :" + "\n"))
    print("Your Applictaion is sent !")


elif choice == 2:

 print("Welvome to Search Site")

 with open("rgstr.txt", "r") as file:
   for line in file:
      print(line,end="") 

elif choice == 3:
   print("Welcome to edit site ")

   with open("rgstr.txt" ,"r") as file:
       content = file.read()

   content = content.replace('orange', 'mango').replace('pineapple', '2').replace('yes', '8')

   with open("rgstr.txt", "w") as file :
       file.write(content)


    
