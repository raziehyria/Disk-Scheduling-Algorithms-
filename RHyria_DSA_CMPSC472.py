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
    current = initial_position # Read the initial position of the disk head.
    for r in requests:
        total_head_movement += abs(r - current) # Calculate the distance between the initial head position and the first request.
        current = r
    return total_head_movement # return the total distance traveled.


# SCAN scheduling
def scan(initial_position, requests):
    total_head_movement = 0
    current = initial_position
    queue = sorted(r for r in requests if r >= initial_position) # Sort the sequence of requests in ascending order.
    for r in queue: #Find the index of the request that is closest to the initial head position
        total_head_movement += abs(current - r) # service those requests.
        current = r
    queue = sorted(r for r in requests if r < initial_position)
    for r in reversed(queue): # end of disk is reached, reverse direction and continue servicing requests until all requests have been serviced.
        total_head_movement += abs(current - r)
        current = r
    return total_head_movement


# C-SCAN scheduling
def cscan(initial_position, requests):
    total_head_movement = 0
    current = initial_position
    queue = sorted(requests + [initial_position]) # Sort the sequence of requests in ascending order.
    left = [r for r in queue if r < initial_position] # Find the index of the request that is closest to the initial head position.
    right = [r for r in queue if r >= initial_position] # Find the index of the request that is opposite to the initial head position.
    for r in right:
        total_head_movement += abs(current - r) #Service all requests from the initial 
        current = r
    current = 0 # reset position of the head 
    for r in left + [max(queue)]:
        total_head_movement += abs(current - r) #Service all requests from the opposite side 
        current = r
    return total_head_movement# return the total distance traveled.

# main method to call on the functions above
if __name__ == '__main__':
    if len(sys.argv) != 2: # checking to see if user inputed proper parameters
        print("Usage: python RHyria_DSA_CMPSC472.py.py initial_position")
        sys.exit(1) 
    
    initial_position = int(sys.argv[1]) # initializing the head based off user input
    
    # Generate a list of random requests
    requests = [random.randint(0, CYLINDERS-1) for _ in range(REQUESTS)]
   
    # Run the algorithms and print the results
    print("FCFS scheduling:", fcfs(initial_position, requests))
    print("SCAN scheduling:", scan(initial_position, requests))
    print("C-SCAN scheduling:", cscan(initial_position, requests))
