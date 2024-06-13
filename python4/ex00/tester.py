from statistics import ft_statistics
# from statistics import median, quantiles

ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")

# Mores tests:
# print()
# print("Mores tests:")
# nums = [1, 42, 360, 11, 64]
# x = quantiles(nums, n=4)[0]
# y = quantiles(nums, n=4)[2]
# print("Quartile from numpy:", x, y)
# print("-----")



# nums = [1, 42, 360, 11]
# ft_statistics(1, 42, 360, 11, toto="mean", tutu="median", tata="quartile")
# print("From standard median: ", median(nums))
# x = quantiles(nums, n=4)[0]
# y = quantiles(nums, n=4)[2]
# print("Quartile from numpy:", x, y)
# print("-----")

# nums = [1]
# ft_statistics(1, toto="mean", tutu="median", tata="quartile")
# # x = quantiles(nums, n=4)[0]
# # y = quantiles(nums, n=4)[2]
# # print("Quartile from numpy:", x, y)
# print("-----")

# nums = [1, 42]
# ft_statistics(1, 42, toto="mean", tutu="median", tata="quartile")
# x = quantiles(nums, n=4)[0]
# y = quantiles(nums, n=4)[2]
# print("Quartile from numpy:", x, y)
# print("-----")

# nums = [1, 42, 360]
# ft_statistics(1, 42, 360, toto="mean", tutu="median", tata="quartile")
# x = quantiles(nums, n=4)[0]
# y = quantiles(nums, n=4)[2]
# print("Quartile from numpy:", x, y)
# print("-----")