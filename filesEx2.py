#write a program that calculates the average grade for each student, 
#and print out the student’s name along with their average grade.


infile = open("C:\Users\NinjaZeroOne\Desktop\studentdata.txt", "r")
line = infile.readline()

def average(yourList):
	theSum = 0
	for i in yourList:
        theSum = theSum + i
	return theSum


while line:
	values = line.split()
	print (values[0], "average is", average(values[1:]))

    
infile.close()