# Author: krulik1
# Date: 2023-08-10

# Purpose: 
# This code is meant to transform the data
# from the dataset chosen for this project.
# *note, the dataset is included in this repository for easy access.

# Dataset:
# Sejnowski,Terry and Qian,Ning. Molecular Biology
# (Protein Secondary Structure). UCI Machine Learning
# Repository. https://doi.org/10.24432/C5SP4F.

## Data preparation scripts for ANN:
structure_val = {
    '_': 0,
    'e': 1,
    'h': 2
}    
    
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

def getSecondaryStructure(struc):
    if struc in structure_val:
        return structure_val.get(struc, None)
    return struc

def getHydrophobicity(aa):
    if aa in hydrophobicity_values:
        return hydrophobicity_values.get(aa, None)
    return aa

def startswith(input_string, dictionary):
    for key in dictionary:
        if input_string.startswith(key):
            return True
    return False

def cleanData(input_file, output_file):
    clean = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("#"):
                continue
            elif line.startswith("<"):
                clean.append(line)
            elif line.startswith("e"):
                clean.append(line)
            elif startswith(line, hydrophobicity_values):
                t = line.split()
                hydrophobicity = getHydrophobicity(t[0])
                structure = getSecondaryStructure(t[1])
                clean.append(f"{hydrophobicity} {structure}\n")
    
    with open(output_file, 'w') as f:
        f.writelines(clean)

# replace with filepath to data to clean:
input_file = input() 
output_file = input()
