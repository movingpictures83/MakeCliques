# Usage: python makeCliques.py (outputfilename) (size1) (size2) ...

import sys
import numpy
import random
random.seed(1234)   # ONLY FOR TEST PURPOSES, COMMENT OUT FOR BETTER RANDOMNESS

class MakeCliquesPlugin:
   def input(self, filename):
      myfile = open(filename, 'r')
      self.cliquesizes = []
      for line in myfile:
         self.cliquesizes.append(int(line))

   def run(self):
      self.n = sum(self.cliquesizes)

      self.ADJ = numpy.zeros([self.n,self.n])

      currnode = 0
      for cliquesize in self.cliquesizes:
       for j in range(currnode, currnode+cliquesize):
          for k in range(j+1, currnode+cliquesize):
             self.ADJ[j][k] = random.random()   #0 to 1   
       currnode += cliquesize

   def output(self, filename):
    gmlfile = open(filename, 'w')
    gmlfile.write("graph [\n")
    for i in range(self.n):
       gmlfile.write("node [\n")
       gmlfile.write("id "+str(i)+"\n")
       gmlfile.write("label \"A"+str(i)+"\"\n")
       gmlfile.write("]\n")
    for i in range(self.n):
       for j in range(i+1, self.n):
        if (self.ADJ[i][j] != 0):
          gmlfile.write("edge [\n")
          gmlfile.write("source "+str(i)+"\n")
          gmlfile.write("target "+str(j)+"\n")
          gmlfile.write("weight "+str(self.ADJ[i][j])+"\n")
          gmlfile.write("]\n")
    gmlfile.write("]\n")
