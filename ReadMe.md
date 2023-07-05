# Protein Sendary Structure Analysis:
This project is currently comprised of a series of scripts designed to quickly give the user data about the secondary structure of an AA sequence. The main purpose of this project is for me to practise and learn data analysis skills and apply them to a subject that I am interested in. In this case, the subject is proteomics.
## Scripts:
* \*Please note that this project uses the Kyle-Doolittle scale for hydrophobicity values.
* The first few scripts in this project are related to hydrophobicity since it is the most easily quantifiable characteristic of secondary protein structure, and can be used to predict the formation of helixes that may indicated domains that cross the cell membrane.
### getHydrophobicity(AA):
* This function translates single-letter amino acid code (usually from a fasta file) into hydrophobicity values.
* Iterator will be added eventually.
### hydrophobicityPlot(fasta):
* This function takes an amino acid sequence and creates a hydrophobicity plot using pyplot and the getHydrophobicity() function.
* Here is a sample plot of a Cytochrome P450 from Pseudomonas Aeruginosa PAO1.
![Hydrophobicity plot](https://github.com/krulik1/Protein-2ndary-struc-analysis/blob/main/p450_DAO1.svg)
### hydroSeq(fasta):
* This function takes the hydrophobicity data of the fasta sequence and transforms it into bar graph that counts the number of contiguous sequences of same hydrophobicity and organizes them by length.
* The results for the cytochrome P450 suggest that the data is normally distributed:
![Bar Plot](https://github.com/krulik1/Protein-2ndary-struc-analysis/blob/main/p450_DAO1_hydroSeq.png)
