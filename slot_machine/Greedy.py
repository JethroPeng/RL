from slot_machines import *
import random
import matplotlib.pyplot as plt

class Greedy:
    def __init__(self,e,k,u=[],sig=[]):
        self.e = e
        self.k = k
        self.machines = slot_machine(k,u,sig)
        self.preward = []
        self.time = []
        self.train_time = 0
        self.rewardline = []
        self.avgreward = []
    def train_sample(self):
        if (len(self.preward)<self.k):
            self.train_time +=1
            res = self.machines.randomNum(len(self.preward))
            self.preward.append(res)
            self.time.append(1)
            self.rewardline.append(res)
            if (len(self.avgreward)!=0):
                self.avgreward.append(self.avgreward[-1]+((res - self.avgreward[-1]) / self.train_time))
            else:
                self.avgreward.append(res)
        else:
            self.train_time += 1
            rand = random.random()
            if rand<(1-self.e):
                choose = self.preward.index(max(self.preward))
            else:
                choose = int(rand*10)
            res = self.machines.randomNum(choose + 1)
            self.time[choose] = self.time[choose] + 1
            self.preward[choose] = self.preward[choose] + ((res - self.preward[choose]) / self.time[choose])
            self.rewardline.append(res)
            self.avgreward.append(self.avgreward[-1] + ((res - self.avgreward[-1]) / self.train_time))
    def train(self,k):
        for i in range(k):
            self.train_sample()
    def draw(self):
        x = np.linspace(1,len(self.avgreward)+1,len(self.avgreward))
        plt.plot(x, self.avgreward, "r-", linewidth=2)
        plt.grid(True)
        plt.show()
    def drawdata(self):
        return self.avgreward

#实例化
d1 = Greedy(0,10)
d2 = Greedy(0.01,10)
d3 = Greedy(0.1,10)
d1.train(1000)
d2.train(1000)
d3.train(1000)

#绘图
x = np.linspace(1,len(d1.avgreward)+1,len(d1.avgreward))
plt.plot(x, d1.avgreward, "r", linewidth=1,label = '0')
plt.plot(x, d2.avgreward, "g", linewidth=1,label = '0.01')
plt.plot(x, d3.avgreward, "b", linewidth=1,label = '0.1')
plt.legend(loc='best')
plt.grid(True)
plt.show()

