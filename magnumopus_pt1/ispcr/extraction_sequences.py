#!/usr/bin/env python3
import subprocess
import tempfile

def step_three(hit_pairs: list[tuple[list[str]]], assembly_file: str) -> str:
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file_obj:
        for pair_item in hit_pairs:
            sequence_contig = pair_item[0][1]
            sequence_start = pair_item[0][9]
            sequence_stop = str(int(pair_item[1][9]) - 1)
            temp_file_obj.write(f"{sequence_contig}\t{sequence_start}\t{sequence_stop}\n")
    
    bed_filepath = temp_file_obj.name

    seqtk_cmd = ["seqtk", "subseq", assembly_file, bed_filepath]
    seqtk_result = subprocess.run(seqtk_cmd, capture_output=True, text=True)

    # Return the output from seqtk
    return seqtk_result.stdout
