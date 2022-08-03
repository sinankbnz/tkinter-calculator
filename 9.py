from ossaudiodev import SNDCTL_DSP_GETODELAY


n=int(input("Enter a number :"))
r=int(input("Enter range :"))
a=1
for a in range(1,r+1,1):
    mul=a*n
    print(a,"*",n,"=",mul)
