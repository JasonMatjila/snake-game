num_terms = int(input("Enter the number of terms to generate: "))

# initialize the first two terms of the sequence
a = 0
b = 1

# print the first two terms
print(a, end=' ')
print(b, end=' ')

# generate the rest of the sequence
for i in range(2, num_terms):
    c = a + b
    print(c, end=' ')
    a = b
    b = c
