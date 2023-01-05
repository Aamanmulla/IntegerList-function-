lst=[]

n=int(input("Enter the numbers in a list: "))
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele)
print("\nInput: ",lst)

def integer_list(lst):
    result1=lst.count(19)
    result2=lst.count(5)


    if result1==2 and result2>=3:
        print("\nOutput: \nTrue\n")
    else:
        print("\nOutput: \nFalse\n")

integer_list(lst)