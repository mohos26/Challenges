# https://leetcode.com/problems/frequency-tracker
# 21.02.2026


class FrequencyTracker: # contest

    def __init__(self):
        self.d = defaultdict(int)
        self.dd = defaultdict(int)

    def add(self, number: int) -> None:
        if self.dd[self.d[number] ]:
            self.dd[self.d[number]] -= 1
        self.d[number] += 1
        self.dd[self.d[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.d[number]:
            self.dd[self.d[number]] -= 1
            self.d[number] -= 1
            self.dd[self.d[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.dd[frequency] > 0


class FrequencyTracker:
    def __init__(self):
        self.count = defaultdict(int)
        self.freq_count = defaultdict(int)

    def add(self, number: int) -> None:
        old_f = self.count[number]
        if old_f > 0:
            self.freq_count[old_f] -= 1

        self.count[number] += 1
        new_f = self.count[number]
        self.freq_count[new_f] += 1

    def deleteOne(self, number: int) -> None:
        if self.count[number] > 0:
            old_f = self.count[number]
            self.freq_count[old_f] -= 1

            self.count[number] -= 1
            new_f = self.count[number]
            if new_f > 0:
                self.freq_count[new_f] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0
