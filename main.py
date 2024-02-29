import numpy as np
from timeit import default_timer as timer
from hybrid import hybrid_sort
import matplotlib.pyplot as plt
import random
from collections import Counter
from progress.bar import Bar
def main():
    # task_one()
    n = 100
    task_two(n)
    min_k_arr = [None] * 1000
    bar = Bar('Processing', max = 1000)
    for i in range(1000):
        min_k = task_two(n)
        min_k_arr[i] = min_k
        bar.next()
    bar.finish()
    counter = Counter(min_k_arr)
    top_three_most_common = counter.most_common(3)
    print("N = ", n)
    print("Most common: ", top_three_most_common[0])
    print("Second most common: ", top_three_most_common[1])
    print("Third most common: ", top_three_most_common[2])

def task_one(n, k_max):
    loop = 10
    avg_time = []
    for i in range(1, k_max + 1, 1):
        avg_time.append(average_time(loop, i, n))
    return avg_time

def task_two(n):
    k_max = n
    if(k_max > 100):
        k_max = 100
    k_values = range(1, k_max + 1) # Fill with your K values
    avg_times = task_one(n, k_max) # Fill with your average times

    # plt.plot(k_values, avg_times)
    # plt.title("HybridSort Performance")
    # plt.xlabel("K Value")
    # plt.ylabel("Average Time (s)")
    # plt.grid(True)
    # plt.show()
    sorted_avg_times = sorted(avg_times)
    min_val = sorted_avg_times[0]
    min_index = avg_times.index(min_val)
    return min_index + 1

def average_time(loop, k, n):
    result = 0
    for i in range(loop): 
        rand = list(range(n))
        random.shuffle(rand)
        start = timer()
        hybrid_sort(rand, k)
        end = timer()
        result += end - start
    return result/loop

if __name__=="__main__": 
    main()