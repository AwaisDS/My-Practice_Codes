add=lambda x , y: x + y

#print(add(4 , 9))

x=[1,2,3,4,5,6,7]

sq=list(map(lambda x : x ** 2 , x))
#print(sq)

check_even= list(filter(lambda x : x % 2 == 0 , x))
print(check_even)

f={x: (lambda x : x*x)(x) for x in range(5)}
print(f)