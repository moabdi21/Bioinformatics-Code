#DNA string
s = "TACAGGGAAGGTGCTACTAATATCGTCACGAGTCGGACAAGTGATGGGTCTCGAGAACCTTAGACAAATTATACATATACCGGATTAACATCCCTTCATCCCCTACTCTGTGGTATGGTACTCTTGAGTAGATCATCTTGCAACGTATCAGCTCCACCCTTGCCCGTATATGCAGGACAGGCGACAGTTGCTAACTCCCGTCAGAGAGCCCCGTTAGAGGTCATGACAGTTTTGAGGAGTACTGGGCTTACCAATGACTGGCCGCGGCGCTTTGAAACATTATATAACGATAGCCGTGACCCACCCTCTTCGTAACATGGGCGTGTACACCTACCCGCATCAGCGGACGTATTGAAAATATATGGTCAGAAACGGCTAAAAATTGGGCCGCTGGCCCGCAGGCGCTGAGCTACCGAACACCCGTTCTCCTAATGGAGTGAGTCGTACACCTGTTGAGTATCTTATTGCTTCGATGCCTCGACCGTCTCGCCATCGAAGAGTACTCCCATGGGGAAGACAGGCTGACTCCAATCGAAATGAACTTAGTAAGTAGAATGTATTCATGACCAGGGCCGGTAACACTTCAGGGTCTATAGCGTAGCCTACCGAGAATTAACCAATAGGAGCTCTTACGACGTCTTATATAGTCTATGGTACCTCAGTACCGGTAACTCCTTGTTGTTGGTACGCTCCGAAACTCCTTAGTAAGTTCATGGTTGCCTCGGGATGGCCGGAATGACGACGTCCGTTGGAATTTGTGGGCGCAACTGGCATGTTGTGAGCAAGCGTCTACTTGTTGCGTAATCTATGGAACACTAACTGAGGACTAGCCAGTCATCGCTAACGGCCAACAAATTAACCTGATGACAGTAGATTATTATTGGTTATGAATGACCATTACAGAGCGGTCTATGTGTCCAATTACGG";

#datasets
a = 0;
c = 0;
g = 0;
t = 0;
#reads the string.
for char in s:
    if char == 'A':
        a += 1;
    elif char == 'C':
        c += 1;
    elif char == 'G':
        g += 1;
    elif char == 'T':
        t += 1;
print(a,c,g,t);
