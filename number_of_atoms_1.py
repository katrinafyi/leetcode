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
    
    def parse_molecule(self):
        #print(self.formula[self.i:])
        if self.char() == '(':
            self.i += 1
            atoms = self.parse_formula()
        else:
            atoms = {self.parse_element(): 1}
            
        count = self.parse_count()
        for k in atoms:
            atoms[k] *= count

        return atoms
    
    def parse_formula(self):
        c = self.char()

        if c != '' and c != ')':
            formula = self.parse_molecule()
            for k, v in self.parse_formula().items():
                if k not in formula: formula[k] = 0
                formula[k] += v
            return formula
        
        if c == ')':
            self.i += 1
        return {}
    
    def countOfAtoms(self, formula: str) -> str:        
        self.formula = formula
        self.i = 0
        
        s = ''
        for k, v in sorted(self.parse_formula().items()):
            s += k + (str(v) if v > 1 else '')
        return s
            
