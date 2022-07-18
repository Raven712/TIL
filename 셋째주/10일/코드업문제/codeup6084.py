h, b, c, s = map(int,input().split())
#h = 1초에 몇번
#b = 2^b 비트사용
#c = 저장할 트랙개수채널 , 모노1 스테레오2
#s = 녹음할 시간
byte = b*8
KB = byte*1024
MB = KB*1024
print(round(h*b*c*s/8/1024/1024,1), 'MB')