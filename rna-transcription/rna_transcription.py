def to_rna(dna_strand):
    rna_strand = ""
    if dna_strand == "":
        return rna_strand
    else:
        for i in range(0, len(dna_strand)):
            if dna_strand[i] == "C":
                rna_strand += "G"
            elif dna_strand[i] == "G":
                rna_strand += "C"
            elif dna_strand[i] == "T":
                rna_strand += "A"
            elif dna_strand[i] == "A":
                rna_strand += "U"           
    return rna_strand
