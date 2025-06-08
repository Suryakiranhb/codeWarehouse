#TRIEs

#lets create a trie
#creating a trie node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False # True if the node represents the end of a word

#creating a trie class
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode() #creating a new node if the starting letter doesnt exist yet
            node = node.children[char]  #move to the child node 
        node.end_of_word = True 

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def starts_with(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # prefix does not exist
            node = node.children[char]
        return True

trie = Trie()
trie.insert("cat")
trie.insert("cap")
trie.insert("can")

print(trie.search("cat"))
print(trie.search("car"))
print(trie.starts_with("ca"))
print(trie.starts_with("cb"))

# True False True False

# DRY RUN
# First, a class is initialized, called TrieNode which has a set called children in it, and a bool var called end_of_word. This is used to define if the word is complete or not.
# Now, we initialize the class with a variable trie. To it, we insert the word cat. What this does is, it goes into the trie's TrieNode instance's insert method, and in that it loops through each character in the word cat.
# For the word 'c', it checks if its in the children set. it wont be. so it stores it in the chilren set. it goes to the next character, 'a'. again it goes and checks if the children set has 'a' in it or not 
# It wont be there. it will store it in children set. Then the same thing happens with the character 't'. Note that each time, a TrieNode is created. Since none of these letters already exist.
# Now, coming to the insert of the word 'cap', initially it goes into the same instance's insert function to insert 'c'. But now, the if condition fails because 'c' is already existing in children set. It now navigates to where it exists. 
# From the next iteration, we get the character 'a'. This also exists in the children set. It now navigates to where it exists. 
# From the next iteration, we get the character 'p'. But this time, 'p' does not exist. So now, we create a new node for 'p' and store it in the children set of 'a'. This is how we insert cap. the same thing happens for the word 'can', but this time, in a's node, we store another node called 'n', just like we did for 'p'.
# Now suppose we need to insert a word called 'captain', here, it will go to 'c' node, then to 'a' node then to 'p' node. but now it will encounter a new letter called 'a'. Now instead of using the 'a' root node from earlier, it will create a new node under 'p', called 't'.

# Mental model
# A Trie is a tree where each path from root to a node represents a prefix.
# children is a dict mapping characters → TrieNode.
# We reuse nodes when the prefix already exists, and create new ones only when necessary.
# At the last node of the word, we set end_of_word = True.