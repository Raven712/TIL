S = input() 
# alp = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z] # 이렇게 푸는게 아닌거같다...
# alp2 = []
# for i in s:
#   if i in alp:
#     alp2.append()

# baekjoon


# index함수나 find 함수를 이용하는 문제다.
alp = 'abcdefghijklmnopqrstuvwxyz'
alp2 = [-1] * len(alp)
temp = -1

for i in S:   
  K = alp.find(i)   
  temp += 1
  if alp2[K] == -1:
    alp2[K] = temp


for i in alp2:
  print(i, end = ' ')




  
