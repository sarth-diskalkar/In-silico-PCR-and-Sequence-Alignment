#!/usr/bin/env python3

def needleman_wunsch(seq_a: str, seq_b: str, match: int, mismatch: int, gap: int) -> tuple[tuple[str, str], int]:
    n = len(seq_a)
    m = len(seq_b)
    score_matrix = [[0] * (m+1) for _ in range(n+1)]
    traceback_matrix = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        score_matrix[i][0] = gap * i
        traceback_matrix[i][0] = 'U'
    for j in range(1, m+1):
        score_matrix[0][j] = gap * j
        traceback_matrix[0][j] = 'L'

    for i in range(1, n+1):
        for j in range(1, m+1):
            match_score = score_matrix[i-1][j-1] + (match if seq_a[i-1] == seq_b[j-1] else mismatch)
            delete = score_matrix[i-1][j] + gap
            insert = score_matrix[i][j-1] + gap
            score_matrix[i][j] = max(match_score, delete, insert)

            if score_matrix[i][j] == match_score:
                traceback_matrix[i][j] = 'D'
            elif score_matrix[i][j] == delete:
                traceback_matrix[i][j] = 'U'
            else:
                traceback_matrix[i][j] = 'L'

    
    align_a, align_b = '', ''
    i, j = n, m
    while i > 0 or j > 0:
        if traceback_matrix[i][j] == 'D':
            align_a = seq_a[i-1] + align_a
            align_b = seq_b[j-1] + align_b
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == 'U':
            align_a = seq_a[i-1] + align_a
            align_b = '-' + align_b
            i -= 1
        elif traceback_matrix[i][j] == 'L':
            align_a = '-' + align_a
            align_b = seq_b[j-1] + align_b
            j -= 1

    alignment_score = score_matrix[n][m]

    return (align_a, align_b), alignment_score
