num = int(input("write a number to check:"))
def is_prime(number):
    
    list=[]
    for any in range(2, number):
        if number % any == 0:
            list.append(0)
        else:
            list.append(number)
    if 0 in list:
        print("not prime")
    else:
        print("prime number")

if num == 0 or num ==1:
    print("Not Prime")
else:
    is_prime(num)
