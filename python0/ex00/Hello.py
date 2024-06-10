ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Updating list value
ft_list[1] = "World"

# Updating tuple value
ft_tuple_converted_to_list = list(ft_tuple)
ft_tuple_converted_to_list[1] = "Finland"
ft_tuple = tuple(ft_tuple_converted_to_list)

# Updating set value
ft_set.remove("tutu!")
ft_set.add("Helsinki")

# Updating dict value
ft_dict["Hello"] = "Hive"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
