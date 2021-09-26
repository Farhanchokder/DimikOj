t = int(input())
while(t != 0):
    n = int(input())
    last_digit = n % 10
    while (n != 0):
        r = n % 10
        #print("r = ",r)
        n = n // 10
        #print("n = ",n)
	
    print("Sum =",last_digit+r)  #ei laine  r = first digit
    t -= 1
