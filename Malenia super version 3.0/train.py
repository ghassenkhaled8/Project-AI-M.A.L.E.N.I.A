import numpy as np 
import torch
import json
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from neuralnet import sac_of_words, tokenize, stem
from brain import NeuralNetwork
import nltk
from nltk import sent_tokenize
from typing import ClassVar


with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []


for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w,tag))

ignore_words = [',','?','/','.','!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

x_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    sac = sac_of_words(pattern_sentence, all_words)
    x_train.append(sac)

    label = tags.index(tag)

    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

num_epochs = 1000
batch_size = 8
learning_rate = 0.001
input_layer = len(x_train[0])
hidden_layer = 8
output_layer = len(tags)

print("training model ...")

class Chat_Data(Dataset):
    def __init__(self):
        self.n_samples = len(x_train)
        self.x_data = x_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples
    
dataset = Chat_Data()

train_loader = DataLoader(dataset=dataset,
                          batch_size=batch_size,
                          shuffle=True,
                          num_workers=0)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNetwork(input_layer,hidden_layer,output_layer).to(device=device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    for(words, labels)in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        outputs = model(words)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch+1) % 100 == 0:
            print(f"epoch[{epoch+1}/{num_epochs}], loss: {loss.item():.4f}")

print(f"final loss : {loss.item():.4f}")


data = {
"model_state":model.state_dict(),
"input_layer":input_layer,
"hidden_layer":hidden_layer,
"output_layer":output_layer,
"all_words":all_words,
"tags":tags
}

FILE = "traindata.pth"
torch.save(data,FILE)
print(f"trainig complete, file saved to {FILE}")