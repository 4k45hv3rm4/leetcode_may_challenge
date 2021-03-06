class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousin(self, root:TreeNode, x: int,y: int)-> bool:
        xinfo = []
        yinfo = []
        depth = 0
        if root is None:
            return False
        print(xinfo, yinfo)
        self.dfs(root, x, y,  0, None, xinfo, yinfo)
        return xinfo[0][0]==yinfo[0][0] and xinfo[0][1]!=yinfo[0][1]

    def dfs(self, root, x, y, depth,parent, xinfo, yinfo):
        if root is None:
            return None
        if root.val == x:
            xinfo.append((depth, parent))

        if root.val == y:
            yinfo.append((depth, parent))
        self.dfs(root.left,x,y,depth+1, root, xinfo, yinfo)
        self.dfs(root.right, x, y, depth+1, root, xinfo, yinfo)
x = Solution()
x.isCousin([1,2,3,4], 3,4)
