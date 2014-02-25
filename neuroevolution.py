#IDEAS:
#Only use the EvoNeuron class, where we can change the weights easily
#Randomly change the weights to see what is better
#decide the fittness based on how many things are correct based on what it SHOULD  be like: if something should be F,F,F and it gives F,F,T the fittness is true

class Neuron:
    global bias
    bias=1
    global weights
    weights=[0,0,0,0]
    def __init__(self):
        self.data=[]
    def NAND(self, i1,i2,i3): #Weights that work for NAND whoo
        summation=0
        inputs=[bias,i1,i2,i3]
        weights[0]=6 #-2+-2+-2 overrides the 6
        weights[1]=-2
        weights[2]=-2
        weights[3]=-2
        for i in range(0,4):
            x=weights[i]
            y=inputs[i]
            summation+=(x*y)
        return summation
    def OR(self, i1,i2,i3): #Weights the work for OR whoo
        summation=0
        inputs=[bias,i1,i2,i3]
        weights[0]=0
        weights[1]=2
        weights[2]=2
        weights[3]=2
        for i in range(0,4):
            summation= summation+(weights[i]*inputs[i])
        return summation
    def Output(self,x):
        if(x>1):
            return True
        else:
            return False

class EvoNeuron:
    global bias
    bias=1 #bias is always 1
    global weights
    def __init__(self):
        self.data=[]
    def Summation(self, i1,i2,i3,w0,w1,w2,w3): #just does the function you want based on the weights given and calculates the sum
        summation=0                            #...yeah so its like all universal and stuff
        inputs=[bias,i1,i2,i3]
        weights=[w0,w1,w2,w3]
        for i in range(0,4):
            x=weights[i]
            y=inputs[i]
            summation+=(x*y)
        return summation
    def Output(self,x):
        if(x>1):
            return True
        else:
            return False


#TODO EVOLVE STUFF

#TEST CASES
n=Neuron() #Neuron n= new Neuron();
print "Our NAND:" #NAND returns true for everything except 1,1,1 (ACTUAL NAND)
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
print "Our OR:"
i=n.OR(0,0,0)
t1= n.Output(i)
print t1
i=n.OR(0,0,1)
t2= n.Output(i)
print t2
i=n.OR(0,1,0)
t3= n.Output(i)
print t3
i=n.OR(1,0,0)
t4= n.Output(i)
print t4
i=n.OR(0,1,1)
t5= n.Output(i)
print t5
i=n.OR(1,1,0)
t6= n.Output(i)
print t6
i=n.OR(1,0,1)
t7= n.Output(i)
print t7
i=n.OR(1,1,1)
t8= n.Output(i)
print t8
