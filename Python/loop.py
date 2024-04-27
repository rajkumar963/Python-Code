# a=[[0,0,1,1,1],[0,0,0,0,1],[0,1,1,1,1],[1,1,1,1,1],[0,0,1,1,1]]
# count=0
# max_row=[0,0,0,0,0]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i][j]==1:
#             count+=1
#         max_row[i]=count
#         count=0
#     max1=max(max_row)
#     ans=max_row.index(max1)
#     print(ans)






# m = [[0,0,1,1,1],[0,0,0,0,1],[0,1,1,1,1],[0,1,0,0,1],[0,0,0,1,1]]

# count =0
# max_row=[0,0,0,0,0]
# for i in range(len(m)):
#     for j in range(len(m)):
#         if(m[i][j]==1):
#             count+=1
#     max_row[i]=count
#     count=0

# maxx=max(max_row)
# ans=max_row.index(maxx)
# print(ans)

# i,j=(0,0)
# m = [[0,0,1,1,1],[0,0,0,0,1],[0,1,1,1,1],[0,1,0,0,1],[0,0,0,1,1]]
# for j in range(len(m)):
#     for i in range(len(m)):
#         print(m[i][j],end=" ")
#         i+=1
#     print("\n")
#     j+=1      


# i=0,
# j=4
# row=0
# m = [[0,0,1,1,1],[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]
# #while(i<len(m)):
# while(j<row and j>=0):
#      while(m[i][j]==1):
#             print(m[i][j],end=" ")
#             j-=1
#             row=i
#      i+=1   
# print("\n")
           



