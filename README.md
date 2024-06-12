# Magnum Opus: In-Silico PCR and Sequence Alignment

This repository contains parts one and two of the Python package `magnumopus` which performs in-silico PCR (isPCR) and sequence alignment using the Needleman-Wunsch algorithm. This project is developed as part of the BIOL 7200 Programming for Bioinformatics course at Georgia Tech.

## Overview

The `magnumopus` package includes functionalities for:
1. **In-Silico PCR (isPCR)**: Simulates the Polymerase Chain Reaction (PCR) process to amplify target DNA sequences.
2. **Needleman-Wunsch Algorithm**: Performs global sequence alignment.


## Prerequisites and Dependencies

- Python 3.10 or later
- Required Python packages: `numpy`, `pandas`
  ```bash
  pip install numpy pandas

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Magnum-Opus.git
   cd Magnum-Opus

## Directory Layout
```bash
.
├── magnumopus_pt1
│   ├── blast_output.txt
│   ├── data
│   │   ├── Vibrio_cholerae_N16961.fna
│   │   └── general_16S_515f_806r.fna
│   ├── ispcr
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── extraction_sequences.cpython-311.pyc
│   │   │   ├── primerAnnealing.cpython-311.pyc
│   │   │   └── sort_blastn_results.cpython-311.pyc
│   │   ├── extraction_sequences.py
│   │   ├── primerAnnealing.py
│   │   └── sort_blastn_results.py
│   ├── q1.py
│   ├── q2.py
│   ├── q3.py
│   └── sdiskalkar3.tar.gz
├── Diskalkar_Solution_p1.tar.gz
├── magnumopus_pt2
│   ├── amplicon_align.py
│   ├── data
│   │   ├── Pseudomonas_aeruginosa_PAO1.fna
│   │   ├── Pseudomonas_protegens_CHA0.fna
│   │   └── rpoD.fna
│   ├── magnumopus
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── combinedispcr.cpython-311.pyc
│   │   │   ├── combinedispcr.cpython-37.pyc
│   │   │   └── nw.cpython-311.pyc
│   │   ├── combinedispcr.py
│   │   ├── nw.py
│   │   └── oldpcr.py
│   ├── q1.py
│   └── q2.py
├── Diskalkar_Solution_p2.tar.gz
├── Instructions_p1.pdf
├── Instructions_p2.pdf
└── README.md
```
## Contact
If you have any questions or suggestions, feel free to contact me at sarthd@gmail.com.
