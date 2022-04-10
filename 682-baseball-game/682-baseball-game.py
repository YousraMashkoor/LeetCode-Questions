class Solution:
    def calPoints(self, ops: List[str]) -> int:
        self.scores = []
        self.size = 0
        self.total = 0
        
        def add():
            s = self.scores[self.size-1] + self.scores[self.size-2]
            self.scores.append(s)
            self.total +=s
            self.size += 1
        
        def double():
            s = self.scores[self.size-1]*2
            self.scores.append(s)
            self.size +=1
            self.total += s
            
            
        def remove():
            e = self.scores.pop()
            self.size = self.size - 1
            self.total -= e
            
        for op in ops:
            
            if op == '+':
                add()
            elif op == 'D':
                double()
            elif op =='C':
                remove()
            else:
                op = int(op)
                self.scores.append(op)
                self.size +=1
                self.total += op
        return self.total