#https://www.acmicpc.net/problem/1021

n,m = map(int,input().split())

l = list(map(int,input().split()))

deck = [i for i in range(1,n+1)]
cnt = 0
for i in l:
    flag =1
    while(flag):
        if(i == deck[0]):
            del deck[0]
            flag =0
        else:
            if( deck.index(i) < len(deck)/2):
                tmp = deck[0]
                del deck[0]
                deck.append(tmp)
                cnt+=1
            else:
                tmp = deck[-1]
                deck.insert(0,tmp)
                del deck[-1]
                cnt+=1
print(cnt)