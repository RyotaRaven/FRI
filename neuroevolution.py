###IDEAS:
###Only use the EvoNeuron class, where we can change the weights easily
###Randomly change the weights to see what is better
###decide the fittness based on how many things are correct based on what it SHOULD  be like: if something should be F,F,F and it gives F,F,T the fittness is true
##
###This design for the neuron object will be easier to genetically alter, because each neuron will have an array of weights
###In addition, we found out that python doesn't use getter or setter methods in ojects, but this thing called properties
###so for all the object variables you can just do like myNeuron.weights = [1,2,3] or myNeuron.bias = orNeuron.bias etc.
##class Neuron:
##    bias = 0
##    weights = []
##    #I figured you might want to change the amount of inputs in the future so this
##    #constructor initializes a neuron with a given bias and an array of weights with variable length
##    def __init__(self,weights,bias):
##        self.bias = bias
##        self.weights = weights
##    #evaluate the current neuron against an array of inputs and returns whether
##    #the neuron is activated
##    def eval(self, inputs):
##        assert inputs.__len__() == self.weights.__len__() #make sure there are the same amount of inputs and weights
##        activation = 0
##        for i in range(0,inputs.__len__()): # for every input
##            activation += self.weights[i]*inputs[i]
##        return activation > 1 #if the activation is greater than the bias, fire the neuron (true)       


###TODO EVOLVE STUFF
import random
class NeuronEvolution:
    bias = 0
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
            
    def quality(self, weights):
        activation = 0
        for i in range(0,inputs.__len__()):
            activation += self.weights[i]*inputs[i]
        return activation
    
evolveNeuron = NeuronEvolution(100)
print   (evolveNeuron.getWeights())

###TEST CASES
##nandNeuron = Neuron([-2,-2,-2,2],1) #initialize the nand neuron with appropriate weights
###I THINK I HAVE PYTHON 3 ON MY COMPUTER BECAUSE IT WON'T LET ME PRINT WITHOUT PARENTHESES
###I THINK/HOPE IT STILL WORKS ON YOUR MACHINES
##print ("Our NAND:")
###NAND returns true for everything except 1,1,1 (ACTUAL NAND)
##print (nandNeuron.eval([0,0,0,1]))
##print (nandNeuron.eval([0,0,1,1]))
##print (nandNeuron.eval([0,1,0,1]))
##print (nandNeuron.eval([0,1,1,1]))
##print (nandNeuron.eval([1,0,0,1]))
##print (nandNeuron.eval([1,0,1,1]))
##print (nandNeuron.eval([1,1,0,1]))
##print (nandNeuron.eval([1,1,1,1]))
##
##orNeuron = Neuron([2,2,2,0],1) #initialize the or neuron with appropriate weights and 
##print ("Our OR:")
###OR returns true for everything except 0,0,0
##print (orNeuron.eval([0,0,0,1]))
##print (orNeuron.eval([0,0,1,1]))
##print (orNeuron.eval([0,1,0,1]))
##print (orNeuron.eval([0,1,1,1]))
##print (orNeuron.eval([1,0,0,1]))
##print (orNeuron.eval([1,0,1,1]))
##print (orNeuron.eval([1,1,0,1]))
##print (orNeuron.eval([1,1,1,1]))
