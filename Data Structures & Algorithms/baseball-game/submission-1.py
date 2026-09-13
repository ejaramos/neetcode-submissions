class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # stacks

        res_stack = []
        '''
        An integer x: Record a new score of x.
        '+': Record a new score that is the sum of the previous two scores.
        'D': Record a new score that is the double of the previous score.
        'C': Invalidate the previous score, removing it from the record.
        '''
        for i in range(0, len(operations) ):
            op = operations[i]
            # print(op)
            if op == 'C':
                res_stack.pop()
                continue
            
            if op == '+':
                next_op = int(res_stack[-2]) + int(res_stack[-1])
            elif op == 'D':
                next_op = 2*int(res_stack[-1])
            else:
                next_op = int(op)
                
            # print(next_op)
            res_stack.append(next_op)
        
        # print(res_stack)
        return sum(res_stack)