from time import sleep
from tqdm import tqdm # type: ignore
from Loading import ft_tqdm

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
for elem in tqdm(range(333)):
    sleep(0.005)
print()

#print(tqdm.__doc__)
#print(ft_tqdm.__doc__)
