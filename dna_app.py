import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-logo.png')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA Sequence')

sequence_input = "GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = ''.join(sequence)
st.write("""
***
""")

# DNA nucleotide count
st.header('INPUT (DNA QUERY)')
sequence

st.header("OUTPUT (DNA Nucleotide Count)")

st.subheader('1. Count')
def dna_nucleotide_count(seq):
    d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
    ])
    return d


X = dna_nucleotide_count(sequence)
X_lable = list(X)
X_values = list(X.values())
X

st.subheader('2. Description')
st.write('Thre are ' + str(X['A']) + ' adenine (A)')
st.write('Thre are ' + str(X['T']) + ' thymine (T)')
st.write('Thre are ' + str(X['G']) + ' guanine (G)')
st.write('Thre are ' + str(X['C']) + ' cytosine (C)')


st.subheader('3. Dataframe')
df = pd.DataFrame.from_dict(X, orient= 'index')
df = df.rename({0: 'count'}, axis = 'columns')
df.reset_index(inplace = True)
df = df.rename(columns = {'index' : 'nucleotide'})
st.write(df)


st.subheader('4. Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)
p = p.properties(
    width = alt.Step(80)
)
st.write(p)