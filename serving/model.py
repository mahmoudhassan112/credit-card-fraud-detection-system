import torch
import torch.nn as nn

class ExperimentModel_1(nn.Module):
    
   """
   
   Simple feedforward neural network for binary classification.
        
   Layers:
   512 → 128 → 64 → 1 with BatchNorm and ReLU.
   Final Sigmoid outputs probability.
        
   Input: (df.shape[0], 512)
   Output: (df.shape[0], 1)
   
   """

   def __init__(self , *args , **kwargs):
       
       super().__init__(*args , **kwargs)

       # initilize model'layers

       self.fc1 = nn.Linear(30 , 128) # fc1
       self.bn1 = nn.BatchNorm1d(128) # bn1
       self.relu = nn.ReLU() # relu

       self.fc2 = nn.Linear(128 , 64) # fc2
       self.bn2 = nn.BatchNorm1d(64) # bn2

       self.fc3 = nn.Linear(64, 1) #fc3
       self.sigmoid = nn.Sigmoid() # sigmoid
       
   def forward(self , x):

       x = self.fc1(x)
       x = self.bn1(x)
       x = self.relu(x)

       x = self.fc2(x)
       x = self.bn2(x)

       x = self.fc3(x)
       x = self.sigmoid(x)

       return x

