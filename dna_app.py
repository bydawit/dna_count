import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-logo.png')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition if query DNA!

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
