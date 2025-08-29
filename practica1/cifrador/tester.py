import math

def egcd(a,b):
    if b==0: return (a,1,0)
    g,x1,y1 = egcd(b,a%b)
    return (g,y1, x1-(a//b)*y1)

def modinv(a,m):
    a%=m
    g,x,_=egcd(a,m)
    if g!=1: raise ValueError
    return x%m

path = r".\file4.lol"
with open(path,"rb") as f:
    head = f.read(8)

target = b"%PDF-"
found = []
for k in range(1,256,2):  # solo impares
    try:
        inv = modinv(k,256)
    except ValueError:
        continue
    trial = bytes(((b*inv)&0xff) for b in head)
    if trial.startswith(target):
        found.append(k)

print("Llaves que producen '%PDF-':", found)
