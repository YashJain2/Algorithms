import sys                             # Analysis                                    #Time Complexity
def trav(s,i,j):
    if i==j:
        print("A"+str(i),end=" ")    # inorder traversal to print the pattern                  O(n)
    else:
        print("(",end=" ")      
        trav(s,i,s[i][j])
        trav(s,s[i][j]+1,j)
        print(")",end=" ")

def mcm(p):                             
    n=len(p)                                                                                     #c1
    m=[[0]*(n) for i in range (n)]   # initialising multiplication and splitting                 c2
    s=[[0]*(n) for i in range (n)]   # arrays                                                    c3
    for d in range (1,n-1):          # d is the no. of elements selected at a time 1,2..         n-2 times
        for i in range (1,n-d):      # starting matrix chosen till size that can be              n-d-1 times
#                                      used with the given d if d=2 then choose A1A2,A2A3,A3A4   
            j=i+d                    # last index with given array index                          c4
            mini=sys.maxsize                                                                      #c5
            for k in range (i,j):    # k is the place where splitting can occur                   j-i times
                inter=m[i][k]+m[k+1][j]  # calculating at place splitting cost is min              c6
                +(p[i-1]*p[k]*p[j])
#                 print(i,k,inter)
                if inter<mini:                                                                     #c7
                    mini=inter                                                                     # c8
                    s[i][j]=k       # and assigning that place to s[i][j]                          # c9
            m[i][j]=mini            # min cost assigned to m[i][j]                                 # c10
#     print(m,s)
    trav(s,1,n-1)                   # call to trav                                                 O(n)
    
# The total time complexity of Matrix Chain Multiplication Algorithm is :
# c1+c2+c2+((n-2)*(n-d-1))(c4+c5+((j-i)*(c6+c7+c8+c9+c10)))+O(n)
# Approximately equal to O(n^3)+O(n)~ O(n^3)




mcm([5,4,6,2,7])                 # c0
# Time complexity of program is : c0+O(n^3)~O(n^3)






