# -*- coding: utf-8 -*-

n=int(input())
ans=2
for i in range(n):
    s=input()
    ans+=1
    if s[-4:]=="+one":
        ans+=1
if ans==13:
    ans+=1
print(ans*100)
