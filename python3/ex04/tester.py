from ft_calculator import calculator

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calculator.sous_vec(a, b)

# More tests
print()
print("More tests:")
v1 = [1.23, 2.34, 3.45]
v2 = [4.56, 5.67, 6.78]

calculator.dotproduct(v1, v2)
calculator.add_vec(v1, v2)
calculator.sous_vec(v1, v2)
