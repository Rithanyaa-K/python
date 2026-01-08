import csv
with open("day-10/StudentsData.csv",'w') as data:
    writer=csv.writer(data)
    writer.writerow(["S.NO","Name","Dept"])
    writer.writerow([1,"Rithanyaa","BSC"])
    writer.writerow([2,"Nethraa","BSC"])
    writer.writerow([3,"Kani","BSC"])