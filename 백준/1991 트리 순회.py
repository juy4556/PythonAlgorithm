def preorder_traversal(index):
    left, right = nodes[index]
    preorder.append(chr(index + 65))
    if left:
        preorder_traversal(left)
    if right:
        preorder_traversal(right)


def inorder_traversal(index):
    left, right = nodes[index]
    if left:
        inorder_traversal(left)

    inorder.append(chr(index + 65))

    if right:
        inorder_traversal(right)


def postorder_traversal(index):
    left, right = nodes[index]
    if left:
        postorder_traversal(left)
    if right:
        postorder_traversal(right)

    postorder.append(chr(index + 65))


if __name__ == "__main__":
    N = int(input())
    nodes = [[0, 0] for _ in range(N)]
    for _ in range(N):
        node, left, right = input().split()
        if 'A' <= left <= 'Z':
            nodes[ord(node) - 65][0] = ord(left) - 65
        if 'A' <= right <= 'Z':
            nodes[ord(node) - 65][1] = ord(right) - 65
    preorder, inorder, postorder = [], [], []

    preorder_traversal(0)
    inorder_traversal(0)
    postorder_traversal(0)
    print("".join(preorder))
    print("".join(inorder))
    print("".join(postorder))
