import random
import threading
import time


def print_random_numbers(thread_name, end):
    for i in range(1,end+1):
        print(f"{thread_name}-{i}")
        time.sleep(0.5)

threads=[]
random_thread_num=random.randint(5,10)
print(f"selected {random_thread_num} number of threads:")
for i in range(random_thread_num):
    end=random.randint(5,10)
    print("selected end number:",end)
    t_name=f"Thread-{i+1}"
    t=threading.Thread(target=print_random_numbers, args=(t_name,end))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"All {random_thread_num} threads completed.")