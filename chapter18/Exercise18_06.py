# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Implement a PriorityQueue) Change the implementation of Programming
Exercise 18.5 so that it uses a PriorityQueue instead of a Queue. For every
message generated, randomly decide whether to make it low or high priority.
Include this information in the message you queue. When processing messages, those
with high priority will be processed first. You could use a string to determine
priority, in which case "Low" would have lower priority than "High", as priority
would be determined alphabetically.'''

import queue
import random
import threading


def main():
    # create the worker thread
    threading.Thread(target=dequeuer, daemon=True).start()

    for i in range(50):
        priority = "High" if bool(random.randint(0, 1)) else "Low"
        message = f"Message {str(i)} ({priority} priority)"
        q.put([priority, message])
        print(f"Queued {message}\n")
    print("All messages queued\n")

    q.join()
    print("All work completed")


def dequeuer():
    while True:
        message = q.get()
        print(f"Processed {message[1]}\n")
        q.task_done()


q = queue.PriorityQueue()

main()
