#!/usr/bin/env python3
def step_two(sorted_hits: list[str], max_amplicon_size: int) -> list[tuple[list[str]]]:
    hit_pairs = []
    for idx1 in range(len(sorted_hits)):
        for idx2 in range(idx1+1, len(sorted_hits)):
            if idx1 == idx2:
                continue

            hit1 = sorted_hits[idx1]
            hit2 = sorted_hits[idx2]

            start_hit1, end_hit1 = int(hit1[8]), int(hit1[9])
            start_hit2, end_hit2 = int(hit2[8]), int(hit2[9])

            dir_hit1 = "right" if start_hit1 < end_hit1 else "left"
            dir_hit2 = "right" if start_hit2 < end_hit2 else "left"

            if dir_hit1 == dir_hit2:
                continue

            if dir_hit1 == "right" and dir_hit2 == "left" and start_hit1 < start_hit2:
                gap = start_hit2 - end_hit1
            elif dir_hit1 == "left" and dir_hit2 == "right" and start_hit1 > start_hit2:
                gap = start_hit1 - end_hit2
            else:
                continue

            if 0 < gap <= max_amplicon_size:
                hit_pairs.append((hit1, hit2))

    return hit_pairs

