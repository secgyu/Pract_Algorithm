def solution(before, after):
    sort_before = ''.join(sorted(before))
    sort_after = ''.join(sorted(after))
    if sort_before == sort_after:
        return 1
    else:
        return 0