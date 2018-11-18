def shortest_path(word1, word2, words):
    if (len(word1) != len(word2)):
        return -1
    visited = set()
    parent_dict = {}
    current_layer = [word1]
    depth = 0
    while current_layer:
        temp_layer = []
        for it in current_layer:
            if it == word2:
                while parent_dict[word2]:
                    word2 = parent_dict[word2] 
                    print(word2)
                return depth                
            visited.add(it)
            diff = words[it] - visited
            temp_layer.extend(diff)  #[w for in words[cw] if w not in visited]
            for i in diff:
                parent_dict[i] = it
        depth += 1    
        current_layer = temp_layer               
    #return path #list of words
    return -1

words = {'cat' : set(['cut']), 
        'cut': set(['but']), 
        'but' : set(['bug']), 
        'bug': set(['big']) }
print(shortest_path('cat', 'big', words))