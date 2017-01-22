file = open('rosalind_hamm.txt','r')
rawdata = file.readlines()
data= []
for i in rawdata:
    insert = i.strip('\n')
    data.append(insert)
#1.I would want to compare the two strings with each other
    #I can interate thought a string one character at a time
    #I might have to iterate through one of the seq lists in a for
    #loop and then iterate in the 2nd list
    #I can make a list that corresponds with the string indexes of the
#2.Then I would have to count the number of the mismatches.

length = len(data[1])                 #only need length of one given that both seq lengths are equal
Hamming = 0
for i in range(0,length):
    if data[0][i] != data[1][i]:
        Hamming +=1
print(Hamming)
