def longest_repeating_character_replacement(s, k):
    i = 0
    longest = 0
    while i < len(s):
        subs = s[i]
        skipped = 0
        for c in s[i+1:]:
            if c == subs[0]:
                subs += c
            elif skipped < k:
                skipped += 1
                subs += c
            else:
                break
        length = len(subs)
        if skipped < k:
            length += min(i, k-skipped)
        if length > longest:
            longest = length
        i += 1
    return longest
