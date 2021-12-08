filename = 'day8_input.txt'
input = open(filename).read()
data = input.split('\n')
score = 0
for line in data:
    numbers = {}
    patterns = line.split('|')
    signals = patterns[0].split(' ')

    for signal in signals:
        if len(signal) == 2:
            numbers[1] = "".join(sorted(signal))
            signals.remove(signal)
            break
    for signal in signals:
        if len(signal) == 3:
            numbers[7] = "".join(sorted(signal))
            signals.remove(signal)
            break
    for signal in signals:
        if len(signal) == 4:
            numbers[4] = "".join(sorted(signal))
            signals.remove(signal)
            break
    for signal in signals:
        if len(signal) == 7:
            numbers[8] = "".join(sorted(signal))
            signals.remove(signal)
            break
    for signal in signals:
        if len(signal) == 5:
            if numbers[1][0] in signal and numbers[1][1] in signal:
                numbers[3] = "".join(sorted(signal))
                signals.remove(signal)
                break
    for signal in signals:
        if len(signal) == 6:
            cf = 0
            if numbers[1][0] in signal:
                cf += 1
                f = numbers[1][1]
            if numbers[1][1] in signal:
                cf += 1
                f = numbers[1][0]
            if cf == 1:
                numbers[6] = "".join(sorted(signal))
                signals.remove(signal)
                break
    for signal in signals:
        if len(signal) == 6:
            three = 0
            for letter in numbers[3]:
                if letter in signal:
                    three += 1
            if three == 5:
                numbers[9] = "".join(sorted(signal))
                signals.remove(signal)
                break
    for signal in signals:
        if len(signal) == 6:
            numbers[0] = "".join(sorted(signal))
            signals.remove(signal)
            break
    for signal in signals:
        if len(signal) == 5:
            if f in signal:
                numbers[2] = "".join(sorted(signal))
                signals.remove(signal)
                break
    for signal in signals:
        if len(signal) == 5:
            numbers[5] = "".join(sorted(signal))
            signals.remove(signal)
            break

    output = patterns[1].split(' ')
    result = []
    for out in output:
        if out == '':
            continue
        code = "".join(sorted(out))
        for i in range(0, 10):
            if numbers[i] == code:
                result.append(str(i))
    value = int(''.join(result))
    score += value
    print(value)
print(score)



