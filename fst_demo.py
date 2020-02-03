
# Python class for finite-state transducer (FST)
# i_alpha: set of input alphabet symbols
# o_alpha: set of output alphabet symbols
# states: set of states
# start: initial state
# finals: set of final states
# transitions: dictionary of transitions; keys are (state, input) pairs and values are (state, output) pairs

class FST:
    def __init__(self, i_alpha, o_alpha, states, start, finals, transitions):
        self.Sigma = i_alpha
        self.Gamma = o_alpha
        self.Q = states
        self.I = start
        self.F = finals
        self.delta = transitions

    # helper function that returns the transition for state q and input symbol i. If no such transition exists, returns (None, None)
    def get_trans(self, q, i):
        return self.delta.get((q, i), (None, None))

    # takes an input string s and returns the corresponding output string, or None if the FST isn't defined for s
    def get_output_string(self, s):
        output = ''
        state = self.I
        for c in s:
            state, next_output = self.get_trans(state, c)
            if state:
                output = output + next_output
            else:
                return None
        return output


def demo():
    T = FST(set(['a', 'b']), set(['a', 'b']), set([0, 1]), 0, set([0, 1]),
            {(0, 'a'): (1, 'b'), (0, 'b'): (1, 'b'), (1, 'a'): (1, 'a'), (1, 'b'): (1, 'b')})
    print 'Input: aaa Output:', T.get_output_string('aaa')
    print 'Input: bbb Output:', T.get_output_string('bbb')
    print 'Input: a Output:', T.get_output_string('a')
    print 'Input: aba Output:', T.get_output_string('aba')
    print 'Input: ccc Output:', T.get_output_string('ccc')


if __name__ == '__main__':
    demo()