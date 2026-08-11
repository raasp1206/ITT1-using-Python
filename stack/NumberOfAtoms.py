class Solution(object):
    def countOfAtoms(self, formula):
        stack = [{}]
        i = 0
        n = len(formula)
        while i < n:
            if formula[i] == '(':
                stack.append({})
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i]) if start < i else 1
                top_map = stack.pop()
                for atom, count in top_map.items():
                    stack[-1][atom] = stack[-1].get(atom, 0) + (count * multiplier)
          
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                atom_count = int(formula[start:i]) if start < i else 1
                stack[-1][atom] = stack[-1].get(atom, 0) + atom_count
        final_map = stack[0]
        sorted_atoms = sorted(final_map.keys())
        
        res = []
        for atom in sorted_atoms:
            res.append(atom)
            if final_map[atom] > 1:
                res.append(str(final_map[atom]))
                
        return "".join(res)
