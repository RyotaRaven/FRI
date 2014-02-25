class Neuron:
    global bias
    bias=1
    global weights
    weights=[0,0,0,0]
    def __init__(self):
        self.data=[]
    def NAND(self, i1,i2,i3):
        summation=0
        inputs=[bias,i1,i2,i3]
        weights[0]=2
        weights[1]=-2
        weights[2]=-2
        weights[3]=-2
        for i in range(0,4):
            x=weights[i]
            y=inputs[i]
            summation+=(x*y)
        return summation
    def OR(self, i1,i2,i3):
        summation=0
        inputs=[bias,i1,i2,i3]
        weights[0]=1
        weights[1]=0
        weights[2]=0
        weights[3]=0
        for i in range(0,4):
            summation= summation+(weights[i]*inputs[i])
        return summation
    def Output(self,x):
        if(x>1):
            return True
        else:
            return False

n=Neuron() #Neuron n= new Neuron();
i=n.NAND(0,0,0)
t1= n.Output(i)
print t1
i=n.NAND(0,0,1)
t2= n.Output(i)
print t2
i=n.NAND(0,1,0)
t3= n.Output(i)
print t3
i=n.NAND(1,0,0)
t4= n.Output(i)
print t4
i=n.NAND(0,1,1)
t5= n.Output(i)
print t5
i=n.NAND(1,1,0)
t6= n.Output(i)
print t6
i=n.NAND(1,0,1)
t7= n.Output(i)
print t7
i=n.NAND(1,1,1)
t8= n.Output(i)
print t8
