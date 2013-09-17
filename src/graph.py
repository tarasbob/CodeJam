class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def longestPath(node):
    if node == None:
        return 0
    else:
        return max(longestPath(node.left), longestPath(node.right)) + 1

def shortestPath(node):
    if node == None:
        return 0
    else:
        return min(shortestPath(node.left), shortestPath(node.right)) + 1

def isBalanced(node):
    return longestPath(node) - shortestPath(node) <= 1

def LLToTree(start, end):
    if start == end:
        return None
    cur = start
    numnodes = 0
    while cur and cur != end:
        cur = cur.right
        numnodes += 1

    mid = start
    for i in range(numnodes // 2):
        mid = mid.right 

    mid.left = LLToTree(start, mid)
    mid.right = LLToTree(mid.right, end)
    return mid

def createTree(start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    l = createTree(start, mid - 1)
    r = createTree(mid + 1, end)
    n = Node()
    n.data = mid
    n.left = l
    n.right = r
    return n

def LLToTree(node):
    numNodes = 0
    cur = node
    while cur:
        numNodes += 1
        cur = cur.right
    tree = createTree(1, numNodes)
    def nextNode(node):
        while node:
            yield node
            node = node.right
    def visit(node):
        node.data = next(it)
    
    

def treeToLL(node):
    pass

def inOrder(node, visit):
    if node:
        inOrder(node.left)
        visit(node)
        inOrder(node.right)

def bfs(node):
    q = [node]
    while q:
        n = q.pop(0)
        if n:
            print n.data
            q.append(n.left)
            q.append(n.right)


t = createTree(1, 100)
bfs(t)
