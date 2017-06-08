def prime_numbers(limit):
    primes = []
    tested = [1]
    
    for num in range(1, limit+1):

        factors = []

        ##print(tested)
        #print(len(tested))

        for i in range(len(tested)):
            #print('num is {}'.format(num))
            #print('tested is {}'.format(tested[i]))
            #print(num % tested[i])
            if num % tested[i] == 0:
                factors.append(tested[i])
                
        factors.append(num)
        set_factors = set(factors)
        tested.append(num)

        if len(set_factors) == 2:
            primes.append(num)

    return primes
            
print(prime_numbers(30))
