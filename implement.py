import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.end_of_word = True
    
    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.end_of_word
    
    def starts_with_prefix(self, prefix: str) -> list:
        current_node = self.root
        prefix_nodes = []
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]
            prefix_nodes.append(current_node)
        words = []
        self._traverse(prefix, current_node, words)
        return words
    
    def _traverse(self, prefix: str, node: TrieNode, words: list):
        if node.end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            self._traverse(prefix + char, child_node, words)
            

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words



trie = Trie()
words=load_words()
for word in words:
    trie.insert(word)

while True:
    str=input()
    print(sorted(trie.starts_with_prefix(str),key=len))

