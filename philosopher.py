import threading
import time

NUM_PHILOSOPHERS = 5
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]


def philosopher(philosopher_id):
    left_fork = philosopher_id
    right_fork = (philosopher_id + 1) % NUM_PHILOSOPHERS

    if philosopher_id == NUM_PHILOSOPHERS - 1:
        left_fork, right_fork = right_fork, left_fork
    while True:
        print(f"philsofer {philosopher_id} is thinking.")
        time.sleep(1)

        print(f"philsofer {philosopher_id} is hungry.")

        with forks[left_fork]:
            print(f"philsofrt {philosopher_id} picked up fork {left_fork}")
            with forks[right_fork]:
                print(f"philsofer {philosopher_id} pickd up fork {right_fork}")
                time.sleep(2)
                print(f"philsofer {philosopher_id} is putting down fork {right_fork}")
            print(f"philsofer {philosopher_id} is putting down fork {left_fork}")



# ایجاد و شروع نخ‌ها
threads = []
for i in range(NUM_PHILOSOPHERS):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()

# جلوگیری از پایان یافتن برنامه
for t in threads:
    t.join()
