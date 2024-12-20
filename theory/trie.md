# Trie / Prefix Tree
A **trie**, also called a **Prefix Tree**, is a rooted tree used to represent a set of strings. Strings in the tree start at the root node, with each node containing a mapping between the next character to the next node. The special character "_" marks the end of the string.

## Implementation
Implementation of a trie is pretty straightforward, so I'm not going to elaborate. You can find my implementation under the `data_structures/` directory.

| Operation    | Description                       | Time | Space |
|--------------|-----------------------------------|------|-------|
| Insert       | Inserts a new string              | O(n) | O(n)  |
| Search       | Searches for a string             | O(n) | O(1)  |
| SearchPrefix | Searches for a prefix of a string | O(n) | O(1)  |
| Remove      | Removes a string                   | O(n) | O(1)  |

In my implementation, the depth of the recursion of the *Remove* operation, and therefore its space complexity, is O(n). One can use a constant amount of space by keeping a reference from a child to its parent.
As for the rest of the operations of my implementation, their space and time complexity are optimal, like in the table above.
