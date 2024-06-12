#!/usr/bin/env python3
import subprocess

def run_blastn(primer_file, assembly_file):
    output_file = "blast_output.txt"
    command = [
        "blastn",
        "-task", "blastn-short",
        "-query", primer_file,
        "-subject", assembly_file,
        "-outfmt", "6 std qlen",
        "-out", output_file
    ]
    subprocess.run(command)
    return output_file

def process_blast_output(output_file):
    results = []
    with open(output_file, 'r') as file:
        for line in file:
            fields = line.strip().split('\t')
            percent_identity = float(fields[2])
            alignment_length = int(fields[3])
            query_length = int(fields[-1])
            if percent_identity >= 80.0 and alignment_length == query_length:
                results.append(fields)
    return results
def sort_blast_results(results):
    #sorts the hits
    return sorted(results, key=lambda x: int(x[8]))

def step_one(primer_file: str, assembly_file: str) -> list[list[str]]:
    output_file_blast = run_blastn(primer_file, assembly_file)
    hits = process_blast_output(output_file_blast)
    sorted_hits = sort_blast_results(hits)
    return sorted_hits