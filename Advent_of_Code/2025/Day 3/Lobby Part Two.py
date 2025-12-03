with open('/tmp/input.txt') as file:
    total = 0

    for line in file:
        line = line.strip()
        if not line:
            continue

        digits = [int(c) for c in line]
        result = 0

        for picked in range(12):
            search_end = len(digits) - (12 - picked - 1)

            max_digit = max(digits[:search_end])
            idx = digits.index(max_digit)

            result = result * 10 + max_digit
            digits = digits[idx + 1:]

        total += result

    print(total)

