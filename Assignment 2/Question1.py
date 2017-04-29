# loading neuron 1 - 4 and time using the provided code snippets
csvneuron1 = open("data/neuron1.csv")
neuron1 = map( lambda x: int(x.strip()), csvneuron1.readlines() )
csvneuron2 = open("data/neuron2.csv")
neuron2 = map( lambda x: int(x.strip()), csvneuron2.readlines() )
csvneuron3 = open("data/neuron3.csv")
neuron3 = map( lambda x: int(x.strip()), csvneuron3.readlines() )
csvneuron4 = open("data/neuron4.csv")
neuron4 = map( lambda x: int(x.strip()), csvneuron4.readlines() )
csvtime = open("data/time.csv")
time = map( lambda x: int(x.strip()), csvtime.readlines() )

#  loading x and y using the provided code snippets
csv_x = open("data/x.csv")
x = map( lambda x: float(x.strip()), csv_x.readlines() )
csv_y = open("data/y.csv")
y = map( lambda x: float(x.strip()), csv_y.readlines() )