class Input_Trie:
    counter = 0
    def __init__(self):
        self.str = {}
        Input_Trie.counter += 1
        self.count = Input_Trie.counter

def lists(input_string):
    root_node = Input_Trie()
    for index, value in enumerate(input_string, 1):
        present = root_node
        for j in value:
            if j not in present.str:
                present.str[j] = Input_Trie()
            present = present.str[j]
    return root_node

def solution_format(root_node, solution=[]):
    for index in root_node.str:
        solution.append((root_node.count, root_node.str[index].count, index))
        solution_format(root_node.str[index], solution)
    return solution

with open('rosalind_trie.txt') as data:
    input_string = data.read().splitlines()
root_node = lists(input_string)
sentence = 0

for index in solution_format(root_node):
    solution = ' '.join(map(str, index))
    print(solution)
    sentence += 1
