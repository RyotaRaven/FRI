class Neuron:
    global bias
    bias=1
    global weights
    weights=[0,0,0,0]
    #int i[]={1,2,3,4}
    #i[0]=5
    #{5,2,3,4}
    summation=0
    def __init__(self):
        self.data=[]
    def NAND(i1,i2,i3):
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
    def OR(i1,i2,i3):
        summation=0
        inputs=[bias,i1,i2,i3]
        weights[0]=1
        weights[1]=0
        weights[2]=0
        weights[3]=0
        for i in range(0,4):
            summation= summation+(weights[i]*inputs[i])
    def Output():
        if(summation>1):
            return True
        else:
            return False

n=Neuron()
n.NAND(0,0,0)
t1= n.Output()
print t1
n.NAND(0,1,0)
t2= n.Output()
print t2
    
