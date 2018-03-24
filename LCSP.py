#Two DNA Sequences
s1 = "CTAGAAGTGATAGCTTCCCAAGTATGAAGTTCACCCACTTAAAGTCTGGAGGAATACCAATTTGGAGGCTAAACTTTACTCCATCCATTCAGACCTATGTTTTCCGATCGCCGGGGTTCTCTTCACGCGTGTCTACATATCTATTCAGTGCTATATGGTAGAAAATGATCACTGACCGGGTTCGATAACAAAGGGGATCAGCTTTCAATTTTCAATGTACATCCAAACTAGTGTTGTGGACTCTCCCAAGAATAGGCACTCCGGCACTATTCCGATCTATAGAAACGGCCCACCCACAGTTCTGGGATCAGGTGCTCTGCGAATGTAGTTGTACCAGCATTTGTGGCCCGGAACGCTGTACGCAATATCGTGATAGAGTTAAACAGTGTACAAGAGGTAATAGCGAGTTACGTAAAAGGTGCAAGCGCAAAATAAGTCCAATATGCCCGGGTACCCCGCTGAAAGCGAATCTCGTTATGGCTCATTTAACTAAGCGTAGAGGTGCAGAAAATTGCAGGCACTGGTCCTGGTGTTTTAGGTCTGCCCCGTCCGGTGAAATTGTGCCCATAGGTAAACCAAGGTCTAGTCTGAGGCTAGTGTGTGGTAGGATGTTTGGGCGTCCTTGCGTCGCGGGTCGCTATATCTCAGTGGACCTATGGCTTGCCTTGTGAGCACGGATCTCAATTAATATAGCGATACCGTACAGTTTAAGTATGAAGCGCCCCGGCGGCGGAGCCTTTGGATACCCCCCCAGTAGCAAACAGCCGGTCCCACACTTTACTCTGGTAAGACCATGATGGTGCTGCGACTCGAAGTGGGGTCCCCGACTCACCGTCGAGGTCCGTGTTATCCCGCCTATGTCTGAGTTACTAGCTGATCTGCGTCTGGGGGTGGCAT" #v
s2 = "CAAGCGGTAGTGGTTAGATCTAGAGCCACGTGAACCTTTAAGTGCACCTAGTCATTCGGACTGTCAGTTGCGCATGGACGCGTGCAAAATTCAGTGAGGTAGCGCTCACCTATCATTTGTTTTTACGGCTGACACCGCGTTCGGATGGATTTGCAGGAGACCCGCCGTTGGGCCGGACGGGTTACGGGCTCTAGGTTGGTACCTCCTTTCGGAAAAGAGTAACCTTATACCACAGTCGCCTAGGGGGCGCATTGCTGGATAGGTCCTCCGCGGAGTCTTGGTACTTTAATGCAGATCGTGAGGGCCTTCGAGCGTTGAGGAACAATGTACTAAATATCATGTCCTGCGTTGTATAGGCTACATTGTATGAGGTTAGGTCTGCCAAAGGATGCTGCAGCATACTAGGTAACTGTTAGAGCGTGGTACACAGACGTTAAACCAGGTTAACTGTTGGACCGGTTACGACCTGCCACGCATCCATTGGATCCTTATGGTTGTTGGCCCGCAAACCCCACTAGCGGTCATTTAGGATAATACTTGACGGTCCGGAATACGAGTGGTTCATGGATGCCAGTTGTAAAGTCGAAAACTCCGCAAACCTAACGTAGCATCGCCTGACGGCATCTCCATGTCAAAGACGTATAATTGACCTCAGAACTCGTAATTATACCATATGGGAGGCCGGGAACGCTGGTCGGCTTCCTAAAAAGTCTTTCATTGAGTCTCGTGGTCCTGAGGGACCAATAACGAGGACGTGCAAACCTGTTTTTTAGGTATCAGACTACTCGAACTAATCGACGGTAGGGTCGACGAATCTGTGTTCATATACGCGTAGCGGTAAGTTCTTTACGAATGTTCTCTAAAGATGCTCGAAGCTAAACTAAACGTGGCAGATTGCAGTGTC" #w

#2-Dimension array
    #it will store scores the greates score in each,
    #row or column will be apart of the final
    #longest common supsquence.
matrix = [[0 for x in range(len(s2)+1)] for y in range(len(s1)+1)]

x = 0  # row
y = 0  # column

for i in s1: #gets the characters of string 1.
    for j in s2: #gets the character of string 2.
        if i == j:
            matrix[x+1][y+1] = matrix[x][y] + 1
        else:
            matrix[x+1][y+1] = max(matrix[x+1][y], matrix[x][y+1])
        #print(matrix[x][y],end=",")
        y += 1 
    x += 1 
    y = 0  #need to reset rows. 
    #print()
#print()

LCS = ""
x = len(s1)
y = len(s2)
while x != 0 and y != 0:
    #print(x,y)
    #if left score of matrix is the same as current.
    if matrix[x][y] == matrix[x-1][y]:
        x -= 1
    #if score above of matrix is the same as current.
    elif matrix[x][y] == matrix[x][y-1]:
        y -= 1
    #inserting
    else:
        #print(s1[x-1], s2[y-1])
        if(s1[x-1] == s2[y-1]):
            LCS = s1[x-1] + LCS
            x -= 1
            y -= 1        

print("LCS:",LCS)