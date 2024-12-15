from Course_Schedule import Solution


class Trie:
    def __init__(self, ch: chr, is_end=False):
        self.ch = ch
        self.is_end = is_end
        self.children = dict()


class PrefixTree:

    def __init__(self):
        self.root = Trie('_', False)

    def insert(self, word: str) -> None:
        if not word:
            return
        root = self.root
        for index, ch in enumerate(word):
            if ch not in root.children:
                root.children[ch] = Trie(ch)

            root = root.children[ch]
            if index == len(word) - 1:
                root.is_end = True

    def search(self, word: str) -> bool:
        if not word:
            return False
        root = self.root
        for index, ch in enumerate(word):
            if ch not in root.children:
                return False

            root = root.children[ch]
            if index == len(word) - 1 and not root.is_end:
                return False

        return True

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        root = self.root
        for index, ch in enumerate(prefix):
            if ch not in root.children:
                return False

            root = root.children[ch]

        return True


if __name__ == "__main__":
    solution = Solution()
    prefixTree = PrefixTree()

    prefixTree.insert("dog")
    print(prefixTree.search("dog"))  # return true
    print(prefixTree.search("do"))  # return false
    print(prefixTree.startsWith("do"))  # return true
    prefixTree.insert("do")
    print(prefixTree.search("do"))  # return true
