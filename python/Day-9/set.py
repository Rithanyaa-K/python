setEg1 = set ()#{},{1,2,3}
setEg1.add(1)
setEg1.add(5)
setEg1.add(5)
setEg1.add(6)
print(setEg1)
setEg2={1,7}
setEg3=setEg2 | setEg1  #unoin- print all
print(setEg3)
setEg4=setEg2 & setEg1 #intersection -common
print(setEg4)
setEg5=setEg1 - setEg2 
print(setEg5)
setEg6=setEg2 - setEg1
print(setEg6)
