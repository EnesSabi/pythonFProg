text = list("Ugpco ypvi xb zdbeatii ktglpwgadhitc Ipmx fjtg sjgrw Qpntgc.")
lösung = list("Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.")
# a bis z -> 97 - 122
# A bis Z -> 65 - 90
# &nbsp; -> 32
def caesar_encode(src, dist): #a bis z && A bis Z
    out = []
    for x in src:
        if((ord(x) < 123 or ord(x) > 96) and ord(x) > 90 and not (ord(x) == 32)): # for kleinbuchstaben
            a = ord(x) + dist
            if(a > 122):
                a -= 26
            if(a < 97):
                a += 26
        if((ord(x) < 91 or ord(x) > 64) and ord(x) < 97 and not(ord(x) == 32)): # for grossbuchstaben
            a = ord(x) + dist
            if(a > 90):
                a -= 26
            if(a < 65):
                a += 26
        if(ord(x) == 32 or ord(x) == 46):
            a = ord(x)
        out.append(chr(a))
    return out
    
def caesar_decode(src, dist):
    out = []
    for x in src:
        if((ord(x) < 123 or ord(x) > 96) and ord(x) > 90 and not(ord(x) == 32)): # for kleinbuchstaben
            a = ord(x) - dist
            if(a > 122):
                a -= 26
            if(a < 97):
                a += 26
        if((ord(x) < 91 or ord(x) > 64) and ord(x) < 97 and not(ord(x) == 32)): # for grossbuchstaben
            a = ord(x) - dist
            if(a > 90):
                a -= 26
            if(a < 65):
                a += 26
        if(ord(x) == 32 or ord(x) == 46):
            a = ord(x)
        out.append(chr(a))
    return out

def main():
    y = caesar_decode(text, 15)
    print("---------- 15. Sentence ----------")
    print(''.join(y))

if __name__ == "__main__":
    main()

