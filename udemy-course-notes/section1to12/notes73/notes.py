from multiprocessing import Process
import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

# 📍 SIR'S CODE : demonstrating that threading doesn't work here

# thread1 = threading.Thread(target=brew_chai, name="Barista-1")
# thread2 = threading.Thread(target=brew_chai, name="Barista-2")

# start = time.time()

# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# end = time.time()

# print(f"total time taken: {end - start:.2f} seconds")

# 📍 MY CODE : trynig out multi-processing

if __name__ == "__main__":

    process1 = Process(target=brew_chai, name='Barista-1')
    process2 = Process(target=brew_chai, name='Barista-2')

    start = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.time()

    print(f"total time taken: {end - start:.2f} seconds")