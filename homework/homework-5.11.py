num=int(input("Please enter num "))
if num > 0 and num < 10:
    if num == 1:
        print("one")
    if num == 2:
        print("two")
    if num == 3:
        print("three")
    if num == 4:
        print("four")
    if num == 5:
        print("five")
    if num == 6:
        print("six")
    if num == 7:
        print("seven")
    if num == 8:
        print("eight")
    if num == 9:
        print("nine")
elif num > 9 and num < 100:
    sum=int((num/10)+(num%10))
    print(num,"is 2 digit number,sum is",sum)
elif num > 99 and num < 1000:
    ahadot=int(num % 10)
    asarot=int(num / 10 % 10) 
    meot=int(num / 100 % 10) 
    sum=int(meot*asarot*ahadot)
    print(num,"is 3 digit number,mul is",sum)
else:
    print(num,"number has more than 3 digits..")
