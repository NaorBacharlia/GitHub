def check_id(id,lengh):
    if lengh > 9:
        return 0
    for x in id:
        if ord(x) < 48 or ord(x) > 57:
            return 0
    return 1
def fill_zero(id,lengh):
    num=9-lengh
    zero_complate=num*"0"
    id=zero_complate+id
    return id
def test_id(id):
    add_arr=[1,2,1,2,1,2,1,2,1]
    new_arr=[0,0,0,0,0,0,0,0,0]
    for x in range(0,len(add_arr)):
        new_arr[x]=add_arr[x]*int(id[x])
    sum=0
    for x in range(0,len(new_arr)):
        if new_arr[x] > 9:
            ahadot=new_arr[x] % 10
            asarot=int(new_arr[x] / 10)
            new_arr[x]=ahadot+asarot
        sum+=new_arr[x] 
    if sum % 10 ==0:
        return 1
    else:
        return 0       
str_id=input("Please enter your ID number...\n")
lengh=len(str_id)
while not check_id(str_id,lengh):
    str_id=input("Your ID number is wrong enter again...\n")
    lengh=len(str_id)
if lengh < 9:
   str_id=fill_zero(str_id,lengh)
if test_id(str_id)==1:
    print("After the check your ID number is GOOD!!!\n")
else:
    print("After the check your ID number is NOT good!!!\n")








        
