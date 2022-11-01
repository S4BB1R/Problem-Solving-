# https://www.hackerrank.com/challenges/handshake/problem?isFullScreen=true


number = int(input().strip())
for item in range(number):
    n=int(input())
    result=n*(n-1)/2
    print(int(result))