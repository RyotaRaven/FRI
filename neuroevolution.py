#IDEAS:
#Only use the EvoNeuron class, where we can change the weights easily
#Randomly change the weights to see what is better
#decide the fittness based on how many things are correct based on what it SHOULD  be like: if something should be F,F,F and it gives F,F,T the fittness is true

#This design for the neuron object will be easier to genetically alter, because each neuron will have an array of weights
#In addition, we found out that python doesn't use getter or setter methods in ojects, but this thing called properties
#so for all the object variables you can just do like myNeuron.weights = [1,2,3] or myNeuron.bias = orNeuron.bias etc.

import random

class Neuron:
    weights = []
    #I figured you might want to change the amount of inputs in the future so this
    #constructor initializes a neuron where weights[0] is the bias weight and weights[1-n] are the normal input weights
    def __init__(self,weights):
        self.weights = weights
    #evaluate the current neuron against an array of inputs and returns whether
    #the neuron is activated
    def eval(self, inputs):
        inputs.insert(0,1) #add the bias input (always one) to the input array (at the beginning)
        assert inputs.__len__() == self.weights.__len__() #make sure there are the same amount of inputs and weights
        activation = 0
        for i in range(0,inputs.__len__()): # for every input
            activation += self.weights[i]*inputs[i]
        if (activation > 1):
            return 1
        else: return 0#if the activation is greater or equal to 0 (step function), fire the neuron (true)       


#TODO EVOLVE STUFF
class NeuronEvolution:
    bias = 1
    weights = []
    number_Of_Tweaks=0;
    randomWeights = []
    tweakedWeights=[]
    activation=0
    
    def __init__(self,numTweaks):
        number_Of_Tweaks=numTweaks
        
    def getWeights(self):
        for i in range(0, 3):
            self.randomWeights[i]=random.uniform(-1,1)
        for i in range(0,inputs.__len__()):
            activation += self.weights[i]*inputs[i]
            
        while activation<=1:
            for j in range(0,3):
                tweakedWeights[j]=self.randomWeights[j]*random.uniform(-1,1)
            if quality(tweakedWeights) > quality(self.randomWeights):
                randomWeights=tweakedWeights
        return randomWeights

"""class NeuralNetwork:
    hidNeuron1 = Neron([])
    hidNeuron2 = Neron([])
    outNeuron = Neron([])
    def __init__():
        self.data=[]"""

#return the amount of times the output of a neuron was the same as the expected output that was passed in an array
#this functions tests all inputs in this form 
#expected[0]==neuron.eval([0,0,0])
#expected[1]==neuron.eval([0,0,1])
#expected[1]==neuron.eval([0,1,0]) etc.
def quality(neuron, expected): 
    assert 2**(neuron.weights.__len__()-1) == expected.__len__() #make sure there are the same amount of unique inputs and expected values
    correct = 0
    for i in range(0,(2**(neuron.weights.__len__()-1))):
        total = i
        inputs = []
        for j in range(neuron.weights.__len__()-2,-1,-1):   #for every binary digit in the input (starting from the number of inputs-1 and going to 0)
            inputs.append(total//(2**j))                #add a digit to the inputs (// is floor division)
            total -= (total//(2**j))*(2**j)             #subtract the binary value of the digit if it was one
        #print (inputs)                                 #proof that it goes through all possible inputs
        if expected[i]==neuron.eval(inputs):
            correct += 1     #one more of the expected inputs is correct
    return correct


##evolveNeuron = NeuronEvolution(100)
##print   (evolveNeuron.getWeights())

#TEST CASES
nandNeuron = Neuron([6,-2,-2,-2]) #initialize the nand neuron with appropriate weights
#I THINK I HAVE PYTHON 3 ON MY COMPUTER BECAUSE IT WON'T LET ME PRINT WITHOUT PARENTHESES
#I THINK/HOPE IT STILL WORKS ON YOUR MACHINES
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
print ("Quality of NAND:" , quality(nandNeuron,[True,True,True,True,True,True,True,False]))

orNeuron = Neuron([0,2,2,2]) #initialize the or neuron with appropriate weights and 
print ("Our OR:")
#OR returns true for everything except 0,0,0
print (orNeuron.eval([0,0,0]))
print (orNeuron.eval([0,0,1]))
print (orNeuron.eval([0,1,0]))
print (orNeuron.eval([0,1,1]))
print (orNeuron.eval([1,0,0]))
print (orNeuron.eval([1,0,1]))
print (orNeuron.eval([1,1,0]))
print (orNeuron.eval([1,1,1]))
print ("Quality of OR:" , quality(orNeuron,[False,True,True,True,True,True,True,True]))
