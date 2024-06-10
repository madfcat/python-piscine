from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()

print("More tests")
for elem in ft_tqdm(range(2,10,1)):
    sleep(0.705)
print()
for elem in tqdm(range(2,10,1)):
    sleep(0.705)
print()
print()

for elem in ft_tqdm(range(3,71,3)):
    sleep(0.505)
print()
for elem in tqdm(range(3,71,3)):
    sleep(0.505)
print()