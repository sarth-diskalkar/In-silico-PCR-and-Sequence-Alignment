#!/usr/bin/env python3

import argparse
from magnumopus import ispcr
from magnumopus import needleman_wunsch

def get_reverse_complement(sequence):
    base_complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([base_complements[nuc] for nuc in reversed(sequence)])

def strip_fasta_header(fasta_str):
    return ''.join(line for line in fasta_str.strip().split('\n') if not line.startswith('>'))

def process_sequences(input_args):
    amplicon_seq1 = ispcr(input_args.p, input_args.assembly1, input_args.m)
    amplicon_seq2 = ispcr(input_args.p, input_args.assembly2, input_args.m)

    clean_seq1 = strip_fasta_header(amplicon_seq1)
    clean_seq2 = strip_fasta_header(amplicon_seq2)

    align_outcome, align_score = needleman_wunsch(clean_seq1, clean_seq2, input_args.match, input_args.mismatch, input_args.gap)

    clean_seq2_rc = get_reverse_complement(clean_seq2)
    reverse_align_outcome, reverse_align_score = needleman_wunsch(clean_seq1, clean_seq2_rc, input_args.match, input_args.mismatch, input_args.gap)

    if reverse_align_score > align_score:
        align_outcome = reverse_align_outcome
        align_score = reverse_align_score

    print(f"\n{align_outcome[0]}\n{align_outcome[1]}\n#score:\n{align_score}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform in-silico PCR on two assemblies and align the amplicons')
    parser.add_argument('-1', dest='assembly1', required=True, metavar='ASSEMBLY1', help='Path to the first assembly file')
    parser.add_argument('-2', dest='assembly2', required=True, metavar='ASSEMBLY2', help='Path to the second assembly file')
    parser.add_argument('-p', required=True, metavar='PRIMERS', help='Path to the primer file')
    parser.add_argument('-m', type=int, required=True, metavar='MAX_AMPLICON_SIZE', help='Maximum amplicon size for isPCR')
    parser.add_argument('--match', type=int, required=True, metavar='MATCH', help='Match score to use in alignment')
    parser.add_argument('--mismatch', type=int, required=True, metavar='MISMATCH', help='Mismatch penalty to use in alignment')
    parser.add_argument('--gap', type=int, required=True, metavar='GAP', help='Gap penalty to use in alignment')

    args = parser.parse_args()
    process_sequences(args)
