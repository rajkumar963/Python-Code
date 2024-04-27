#Given a number, calculate it's nearest power of two









#Given a number, calculate sum of its digits
# n=int(input("enter the number:"))
# def sum_of_digits(n):
#     sum=0
#     for i in range(n+1):
#         sum=sum+i
#     return sum

# print(sum_of_digits(n))


#Given a number, convert it into binary
n=int(input("enter the number:"))
def binary(n):
    b=0
    for i in range(n+1):
        b=b+(2**i)
    return b

print(binary(n))
