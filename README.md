# DPDA

Deterministic PushDown Automaton

dpda.py will read in a text file "dpda.txt" and construct a DPDA. Then it reads in "input.txt" to determine whether each input strings can be accepted or not by the DPFA. The result is reflected in output.txt as each line contains the result "accetpt" or "reject" for every line in "input.txt".

Files "dpda.txt", "dpda copy1.txt", "dpda copy2.txt" are different test files for dpda.py. Both test cases produced consisent answers identical to the results from manually contructed DPDAs.

dpda.txt structure:

 Line 1: the states of the DPDA (separated by commas, if there is more than one state)
 
 Line 2: the alphabet of the DPDA (separated by commas, if there is more than one symbol)
 
 Line 3: the alphabet of the stack
 
 Line 4: the starting state of the DPDA
 
 Line 5: the final/accept states of the DPDA (separated by commas, if there is more than one accept state)
 
 Line 6 and onward: the transition rules, where each rule takes the form a,b,c,d,e (where being in state a and reading symbol b while popping c from the top of the stack transitions to new state d and pushes e on the top of the stack)
 
In addition to the given alphabet, all DPDAs may also contain empty-string transitions for either the input character, the symbol at the top of the stack, or both (we will use @ to represent this).
