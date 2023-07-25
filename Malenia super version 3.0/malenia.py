import random
import json
import torch
from brain import NeuralNetwork
from neuralnet import sac_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('intents.json','r') as json_data:
    intents = json.load(json_data)

FILE = 'traindata.pth'
data = torch.load(FILE)

input_layer = data["input_layer"]
hidden_layer = data["hidden_layer"]
output_layer = data["output_layer"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetwork(input_layer,hidden_layer,output_layer).to(device=device)
model.load_state_dict(model_state)
model.eval()

#------------------------------------------------------------------------------

Name = "Malenia"
from listen import listen
from speak import say
def Main():
    sentence = listen()
    
    if sentence == "goodbye":
        exit()
    sentence = tokenize(sentence)

    X = sac_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _ , predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                say(reply)

    
while True:
      Main()