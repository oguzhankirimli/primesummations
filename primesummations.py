def prime_numbers_up_to(n):
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [x for x in range(2, n + 1) if sieve[x]]

def count_prime_sum_ways(limit):
    primes = prime_numbers_up_to(limit) 
    ways = [0] * (limit + 1)  
    ways[0] = 1  

    
    for prime in primes:
        for i in range(prime, limit + 1):
            ways[i] += ways[i - prime]  

    return ways

def find_first_value_with_over_n_ways(n):
    limit = 10  
    while True:
        ways = count_prime_sum_ways(limit)  
        for i in range(limit):
            if ways[i] > n:  
                return i
        limit *= 2  


result = find_first_value_with_over_n_ways(5000)
print("5000'den fazla farklı yolla asal sayıların toplamı olarak yazılabilen ilk sayı:",(result))
