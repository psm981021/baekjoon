ans=0

def backtrack(cur,visited,S,cnt):
    global ans

    if(len(cur)==len(S)):
        ans+=1
        return

    for i in range(26):
        if(visited[i]>0 and cur[cnt-1]!= chr(97+i)):
            ncur=cur+chr(97+i)
            visited[i]-=1
            backtrack(ncur,visited,S,cnt+1)
            visited[i]+=1

S=input()
visited=[0 for i in range(26)]

for i in range(len(S)):
    visited[ord(S[i])-97]+=1
cur=""
for i in range(26):
    if(visited[i]>0):
        ncur=cur+chr(97+i)
        visited[i]-=1
        backtrack(ncur,visited,S,1)
        visited[i]+=1

print(ans)