'''*H
* AUTHOR :   Razie Hyria        START DATE :    MARCH 19th 2023
* FILENAME :        Disk Scheduling Algorithms 
* COURSE NAME:      CMPSC 472 Section 001: Operating Systems
* SEMESTER:         SPRING 2023
*
* DESCRIPTION :
*     A python program that implements the following disk-scheduling algorithms: FCFS SCAN C-SCAN
*
* FUNCTIONS USED:  abs, random, queue, max, sort
*
* REF: https://www.geeksforgeeks.org/disk-scheduling-algorithms/
*H'''

import sys
import random

CYLINDERS = 5000 # constant value representing cylinders
REQUESTS = 1000 # constant value representing requests

# FCFS scheduling
def fcfs(initial_position, requests):
    total_head_movement = 0
    current = initial_position # read the initial position of the disk head.
    for r in requests:
        total_head_movement += abs(r - current) # calculate the distance between the initial head position and the first request.
        current = r
    return total_head_movement # return the total distance traveled.


# SCAN scheduling
def scan(initial_position, requests):
    total_head_movement = 0
    current = initial_position
    queue = sorted(r for r in requests if r >= initial_position) # sort the sequence of requests in ascending order.
    for r in queue: # find the index of the request that is closest to the initial head position
        total_head_movement += abs(current - r) # service those requests.
        current = r
    queue = sorted(r for r in requests if r < initial_position)
    for r in reversed(queue): # end of disk is reached, reverse direction and continue servicing requests until all requests have been serviced.
        total_head_movement += abs(current - r)
        current = r
    return total_head_movement


# C-SCAN scheduling
def c_scan(initial_position, requests):
    queue = sorted(requests) # sort the sequence of requests in ascending order.
    direction = 1
    current = initial_position # intialize starting value and direction
    total_head_movement = 0 #movement counter
    
    while queue: # while requests in the queue
        next_req = None
        for req in queue:
            if direction == 1 and req >= current: # looking for request in pos direction
                next_req = req
                break
            elif direction == -1 and req <= current:# looking for request in neg direction
                next_req = req
                break
        
        if next_req is None: # no requests in the current direction, switch direction
            direction = -direction
            continue
        
        distance = abs(next_req - current) # calculate distance between current head and request
        total_head_movement += distance # add distance to total head movement, 
        current = next_req # update the head position to the request,
        queue.remove(next_req) # and remove the request from the queue
    return total_head_movement


# main method to call on the functions above
if __name__ == '__main__':
    if len(sys.argv) != 2: # checking to see if user inputed proper parameters
        print("Usage: python RHyria_DSA_CMPSC472.py.py <#initial_position>")
        print("\nHINT: Try numbers like 0, 100, 500, or random.")
        sys.exit(1) 
    
    initial_position = int(sys.argv[1]) # initializing the head based off user input
    
    # Generate a list of random requests
    requests = [random.randint(0, CYLINDERS-1) for _ in range(REQUESTS)]
   
    # Run the algorithms and print the results
    print("FCFS total head movement:", fcfs(initial_position, requests))
    print("SCAN total head movement:", scan(initial_position, requests))
    print("C-SCAN total head movement:", c_scan(initial_position, requests))
