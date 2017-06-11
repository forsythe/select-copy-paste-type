import time

def f(n):
    c = ([0, 1, 2, 3, 4] + [0]*(n+1-5))
    d = [0]*(n+1)   #tracks which case we choose
        
    for k in range(1,n+1):
        x = c[k-1]+1
        case = -1
        for i in range(2, 6):
            if i*c[max(k-i-1, 0)] >= x:
                x = i*c[max(k-i-1, 0)]
                case = i
        
        c[k] = x
        d[k] = case

    #return c[n]
    print("n = " + str(n) + ", max chars: " + str(c[n]))
    k = n

    while k > 0:
        if d[k] == -1:
            print(str(k) +". Type 1 character")
            k-=1
        else:
            case = d[k]
            for _ in range(case-1):
                print(str(k) +". Paste selection")
                k-=1
            print(str(k) +". Copy selection")
            k-=1
            print(str(k) +". Select all")
            k-=1

def time():
    for _ in range(0, 1000000, 10000):
        t0 = time.time()
        f(_)
        t1 = time.time()
        print(str(_) + ", " + str(round(t1-t0, 3)))
