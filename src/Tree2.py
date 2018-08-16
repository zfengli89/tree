#coding=utf-8

from src.Constants import *

# 节点类
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 结果集
res_pre = []
res_mid = []
res_after = []
res_level = []

# 先序--递归
def preTraverse(root):
    if root is None:
        return
    # LOGGER.info(root.value)
    res_pre.append(root.value)
    preTraverse(root.left)
    preTraverse(root.right)

# 中序--递归
def midTraverse(root):
    if root is None:
        return
    midTraverse(root.left)
    # LOGGER.info(root.value)
    res_mid.append(root.value)
    midTraverse(root.right)

# 后序--递归
def afterTraverse(root):
    if root is None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    # LOGGER.info(root.value)
    res_after.append(root.value)

# 层次遍历--队列
def levelTraverse(root):
    if root is None:
        return
    myQueue = []
    myQueue.append(root)
    while myQueue:
        node = myQueue.pop(0)
        res_level.append(node.value)
        if node.left is not None:
            myQueue.append(node.left)
        if node.right is not None:
            myQueue.append(node.right)

if __name__ == '__main__':
    root = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G', Node('H'))))
    LOGGER.info('----先序遍历----')
    preTraverse(root)
    LOGGER.info(res_pre)

    LOGGER.info('----中序遍历----')
    midTraverse(root)
    LOGGER.info(res_mid)

    LOGGER.info('----后序遍历')
    afterTraverse(root)
    LOGGER.info(res_after)

    LOGGER.info('---层次遍历----')
    levelTraverse(root)
    LOGGER.info(res_level)

