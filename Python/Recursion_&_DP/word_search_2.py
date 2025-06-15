#word_search_2
#Here, we need to find the path of a word in a grid of letters

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # Store thhe full word when it ends here
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word # Marking the end

def find_words(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    rows,cols = len(board), len(board[0])
    result = set()

    def backtrack(r, c, parent):
        letter = board[r][c]
        current_node = parent.children.get(letter)
        if not current_node:
            return

        if current_node.word:
            result.add(current_node.word)

        #Since we have now found the word, marking the board
        board[r][c] = '#'

        # MOST VITAL BLOCK to check if the next letter is among the neighbouring cells, or not. Based on which further recursion takes place
        for dr,dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <=nr <rows and 0 <=nc <cols and board[nr][nc] in current_node.children:
                backtrack(nr,nc,current_node)
            
        board[r][c] = letter # unmarking 

    for r in range(rows):
        for c in range(cols):
            if board[r][c] in trie.root.children:
                backtrack(r,c,trie.root)
    
    return list(result)

board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]

words = ["oath", "pea", "eat", "rain"]
print(find_words(board, words))  # ['oath', 'eat']


