tc = int(input())
for t in range(tc):
    n, k = map(int, input().split())
    
    s = input()
    not_equal = 0 
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            not_equal += 1

    print(f'Case #{t+1}: {abs(k-not_equal)}')
