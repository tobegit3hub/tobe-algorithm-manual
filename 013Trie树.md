
# 实现Trie树

## 什么是Trie树

Trie树是一种树的数据结构，又被称为字典树，非常适用于Ajax自动补全等场景，因为它通过空间换时间能极大提高特别字符串的查询速度。

Tire字典树每条路径都包含一个字母，给定一个单词如“abc”，就可以通过a、b、c三次查询找到是否存在对应的数据，如果给定a、b就可以找到以“ab”开头剩下的字符串，而在叶子节点中包含特殊标志表示存在是否这个单词，因为它也可能只是另一个单词的一部分。

## 如何实现Trie树

首先是定义Trie树的类，内部数据结果其实可以用Python的字典来实现了。

```
class TrieTree(object):

  def __init__(self):
    self.tree = {}

  def add(self, word):
    pass

  def search(self, word):
    pass

tree = TrieTree()
tree.add("abc")
tree.add("bcd")
# Print nothing
print(tree.search("ab"))
# Print None
print(tree.search("abc"))
# Print None
print(tree.search("abcd"))
# Print None
```

然后我们需要实现add函数，首先我们复制一个字典出来，然后是遍历word的所有字母，如果这个字母在字典中有，那么就继续下一个（通过移动字典），如果这个字母在字典中没有那么就加一个，同样继续下一个。注意最后还需要给叶子节点一些特殊的标记，例如多加一个key value。

```
class TrieTree(object):

  def __init__(self):
    self.tree = {}

  def add(self, word):
    tree = self.tree

    for char in word:
      if char in tree:
        tree = tree[char]
      else:
        tree[char] = {}
        tree = tree[char]

    tree['exist'] = True

  def search(self, word):
    pass

tree = TrieTree()
tree.add("abc")
tree.add("bcd")
# Print {'a': {'b': {'c': {'exist': True}}}, 'b': {'c': {'d': {'exist': True}}}}
print(tree.search("abc"))
# Print None
print(tree.search("abc"))
# Print None
print(tree.search("abcd"))
# Print None
```

然后我们还要实现search函数，和前面add非常类似，这时只需要for循环找到那个标志即可。

```
class TrieTree(object):

  def __init__(self):
    self.tree = {}

  def add(self, word):
    tree = self.tree

    for char in word:
      if char in tree:
        tree = tree[char]
      else:
        tree[char] = {}
        tree = tree[char]

    tree['exist'] = True

  def search(self, word):
    tree = self.tree

    for char in word:
      if char in tree:
        tree = tree[char]
      else:
        return False

    if "exist" in tree and tree["exist"] == True:
      return True
    else:
      return False

tree = TrieTree()
tree.add("abc")
tree.add("bcd")
print(tree.tree)
# Print {'a': {'b': {'c': {'exist': True}}}, 'b': {'c': {'d': {'exist': True}}}}
print(tree.search("ab"))
# Print False
print(tree.search("abc"))
# Print True
print(tree.search("abcd"))
# Print False
```

这是本章内容，希望对你有所帮助。[进入下一章](./013Trie树.md)