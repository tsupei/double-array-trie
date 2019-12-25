# double-array-trie
Try to implement three kinds of trie and compare them

# Structure

```bash
.
├── README.md
└── trie
    ├── __init__.py
    ├── double_array_trie.py
    ├── pointer_trie.py
    └── triple_array_trie.py
```

# Pointer-Trie
It maintains a linked list to store children of a node, it saves time, however additional linear time for searching the child.

I use another package for visualization, named `treeviz`. You can checkout [here](https://github.com/tsupei/treeviz)

```python
pointer_trie = PointerTrie()
pointer_trie.insert(Node("apple"))
pointer_trie.insert(Node("applepie"))
pointer_trie.insert(Node("application"))
pointer_trie.insert(Node("apps"))
pointer_trie.insert(Node("ball"))
pointer_trie.visualize()
```

```bash
├── a
│   └── p
│       └── p
│           ├── l
│           │   ├── [e]
│           │   │   └── p
│           │   │       └── i
│           │   │           └── [e]
│           │   └── i
│           │       └── c
│           │           └── a
│           │               └── t
│           │                   └── i
│           │                       └── o
│           │                           └── [n]
│           └── [s]
└── b
    └── a
        └── l
            └── [l]
* character embraced with brackets represents a leaf node
```

# Reference
[An Implementation of Double-Array Trie](https://linux.thai.net/~thep/datrie/datrie.html)

[Double-Array](http://nanika.osonae.com/DArray/dary.html)

[双数组前缀树(Double-Array Trie)](https://zhuanlan.zhihu.com/p/35193582?fbclid=IwAR0b0zcV6qS7nZGGrX3vF-_UKOcFRtEWAKrnE1DabzsffHDNK5FouKQ0EtI)
