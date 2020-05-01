#!/usr/bin/env python3


"""
dpda.txt structure:
 Line 1: the states of the DPDA (separated by commas, if there is more than one state)
 Line 2: the alphabet of the DPDA (separated by commas, if there is more than one symbol)
 Line 3: the alphabet of the stack
 Line 4: the starting state of the DPDA
 Line 5: the final/accept states of the DPDA (separated by commas, if there is more than one accept state)
 Line 6 and onward: the transition rules, where each rule takes the form a,b,c,d,e (where being in state a and reading symbol b while popping c from the top of the stack transitions to new state d and pushes e on the top of the stack)
In addition to the given alphabet, all DPDAs may also contain empty-string transitions for either the input character, the symbol at the top of the stack, or both (we will use @ to represent this).

Algorithm:
    1. read in file dpda.txt
    2. collect the start and final state from line 4 & 5
    3. from line 6 and onward: divide into a 3-tuple and 2-tuple
    4. 3-tuple (curr_state, input, top_stack): if in curr_state, and next symbol from process_list = input, and top_stack matches top of the stack, execute 2-tuple
    5. 2-tuple (new_state, elt). Record the new state, push elt to the stack
    6. At the end of the input file, check with the list of final states

Different cases of the input and stack:
    case 1: input and top of stack both match
    case 2: input matches but top of stack does not
    case 3: input does not match but top of stack does
    case 4: neither input or top of stack matches

**line 6 will always be the form (init_state, @, @, curr_state, stack symbol)**
"""


def open_file(filename):
    file = open(filename, "r")
    content = file.readlines()
    file.close()
    return content


def process_str(stack, init_state, string, dictionary):
    """
    :param stack: the stack in DPDA
    :param init_state: initial state given by the DPDA rules
    :param string: input string to process
    :param dictionary: contains key and value. Key is the 3-tuple, value is the 2-tuple
    :return:
    """
    initial_tuple = dictionary.get((init_state, '@', '@'))
    curr_state = initial_tuple[0]
    stack_symbol = initial_tuple[1]
    stack.append(stack_symbol)

    length = len(string)
    counter = 0
    # counter only increments if the input character is read (case 1, 2, 4)
    while counter < length:
        top_stack = stack[-1]

        # case 1
        if dictionary.get((curr_state, string[counter], top_stack)) is not None:
            temp_tuple = dictionary.get((curr_state, string[counter], top_stack))
            # print("all match:", temp_tuple)
            stack.pop()
            curr_state = temp_tuple[0]
            # push the stack only if it's not empty
            if temp_tuple[1] != '@':
                stack.append(temp_tuple[1])
            counter += 1

        # case 2
        # by definition case 2 does not pop the element off the stack
        elif dictionary.get((curr_state, string[counter], '@')) is not None:
            temp_tuple = dictionary.get((curr_state, string[counter], '@'))
            # print("no pop:", temp_tuple)
            curr_state = temp_tuple[0]
            if temp_tuple[1] != '@':
                stack.append(temp_tuple[1])
            counter += 1

        # case 3
        # no inputs are read therefore counter does not increase
        elif dictionary.get((curr_state, '@', top_stack)) is not None:
            temp_tuple = dictionary.get((curr_state, '@', top_stack))
            # print("no input:", temp_tuple)
            stack.pop()
            curr_state = temp_tuple[0]
            if temp_tuple[1] != '@':
                stack.append(temp_tuple[1])

        # case 4
        else:
            return -1

#        print("curr_state:", curr_state)
#        print("top stack:", stack[-1])
    # At this point if all left is the stack symbol, then set curr_state from the 2-tuple
    if dictionary.get((curr_state, '@', stack[-1])) is not None:
        temp_tuple = dictionary.get((curr_state, '@', stack_symbol))
        curr_state = temp_tuple[0]

    return curr_state


def print_result(file, result_list, final_states):
    counter = 1
    for i in result_list:
        if counter != len(result_list):
            if i in final_states:
                file.write("accept\n")
            else:
                file.write("reject\n")
        else:
            if i in final_states:
                file.write("accept")
            else:
                file.write("reject")
        counter += 1


def main():
    dpda = open_file("dpda.txt")
    start_state = ""
    final_states = []
    action_dictionary = {}
    counter = 0
    # read in dpda.txt, extract information
    for line in dpda:
        line = line.strip()
        if counter == 3:
            start_state = line
        elif counter == 4:
            final_states = line.split(",")
        elif counter > 4:
            temp = line.split(",")
            # print(temp)
            action_dictionary[(temp[0], temp[1], temp[2])] = (temp[3], temp[4])

        counter += 1

    # print("start:", start_state)
    # print("final:", final_states)
    # print("actions:", action_dictionary)

    # read in input.txt and extract the strings to be processed
    trans_states = open_file("input.txt")
    transition = []
    for line in trans_states:
        line = line.strip()
        transition.append(line)

    # write the result of dpda to the list and compare to final states
    result_list = []
    stack = []
    cout = 1
    for i in transition:
#        print(cout)
        # method call to process each input string
        result_list.append(process_str(stack, start_state, i, action_dictionary))
        cout += 1
#    print(result_list)

    # write the result of the comparison file in output.txt
    output = open("output.txt", "w+")
    print_result(output, result_list, final_states)
    output.close()


main()
