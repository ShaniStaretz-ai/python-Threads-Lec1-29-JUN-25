import random
import time
from concurrent.futures import ThreadPoolExecutor


def print_sequence(name, count):
    for i in range(count):
        print(f"Thread {name}: i={i}\n")
        time.sleep(0.3)


if __name__ == '__main__':
    # thread1 = threading.Thread(target=print_sequence, args=("Alpha", 5))
    # thread2 = threading.Thread (target=print_sequence, args=("Beta", 3))
    # thread3 = threading.Thread(target=print_sequence, args=("Gamma", 4))
    # thread1.join()
    # thread2.join()
    # thread3.join()

    with ThreadPoolExecutor(max_workers=2) as executor:
        data = [("Alpha", 5), ("Beta", 3), ("Gamma", 4)]
        tasks = [executor.submit(print_sequence, name, count) for name, count in data]
        for task in tasks:
            task.result()
    print("All threads completed!")
    print("***Bonus – Dynamic Version***")
    names = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Theta", "Sigma", "Omega", "Kappa"]
    random.shuffle(names)
    task_count = random.randint(5, 10)
    data = [(names[i], random.randint(2, 6)) for i in range(task_count)]
    with ThreadPoolExecutor(max_workers=2) as executor2:
        tasks = [executor2.submit(print_sequence, name, count) for name, count in data]
        for task in tasks:
            task.result()
    print("All threads completed!")