# Keywords
# dictionary - words are nodes
# shortest - BFS
# transformed sequence - path

# Steps
# load words
# make graph
# traverse it - run bfs
# parse result in correct formatted
# return result

# Load words
f = open("words.txt", "r")
words = f.read().split("\n") # read list of new words and give us python list
f.close()

# create new set with all the words from list lower case
word_set = set()
for word in words:
    word_set.add(word.lower())

# Get Neighbors
def get_neighbors(word):
    neighbors = []
    string_word = list(word) # turns word into a list of its chars
    # loop through string_word
    # change each letter to letter
    # check if it's a word in provided file
    for i in range(len(string_word)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(string_word) # creating copy to mutate
            temp_word[i] = letter
            w = "".join(temp_word)

            if w != word and w in word_set: # w doesn't match original word, and is in word_set
                neighbors.append(w)

    return neighbors


# Instantiate Queue
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Run Our Search
def find_word_ladder(beginWord, endWord):
    visited = set()
    q = Queue()
    q.enqueue([beginWord]) # enqueue it as a list to save as path

    while q.size():
        path = q.dequeue() # which will be a list
        v = path[-1] # last item in list

        if v not in visited:
            visited.add(v)
            if v == endWord:
                return path
            #else
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)



print(find_word_ladder("cool", "bean"))