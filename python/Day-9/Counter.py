from collections import Counter
a=Counter("encyclopedia")       #display the max letter count first so that we using counter
print(a)
print(a.most_common(3)) #it shows in list format and it gives first 3 max
print(a.clear())  #it clear all
print(a.most_common(3))  #after clear there is no parameters

