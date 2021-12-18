"""Input: a string of comma separated numbers. The numbers 5 and 8 are present in the listAssume that 8 always comes after 5.

Case 1: num1 = add all numbers which do not lie between 5 and 8 in the input.
Case 2: num2= numbers formed by concatenating all numbers from 5 to 8.
Output: sum of num1 and num2

Example: 1) 3,2,6,5,1,4,8,9
Num1 : 3+2+6+9 =20
Num2: 5148
output: 5248+20 = 5168 """

=======================================================================================================================================================================

n=input()
n=n.replace(",","")
a=(n.index("5"))
b=(n.index("8"))
n1=int(n[a:b+1])
n=n.replace(n[a:b+1],"")
i=0
s=0
while(i<len(n)):
    s=s+int(n[i])
    i+=1
print(n1+s)
