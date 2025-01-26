import numpy as np 
from random import randint 
import random 

class Env(object):

    def __init__(self):
        super(Env, self).__init__()

        self.grid= [
            [0,0,1],
            [0,-1,0],
            [0,0,0]
        ]

        #starting position
        self.y= 2
        self.x= 0

        self.actions= [
            [-1, 0], # UP
            [1, 0], #DOWN
            [0, -1], # LEFT
            [0, 1] #RIGHT
        ]

    def reset(self):
        self.y= 2
        self.x= 0
        return (self.y*3+ self.x+1)
    
    def step(self, action):
        self.y = max(0, min(self.y + self.actions[action][0], 2))
        self.x = max(0, min(self.x + self.actions[action][1], 2))

        return (self.y*3+self.x+1) , self.grid[self.y][self.x]

    
    def is_finished(self):
        return self.grid[self.y][self.x] == 1

    def show(self):
       
        print("---------------------")
        y = 0
        for line in self.grid:
            x = 0
            for pt in line:
                print("%s\t" % (pt if y != self.y or x != self.x else "X"), end="")
                x += 1
            y += 1
            print("")


def take_action(st, Q, eps):
    # take an action
    if random.uniform(0, 1) < eps: # exploration
        action = randint(0, 3)
    else: #greedy action, exploitation
        action = np.argmax(Q[st])

    return action






if __name__ == '__main__':
    env = Env()
    st = env.reset()

    Q = np.zeros((10, 4))

    for _ in range(100):
        # reset the game
        st = env.reset()
        while not env.is_finished():
            
            at= take_action(st, Q, 0.4)
            stp1, r = env.step(at)
            #print(f"state: {stp1} => r: {r}")

            #update the Q 
            atp1 = take_action(stp1, Q, 0.0)
            Q[st][at] = Q[st][at] + 0.1*(r + 0.9*Q[stp1][atp1] - Q[st][at])

            st = stp1

    for s in range(1, 10):
        print(s, Q[s])  