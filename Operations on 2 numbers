import sys
def main():
    a=int(input("Enter a : "))
    b=int(input("\nEnter b : "))
    ch=int(input("\nEnter the operation to be performed\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Exit : "))
    while(ch):
        if(ch==1):
            result=a+b;
            print("\n",a," + ",b," = ",result)
        elif(ch==2):
            result=a-b;
            print("\n",a," - ",b," = ",result)
        elif(ch==3):
            try:
                result=a/b;
                print("\n",a," / ",b," = ",result)
            except ZeroDivisionError:
                print("\nDivision by zero error")
        elif(ch==4):
            result=a*b;
            print("\n",a," * ",b," = ",result)
        elif(ch==5):
            sys.exit()
        else:
            print("Invalid choice!!")
        ch=int(input("\nEnter the operation to be performed\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Exit : \n"))
main()
