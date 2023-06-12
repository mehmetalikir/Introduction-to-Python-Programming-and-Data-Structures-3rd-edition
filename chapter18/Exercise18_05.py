# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Implement a Queue) The following code listing contains skeleton code for a
multithreading program, where the main thread generate 50 messages and places
them in a Queue and another thread takes them from the Queue and prints them.'''
import threading
import queue
import random

def main():
    q = queue.Queue()  # Create a regular Queue instead of PriorityQueue

    # Create the worker thread
    threading.Thread(target=dequeuer, args=(q,), daemon=True).start()

    for i in range(50):
        priority = "High" if bool(random.randint(0, 1)) else "Low"
        message = f"Message {str(i)} ({priority} priority)"
        q.put([priority, message])
        print(f"Queued {message}\n")
    print("All messages queued\n")

    q.join()
    print("All work completed")

def dequeuer(q):
    while True:
        message = q.get()
        print(f"Processed {message[1]}\n")
        q.task_done()

main()
