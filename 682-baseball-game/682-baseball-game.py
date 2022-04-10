class Solution:
    def calPoints(self, ops: List[str]) -> int:
        self.scores = []
        self.size = 0
        self.total = 0


        for op in ops:
            
            if op == '+':
                s = self.scores[self.size-1] + self.scores[self.size-2]
                self.scores.append(s)
                self.total +=s
                self.size += 1
            elif op == 'D':
                s = self.scores[self.size-1]*2
                self.scores.append(s)
                self.size +=1
                self.total += s
            elif op =='C':
                e = self.scores.pop()
                self.size = self.size - 1
                self.total -= e
            else:
                op = int(op)
                self.scores.append(op)
                self.size +=1
                self.total += op
        return self.total