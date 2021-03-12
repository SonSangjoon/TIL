import string

S = input()
ans = [-1] * 26

#alphabet
# [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
alphabet = list(string.ascii_lowercase)

for i in range(len(S)):
    t = S[i]
    p = alphabet.index(t)

    if ans[p] == -1:
        ans[p] = i

for i in ans:
    print(i, end=" ")


ord(string) 