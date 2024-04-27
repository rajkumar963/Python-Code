#Reverse a string
# s="abcdefghijklmnopqrstuvwxyz"
# s=s[::-1]
# print(s)

#check polindrome or not
# a="madam"
# if(a==a[::-1]):
#     print("palindrome") 
# else:
#     print("not a palindrome")

#left side rotation by 2
# a="abcde"
# b=a[2:]+a[0:2]
# print(b)

#sum of elements in list
# list=list(map(int,input().split()))
# input=sum(list)     
# print(input)

#sum of odd indexed elements and sum of even indexed elements
# list=list(map(int,input().split()))
# sum=0
# for i in range(0,len(list)):
#     if(i%2==0):
#         sum=sum-list[i]
#     else:
#         sum=sum+list[i]
# print(sum)

#Print a right triangle with asterisks
# for i in range(1,10):
#     print("*"*i)

#Print a square with asterisks
# n=int(input("enter the number:"))
# for i in range(0,n):
#     print("*"*n)


#Print a hollow rectangle with asterisks
# n=int(input("enter the number:"))
# for i in range(0,n):

#Print a circle with asterisks
# def printCircle(r):
#     for i in range(r):
#         print("*"*r)    
# printCircle(10)   
    
#squre of list
# l=[1,2,3,4,5]
# sql=list(map(lambda x:x**2,l ))
# print(sql)

# matrix=[[0 for i in range(5)] for j in range(5)]
# print(matrix)


# name=["apple","banana","cherry"]
# price=[10,20,30]
# l=[[name[i],price[i]] for i in range(len(name))]
# print(l)

#Calculate sum of each row in 2D array
# a=[1,2,3,4,5]
# b=[6,7,8,9,10]
# l=list(map(lambda x,y:x+y,a,b))
# print(l)

#intersection of two list
# a=[1,2,3,4,5]
# b=[1,7,8,9,10]
# l=list(set(a+b))
# print(l)

#union of two list
# a=[1,2,3,4,5]
# b=[1,7,8,9,10]
# l=list(sorted(a+b))
# print(l)


#sum of two Matrix
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[[8,9,10],[11,12,13],[14,15,16]]
# l=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         l[i][j]=a[i][j]+b[i][j]

# print(l)

#Transpose of matrix
# a=[[1,2,3],[4,5,6],[7,8,9]]
# l=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         l[i][j]=a[j][i]

# print(l)

#multiplication of two matrix
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[[8,9,10],[11,12,13],[14,15,16]]
# l=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         l[i][j]=a[i][j]*b[i][j]

# print(l)

#Write a function to write multiplication table
# n=int(input("enter the number:"))
# def write_multiplication_table(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)

# write_multiplication_table(n)

#Print first N terms of a GP with given first term, N and common ration
# n=int(input("enter the number:"))
# r=int(input("enter the common ratio:"))
# def print_GP(n,r):
#     for i in range(1,n+1):
#         print(r*i)
# print_GP(n,r)


#Given a number, calculate it's nearest power of two
n=int(input("enter the number:"))
def nearest_power_of_two(n):
    count=0
    while(n!=0):
        n=n/2
        count+=1    
    return 2**count

print(nearest_power_of_two(n))






