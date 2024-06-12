#!/usr/bin/env python3

import magnumopus

primer_file = "data/rpoD.fna"
assembly = "data/Pseudomonas_aeruginosa_PAO1.fna"
max_amp_size = 2000

amplicons = magnumopus.ispcr(primer_file, assembly, max_amp_size)

print(amplicons)
