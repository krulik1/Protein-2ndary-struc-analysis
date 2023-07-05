# Hydrophobicity Analysis Scripts
# Author: Jakub Krulik

# This program inputs a single-protein fasta file,
# plots the hydrophibicity of the individual AAs using matplotlib,
# counts the number of contiguous hydrophobic or hydrophilic AAs,
# and displays this data in a bar chart.

# NOTE* Hydrophobicity scale: kyle-doolittle scale
import matplotlib.pyplot as plt


# Sample Data: (seq can be any protein sequence)
# - AA sequence obtained from ncbi genbank database
# - NP_251165.1 cytochrome P450 [Pseudomonas aeruginosa PAO1]
# - https://www.ncbi.nlm.nih.gov/assembly/GCF_000006765.1/
# - sample output can be 
seq = "MDDAFSEEGSAQPRHDAQRPALAPRSDGFDIHTYHPDFVADPYPLLRLIRSRAPVCRDQASIWWISRYADVSACLRDRRFSADPARLGAAGVRQGGASWFGHQQLQPLARFYDNFMLFNDAPRHTRLRRLFAPAFGPDAVRRWEARIEVLVEELLDSLLERREPDLLRDFAEPLTIRVAAELFGFPREDTGQLLPWGRDLAAGLDLAASHGDAGQINRSAVAFSDYLQRQARGWSDGSSRPPSGAAPSILDGAAMLEAGLGLEDLVAAYAMVFMAAFETTISMVGNATLALLTHPDQLDLLRRCPELAANAVEELLRFDGAVRGGVRCTLEEVEIGGQRIPPGEKVWLSFLAANRDPEMFAAPDRLQLQRANAKQHVAFAHGPHYCLGAYLARLELQCALRGLVRRRFALASEPTDLRWRRSSVFRTLERLPIVPEGDAQKTCE"

# function that converts single-letter AA code into hydrophobicity values.
def getHydrophobicity(aa):
    hydrophobicity_values = {
        'A': 1.8,
        'R': -4.5,
        'N': -3.5,
        'D': -3.5,
        'C': 2.5,
        'Q': -3.5,
        'E': -3.5,
        'G': -0.4,
        'H': -3.2,
        'I': 4.5,
        'L': 3.8,
        'K': -3.9,
        'M': 1.9,
        'F': 2.8,
        'P': -1.6,
        'S': -0.8,
        'T': -0.7,
        'W': -0.9,
        'Y': -1.3,
        'V': 4.2
    }
    
    return hydrophobicity_values.get(aa.upper(), None)

# Function plots the hydrophobicity of AAs in a linear plot
def hydrophobicityPlot(fasta):
    n = len(fasta)

    hydro = []
    axis = []
    for i in range(0,n,1):
        x = fasta[i]
        hydro.append(getHydrophobicity(x))
        axis.append(i)
        
    plt.figure(figsize=(70,8))
    plt.scatter(axis, hydro)
    plt.plot(axis, hydro)
    plt.savefig('p450_DAO1.svg')


hydrophobicityPlot(seq)    
## Sample data: NP_251165.1 cytochrome P450 [Pseudomonas aeruginosa PAO1]

## NOTES:
# Count the number of regions likely to be membrane crossing helices.
# Method for determining helices??
# - if 20+ AAs are positive, seq might be a helix
# Method for finding Protein domains??

## RESULTS:
# No membrane-crossing helices.
# Maximum hydrophobic sequence length of 8 occuring once
# length of hydrophobic/hydrophilic sequences appears to be normally distributed

# Function counts the number of sequences of contiguous hydrophobic/hydrophilic AAs and categorizes them by length
def hydroSeq(fasta):
    n = len(fasta)
    hydro = []
    hydrophobicSeq = []
    aaCount = 0

    # Translates the AA sequence into hydrophobicity values
    for i in range(0,n,1):
        x = fasta[i]
        hydro.append(getHydrophobicity(x))

    # Counts the number of consecutive hydrophobic and hydrophilic AAs in the order that they occur in the AA sequence
    for i in range(0,n,1):
        if hydro[i] > 0:
            aaCount = aaCount + 1
            if i != len(hydro):
                if hydro[i+1] < 0:
                    hydrophobicSeq.append(aaCount)
                    aaCount=0
        elif hydro[i] < 0:
            if i == len(hydro)-1:
                aaCount = aaCount-1
                hydrophobicSeq.append(aaCount)
            elif hydro[i+1]>0:
                aaCount = aaCount-1
                hydrophobicSeq.append(aaCount)
                aaCount = 0
            else:
                aaCount = aaCount-1

    # Prints the lengths of sequences in the order that they occur           
    print(hydrophobicSeq)
    
    numberAA = set(hydrophobicSeq)
    numberAA = list(numberAA)
    numberAA.sort()
    print(numberAA)
    numberSeq = []

    # Counts the number of sequences at different lengths
    for i in range (0,len(numberAA),1):
        numberSeq.append(hydrophobicSeq.count(numberAA[i]))
    # print("numberSeq: " + str(len(numberSeq))+" numberAA: " + str(len(numberAA)))
    
    plt.figure(figsize=(100,50))
    plt.title("Length of Hydrophobic and Hydrophilic Sequences",fontsize=80)
    plt.xlabel("Sequence Length (negative-hydrophilic, positive-hydrophobic)",fontsize=80)
    plt.ylabel("Number of sequences",fontsize=80)
    
    plt.xticks(numberAA, fontsize=80)
    plt.yticks(fontsize=80)
    plt.grid(axis = 'y')
    plt.bar(numberAA,numberSeq)
    plt.show()
    
hydroSeq(seq)
