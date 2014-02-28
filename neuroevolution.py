import random

class Neuron:
    weights = []
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

class NeuronEvolution:
    bias = 1
    weights = []
    number_Of_Tweaks=0;
    randomWeights = []
    tweakedWeights = []
    activation = 0

    def __init__(self,numTweaks):
        number_Of_Tweaks = numTweaks

    def getWeights(self):
        for i in range(0, 3):
            self.randomWeights[i] = random.uniform(-1,1)
        for i in range(0,inputs.__len__()):
            activation += self.weights[i]*inputs[i]

        while activation<=1:
            for j in range(0,3):
                tweakedWeights[j] = self.randomWeights[j]*random.uniform(-1,1)
            if quality(tweakedWeights) > quality(self.randomWeights):
                randomWeights = tweakedWeights
        return randomWeights

class NeuralNetwork:
    global hidNeuron1
    global hidNeuron2
    global outNeuron
    global bias
    bias = 1
    def __init__(self, weight1, weight2, weight3):
        self.hidNeuron1 = Neuron(weight1)
        print(weight2)
        print(len(weight2))
        self.hidNeuron2 = Neuron(weight2)
        print(weight3)
        print(len(weight3))
        self.outNeuron = Neuron(weight3)

    def evaluate(self, inputs):
        #the eval method automatically inserts the bias input as 1 (so you just have to pass in the other inputs)
        print(inputs)
        one=self.hidNeuron1.eval(inputs)
        print(one)
        two=self.hidNeuron2.eval(inputs)
        print(two)
        out=[1,one,two]
        print(len(out))
        print(out)
        return self.outNeuron.eval(out)


#return the amount of times the output of a neuron was the same as the expected output that was passed in an array
#this functions tests all inputs in this form
#expected[0]==neuron.eval([0,0,0])
#expected[1]==neuron.eval([0,0,1])
#expected[2]==neuron.eval([0,1,0]) etc.
def quality(neuron, expected):
    assert 2**(neuron.weights.__len__()-1) == expected.__len__() #make sure there are the same amount of unique inputs and expected values
    correct = 0
    for i in range(0,(2**(neuron.weights.__len__()-1))):
        total = i
        inputs = []
        for j in range(neuron.weights.__len__()-2,-1,-1):   #for every binary digit in the input (starting from the number of inputs-1 and going to 0)
            inputs.append(total//(2**j))                #add a digit to the inputs (// is floor division)
            total -= (total//(2**j))*(2**j)             #subtract the binary value of the digit if it was one
        if expected[i] == neuron.eval(inputs):
            correct += 1     #one more of the expected inputs is correct
    return correct


##evolveNeuron = NeuronEvolution(100)
##print   (evolveNeuron.getWeights())

#TEST CASES
nandNeuron = Neuron([6,-2,-2,-2]) #initialize the nand neuron with appropriate weights
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

network = NeuralNetwork([6,-2,-2,-2], [6,-2,-2,-2], [0,1,1])
print ("Our NAND network:")
#NAND returns true for everything except 1,1,1 (ACTUAL NAND)
print (network.evaluate([0,0,0]))
print (network.evaluate([0,0,1]))
print (network.evaluate([0,1,0]))
print (network.evaluate([0,1,1]))
print (network.evaluate([1,0,0]))
print (network.evaluate([1,0,1]))
print (network.evaluate([1,1,0]))
print (network.evaluate([1,1,1]))
print ("Quality of OR:" , quality(orNeuron,[False,True,True,True,True,True,True,True]))
