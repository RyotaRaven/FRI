#IDEAS:
#Only use the EvoNeuron class, where we can change the weights easily
#Randomly change the weights to see what is better
#decide the fittness based on how many things are correct based on what it SHOULD  be like: if something should be F,F,F and it gives F,F,T the fittness is true

class Neuron:
    bias = 0
    weights = []
    #I figured you might want to change the amount of inputs in the future so this
    #constructor initializes a neuron with bias one and variable length of weights
    def __init__(self,weights,bias):
        self.bias = bias
        self.weights = weights
    #evaluate the current neuron against an array of inputs and returns whether
    #the neuron is activated
    def eval(self, inputs):
        assert inputs.__len__() == self.weights.__len__() #make sure there are the same amount of inputs and weights
        activation = 0
        for i in range(0,inputs.__len__()): # for every input
            activation += self.weights[i]*inputs[i]
        return activation > self.bias #if the activation is greater than the bias, fire the neuron (true)       


#TODO EVOLVE STUFF

#TEST CASES
nandNeuron = Neuron([-1,-1,-1],-3) #initialize the nand neuron with appropriate weights
print ("Our NAND:")
#NAND returns true for everything except 1,1,1 (ACTUAL NAND)
print (nandNeuron.eval([0,0,0]))
print (nandNeuron.eval([0,0,1]))
print (nandNeuron.eval([0,1,0]))
print (nandNeuron.eval([0,1,1]))
print (nandNeuron.eval([1,0,0]))
print (nandNeuron.eval([1,0,1]))
print (nandNeuron.eval([1,1,0]))
print (nandNeuron.eval([1,1,1]))

orNeuron = Neuron([1,1,1],0) #initialize the or neuron with appropriate weights and 
print ("Our OR:")
print (orNeuron.eval([0,0,0]))
print (orNeuron.eval([0,0,1]))
print (orNeuron.eval([0,1,0]))
print (orNeuron.eval([0,1,1]))
print (orNeuron.eval([1,0,0]))
print (orNeuron.eval([1,0,1]))
print (orNeuron.eval([1,1,0]))
print (orNeuron.eval([1,1,1]))
