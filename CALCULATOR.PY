NAME=input("PLEASE ENTER YOUR NAME ")
print(f"HELLO {NAME.upper()} NICE TO MEET YOU. THIS IS A BASIC CALCULATOR MADE BY ARJUN")

Num1=float(input("ENTER FIRST NUMBER: "))
Num2=float(input("ENTER SECOND NUMBER: "))
OPERATOR=int(input('''ENTER \n1 FOR ADDITION \n2 FOR SUBTRACTION \n3 FOR MULTIPLICATION \n4 FOR DIVISION \n5 FOR FLOOR DIVISION \n6 FOR REMAINDER
7 FOR RAISE TO POWER \n8 FOR SQUARE \n9 FOR CUBE \n10 FOR SQUARE ROOT \n11 FOR CUBE ROOT\n'''))

if(OPERATOR==1):
    print("Addition Of Numbers",Num1+Num2)    
elif(OPERATOR==2):
    print("Subtraction Of Numbers",Num1-Num2)    
elif(OPERATOR==3):
    print("Multiplication Of Numbers",Num1*Num2)    
elif(OPERATOR==4):
    print("Division  Of Numbers",Num1/Num2)    
elif(OPERATOR==5):
    print("Flooor Division Of Numbers",Num1//Num2)    
elif(OPERATOR==6):
    print("Remainder Of Numbers",Num1%Num2)    
elif(OPERATOR==7):
    print("Raise To Power",Num1**Num2)    
elif(OPERATOR==8):
    print("Sqaure Of Number",Num1*2)    
elif(OPERATOR==9):
    print("Cube Of Number",Num1*3)    
elif(OPERATOR==10):
    print("Square Root Of Number",Num1*0.5)    
elif(OPERATOR==11):
    print("Cube Root Of Number",Num1**0.33)   
else:
    print("invalid operator")