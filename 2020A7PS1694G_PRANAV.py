#!/usr/bin/env python3
from Agent import * # See the Agent.py file
from pysat.solvers import Glucose3
import time 

#### All your code can go here.

#### You can change the main function as you wish. Run this program to see the output. Also see Agent.py code.

# Global variables
start = time.time()
Agent_has_visited = []
foundGold = False       # boolean flag to check if gold has been found by agent

def FindAdjacentRooms(curLoc):
    cLoc = curLoc
    validMoves = [[0,1],[0,-1],[-1,0],[1,0]]
    adjRooms = []
    for vM in validMoves:
        room = []
        valid = True
        for v, inc in zip(cLoc,vM):
            z = v + inc
            if z<1 or z>5:  #Check whether index is between 1 and 5
                valid = False
                break
            else:
                room.append(z)
        if valid==True:
            adjRooms.append(room)
    return adjRooms

def room_to_num(room):
    return ((room[0]*10) + room[1])

class KB:
    def __init__(self):
        self.g = Glucose3()
        self.g.add_clause([-11])        # [1,1] is safe
        self.g.add_clause([-25,-34,-23,-14,240])    # condition for gold in room [2,4]
        self.g.add_clause([-35,-44,-33,-24,340])    # condition for gold in room [3,4]
        self.g.add_clause([-45,-54,-43,-34,440])    # condition for gold in room [4,4]
        self.g.add_clause([-24,-33,-22,-13,230])    # condition for gold in room [2,3]
        self.g.add_clause([-34,-43,-32,-23,330])    # condition for gold in room [3,3]
        self.g.add_clause([-44,-53,-42,-33,430])    # condition for gold in room [4,3]
        self.g.add_clause([-23,-32,-21,-12,220])    # condition for gold in room [2,2]
        self.g.add_clause([-33,-42,-31,-22,320])    # condition for gold in room [3,2]
        self.g.add_clause([-43,-52,-41,-32,420])    # condition for gold in room [4,2]
    
    def TELL(self,ag):
        percept = ag.PerceiveCurrentLocation()
        adj_rooms = FindAdjacentRooms(ag.FindCurrentLocation())
        num_adj_rooms = len(adj_rooms)

        if (percept == 0):
            for room in adj_rooms:
                val = room_to_num(room)
                self.g.add_clause([-val])
        
        elif (percept == 1):
            clause = []
            for room in adj_rooms: 
                val = room_to_num(room)
                clause.append(val)
            self.g.add_clause(clause)

            for i in range(num_adj_rooms):
                for j in range(i+1,num_adj_rooms):
                    temp_clause = []
                    temp_clause.append(-(clause[i]))
                    temp_clause.append(-(clause[j]))
                    self.g.add_clause(temp_clause)
        
        elif (percept == 2):
            clause = []
            for room in adj_rooms:
                val = room_to_num(room)
                clause.append(val)
            
            if (num_adj_rooms == 2):
                for cl in clause:
                    self.g.add_clause([cl])
            
            elif (num_adj_rooms == 3):
                temp_clause=[]
                temp_clause.append(clause[0])
                temp_clause.append(clause[1])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[0])
                temp_clause.append(clause[2])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[1])
                temp_clause.append(clause[2])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(-clause[0])
                temp_clause.append(-clause[1])
                temp_clause.append(-clause[2])
                self.g.add_clause(temp_clause)
            
            else:
                temp_clause=[]
                temp_clause.append(-clause[0])
                temp_clause.append(-clause[1])
                temp_clause.append(-clause[2])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(-clause[0])
                temp_clause.append(-clause[1])
                temp_clause.append(-clause[3])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(-clause[0])
                temp_clause.append(-clause[2])
                temp_clause.append(-clause[3])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[0])
                temp_clause.append(clause[1])
                temp_clause.append(clause[2])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[0])
                temp_clause.append(clause[1])
                temp_clause.append(clause[3])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[0])
                temp_clause.append(clause[2])
                temp_clause.append(clause[3])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(-clause[1])
                temp_clause.append(-clause[2])
                temp_clause.append(-clause[3])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[1])
                temp_clause.append(clause[2])
                temp_clause.append(clause[3])
                self.g.add_clause(temp_clause)
            
        elif (percept == 3):
            clause = []
            for room in adj_rooms:
                val = room_to_num(room)
                clause.append(val)
            
            if (num_adj_rooms == 3):
                for cl in clause:
                    self.g.add_clause([cl])
            
            else:
                temp_clause=[]
                temp_clause.append(-clause[0])
                temp_clause.append(-clause[1])
                temp_clause.append(-clause[2])
                temp_clause.append(-clause[3])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[0])
                temp_clause.append(clause[1])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[0])
                temp_clause.append(clause[2])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[0])
                temp_clause.append(clause[3])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[1])
                temp_clause.append(clause[2])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[1])
                temp_clause.append(clause[3])
                self.g.add_clause(temp_clause)

                temp_clause=[]
                temp_clause.append(clause[2])
                temp_clause.append(clause[3])
                self.g.add_clause(temp_clause) 
    
    def ASK(self,clause):
        if (self.g.solve(assumptions=[-clause]) == False):
            return True 
        else:
            return False
 

