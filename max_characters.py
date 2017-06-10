def print_if(s, b):
    if b:
        print(s)

def f(n):
    c = ([0, 1, 2, 3, 4] + [0]*(n+1-5))
    for _ in range(min(n, 4)):
        print("Type 1 character")
        
    for k in range(5, n+1):
        x = c[k-1]+1
        val_if_type = x
        case = -1
        y = x
        for i in range(2, 6):
            x = max(x, i*c[max(k-i-1, 0)])
            if x > y:
                y = x
                case = i
        for r in range(case):
            print_if("Select all", k==n)
            print_if("Copy selection", k==n)
            for _ in range(case-1):
                print_if("Paste", k==n)
        c[k] = x
        if val_if_type == x:
            print_if("Type 1 character", k==n)
    return c[n]
