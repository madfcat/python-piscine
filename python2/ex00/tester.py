from load_csv import load


print(load("life_expectancy_years.csv"))

# More tests

print()
print()
print("More tests:")
print(load(""))
print(load(2))
print(load("hey.csv"))
print(load("life_expectancy_years_txt.txt"))