def PlanPath(curLoc,kb):       # function to plan a path from current room to nearest unvisited safe room
    queue = []
    queue.append(curLoc)
    path=[]
    parent_map={}
    visited=[]
    next_room = [0,0]

    while(queue):
        head = queue.pop(0)
        if ((kb.ASK(-room_to_num(head))) and (head not in Agent_has_visited)):  # checking if room is safe and unvisited
            next_room = head     # setting next_room as head
            break 
        
        adj_rooms = FindAdjacentRooms(head)
        for room in adj_rooms:
            if ((kb.ASK(-room_to_num(room))) and (room not in visited)):     # checking if room is safe and has not been visited during bfs
                parent_map[room_to_num(room)] = room_to_num(head)     # storing parent room of current room to construct path
                queue.append(room)
                visited.append(room)
        
    if (next_room == [0,0]):        # there is no unvisited safe room
        return path
    while (next_room != curLoc):    # making path from curLoc to next_room
        path.append(next_room)
        val = parent_map[room_to_num(next_room)]
        next_room = [val//10,val%10]
    path.reverse()
    return path 

def moveToLoc(ag,path):     # function to move from current room to new room given a path
    print("Current location is ",ag.FindCurrentLocation())
    print("Path is: ",end=" ")
    for room in path:
        print(" -> ",room,end=" ")
    print()

    for next_room in path:
        if (ag.FindCurrentLocation()[0] == next_room[0]):
            if (ag.FindCurrentLocation()[1] > next_room[1]):
                ag.TakeAction('Down')
            else:
                ag.TakeAction('Up')
        else:
            if (ag.FindCurrentLocation()[0] > next_room[0]):
                ag.TakeAction('Left')
            else:
                ag.TakeAction('Right')
    print()

def check_for_Gold(kb):     # checking if GOLD can be infered from current KB
    global foundGold
    if (kb.ASK(240)):               
        print("Gold is present in room [2,4].")
        foundGold = True  
 
    if (kb.ASK(340)):
        print("Gold is present in room [3,4].")
        foundGold = True 
        
    if (kb.ASK(440)):
        print("Gold is present in room [4,4].")
        foundGold = True 
        
    if (kb.ASK(230)):
        print("Gold is present in room [2,3].")
        foundGold = True 
        
    if (kb.ASK(330)):
        print("Gold is present in room [3,3].")
        foundGold = True 
        
    if (kb.ASK(430)):
        print("Gold is present in room [4,3].")
        foundGold = True 
        
    if (kb.ASK(220)):
        print("Gold is present in room [2,2].")
        foundGold = True 
        
    if (kb.ASK(320)):
        print("Gold is present in room [3,2].")
        foundGold = True 
        
    if (kb.ASK(420)):
        print("Gold is present in room [4,2].")
        foundGold = True 
        

def main():
    ag = Agent()
    kb = KB()
    
    Agent_has_visited.append([1,1])     # adding [1,1] to list of visited rooms
    kb.TELL(ag)     # percieving at [1,1] and adding corresponding clauses to KB
    path = PlanPath(ag.FindCurrentLocation(),kb)       # planning path to nearest unvisited and safe room
    
    while (len(path) != 0):     # when path is empty, it means that there is no safe room that is unvisited
        
        moveToLoc(ag,path)      # move to nearest unvisited safe room using the path
        curLoc = ag.FindCurrentLocation()
        Agent_has_visited.append(curLoc)        # adding the new room to list of visited rooms
        kb.TELL(ag)     # percieving current room and adding corresponding clauses to KB
        path = PlanPath(curLoc,kb)     # plan a new path to next nearest unvisited safe room
        check_for_Gold(kb)
        if (foundGold):
            break 

    if (foundGold == False):        # checking if loop exited after finding GOLD or without finding GOLD
        print("Gold could not be detected after visiting all the safe rooms.")
    
    print("Time taken: ",time.time()-start)


if __name__=='__main__':
    main()
