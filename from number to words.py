x= {0:"",1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

z = {0:'',2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy',8: 'Eighty',9: 'Ninety'}

#enter a number from 1 to 9999
n=int(input("enter a number: "))
#make a variable that converts the int to str
numb=str(n)
#o is a var that contains the length of numb
o=len(numb)
#printing the numbers form 1 to 19
if (n >= 1) and (n <= 19):
    b=int(numb)
    print(x[b])
#printing numbers that have 2 digit and more than 19
elif o==2 and (n>19):
    num=int(numb[0])
    num2=int(numb[1])
    print(z[num]+" "+x[num2])
#print number that have 3 digits
elif o==3:
    num=int(numb[0])
    num2=int(numb[1])
    num3=int(numb[2])
    if num2==1 and num3 <=9:
        num0=str(num2)+""+str(num3)
        numv=int(num0)
        print(x[num] + " hundred and " + x[numv])
    elif num2 == 0 and num3==0:
        print(x[num]+" hundred")
    elif num2==0:
        print(x[num]+" hundred and "+x[num3])
    else:
        print(x[num]+" hundred and "+z[num2]+" "+x[num3])
#printing the numbers that have 4 digits
elif o==4:
    num=int(numb[0])
    num2=int(numb[1])
    num3=int(numb[2])
    num4=int(numb[3])
    if num3 == 1 and num4 <= 9:
        num0 = str(num3) + "" + str(num4)
        numv = int(num0)
        print(x[num] + " thousend and " + x[numv])
    elif num2 == 0 and num3==0 and num4==0:
        print(x[num] + " thousend")
    elif num2==0 and num3==0:
        print(x[num]+" thousand and "+x[num4])
    elif num2==0:
        print(x[num]+" thousend and "+z[num3]+" "+x[num4])
    elif num4==0 and num3==0:
        print(x[num] + " thousend and " + x[num2] + " hunderd")
    else:
        print(x[num]+" thousend and "+x[num2]+" hunderd and "+z[num3]+" "+x[num4])
else:
    print("Number Out Of Range")
