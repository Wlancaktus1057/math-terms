'''
This is a program wich makes mathematical terms and solves them
Oliver Leitner's first program 2021-01-25
'''
import sys
import time
from random import *

exec_count = 10 #the standard count of exercises if no arguments are given

if len(sys.argv) == 2:
    exec_count = int(sys.argv[1])

count = 1

while count <= exec_count:

    a = randint(-9, 9)
    b = randint(-9, 9)
    c = randint(-9, 9)
    d = randint(-9, 9)

    if a == c:
        continue
    
    solution = (d-b)/(a-c)#gets the solution

    int_solution = int(solution)

    if solution != int_solution:#checks if the term can be solved/makes sense
        continue

    if b >= 0:
        bb = f"+ {b}"
    else:
        bb = f"- {-b}"
    
    if d >= 0:
        dd = f"+ {d}"
    else:
        dd = f"- {-d}"#formating for displaying the'+'
    
    print(f"{count}:  {a}x {bb} = {c}x {dd}               x = {int_solution}\n")
    ##time.sleep(1)
    count += 1
