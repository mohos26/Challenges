with open('/tmp/input.txt') as file:
    total = 0
    for line in file:
        line = line.strip()
        if not line:
            continue

        digits = [int(c) for c in line]

        first = max(digits)
        idx = digits.index(first)

        if idx == len(digits) - 1:
            first, second = max(digits[:-1]), first
        else:
            second = max(digits[idx + 1:])

        total += first * 10 + second

    print(total)
