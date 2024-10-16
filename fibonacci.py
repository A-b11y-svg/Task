print("Software is the solution")

print("**********")
print("**********")
print("**********")
print("**********")

choice = int(input("Enter Your Choice: "))

if choice == 1:
    print("Welcome to Registration Site")

    with open("rgstr.txt", "w") as file:
        first = file.write(input("Enter Your Name: ") + "\n")  # Add newlines
        second = file.write(input("Enter Your Surname: ") + "\n")
        last = file.write(input("Enter Your Last Name: ") + "\n")
        apply = file.write(input("Enter Job You Want to Apply for: ") + "\n")
        quali = file.write(input("What Is Your Qualification: ") + "\n")
        year = file.write(input("How many years of Experience do you have: ") + "\n")
        
    print("Your Application is sent!")

elif choice == 2:
    print("Welcome to Search Site")

    with open("rgstr.txt", "r") as file:
        for line in file:
            print(line, end='')  # Properly handle newlines

elif choice == 3:
    print("Welcome to Edit Site")
    
    with open("rgstr.txt", "r") as file:
        content = file.read()  # Read the content of the file
    
    # Perform multiple replacements
    content = content.replace('orange', 'mango').replace('pineapple', '2').replace('yes', '8')
    
    # Write the updated content back to the file
    with open("rgstr.txt", "w") as file:
        file.write(content)

else:
    print("Invalid choice. Please try again.")
