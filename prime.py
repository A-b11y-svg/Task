#def prime():

attempt = 0
max_Attempts = 5


while attempt < max_Attempts :
 num=int(input("Enter a Number :"))
 if num%2 == 0:
  print(f"Yes {num} is an even number ")
  
 else:
        print(f"{num} Is not an even number !")
 attempt += 1  # Increment the attempt count

print(f"Attempts remaining: {max_Attempts - attempt}")

if attempt == max_Attempts:
   print("You're out of time !")