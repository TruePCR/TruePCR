import pandas as pd

def parse(f):
    """parse TruePCR dataset file into a pd.DataFrame"""
    dna = pd.read_csv(f, index_col=[0,1])
    dna = dna.transpose()
    dna.index = [int(s.split(' ')[1]) for s in dna.index]
    dna.index.name = 'cycle'
    return dna
