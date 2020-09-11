from collections import defaultdict

"""
Formula -> Molecule Formula | e
Molecule -> ( Element | "(" Formula ")" ) [ Number ]
"""

class Solution:
    def char(self, inc=0):
        if self.i >= len(self.formula):
            return ''
        c = self.formula[self.i]
        self.i += inc
        return c
    
    def parse_count(self):
        n = 0
        while self.char().isdigit():
            n = 10 * n + int(self.char(1))
        return n if n != 0 else 1
    
    def parse_element(self):
        atom = self.char(1)
        assert atom.isupper()
        
        while self.char().islower():
            atom += self.char(1)
        return atom
    
    def countOfAtoms(self, formula: str) -> str:    
        self.formula = formula
        self.i = 0
        
        stack = [defaultdict(int)]
        expecting_count = False
        
        while self.i < len(self.formula) or expecting_count:
            #print(stack)
            
            if expecting_count:
                expecting_count = False
                
                count = self.parse_count()
                molecule = stack.pop()
                
                # multiply current molecule by count suffix
                for k in molecule:
                    molecule[k] *= count
                    
                # sum with previous molecules
                for k, v in molecule.items():
                    stack[-1][k] += v
                
                continue
                
            c = self.char()
                
            if c == '(':
                stack.append(defaultdict(int))
                self.i += 1
                continue
            
            if c.isupper():
                atom = self.parse_element()
                stack.append(defaultdict(int, ((atom, 1), )))
                expecting_count = True
                continue
                
            if c == ')':
                expecting_count = True
                self.i += 1
                continue
        
        assert len(stack) == 1
        
        s = ''
        for k, v in sorted(stack[0].items()):
            s += k + (str(v) if v > 1 else '')
        
        return s
            
