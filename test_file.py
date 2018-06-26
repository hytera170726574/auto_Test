from PIL import  Image
import math
import operator
from functools import reduce
im1=Image.open("4.png")
im2=Image.open("4.png")
h1=im1.histogram()
h2=im2.histogram()
result=math.sqrt(reduce(operator.add,list(map(lambda a,b:(a-b)**2,h1,h2)))/len(h1))

print result