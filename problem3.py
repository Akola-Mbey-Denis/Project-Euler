#  Largest prime factor
   
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
def prime_factors( num):
    i=2
 
    while i*i<num:
        while num%i==0:
            num=num//i
        i+=1 
     
    print(num)

if __name__=="__main__":
   prime_factors(600851475143)   
        
