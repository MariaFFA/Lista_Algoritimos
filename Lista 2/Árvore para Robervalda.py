class Node:
    def __init__(self, value):
        self.value = int(value)
        self.father = None
        self.left = None
        self.right = None
        self.height = 0
        self.balance = 0
        self.sucessor = None

class Tree:
    def __init__(self):
        self.root = None
        self.nodeqt = 0
        self.qtd = 0
    
    def add(self,node):
        self.nodeqt += 1
        above = None
        father = self.root
        while father:
            above = father
            if node.value < father.value:
                father = father.left
            else:
                father = father.right
        node.father = above
        if not above:
            self.root = node
        elif node.value < above.value:
            above.left = node
        else:
            above.right = node
        while above:
            self.updateHeight(above)
            self.updateBalance(above)
            if (-1 > above.balance) or (above.balance > 1):
                self.balanceTree(above)
                above = None
            else:
                above = above.father

    def remove(self, node):
        self.nodeqt -= 1
        node = self.find(int(node), self.root)
        self.whoissucessor(node)
        if not node.sucessor:
            above = node.father
        elif node.sucessor.father == node:
            above = node.sucessor
        else:
            above = node.sucessor.father
        if not node.father:
            self.root = node.sucessor
            if not node.sucessor:
                return None
            elif (not node.right and node.left == node.sucessor) or (not node.left and node.sucessor == node.right):
                self.root.father = None
                return None
        if not node.left:
            if not node.right:
                if node.father.left == node:
                    node.father.left = None
                else:
                    node.father.right = None
            else:    
                if node.value < node.father.value:
                    node.father.left = node.right
                    node.right.father = node.father
                else:
                    node.father.right = node.right
                    node.right.father = node.father
                node.sucessor.father = node.father
        elif not node.right:
            if node.value < node.father.value:
                node.father.left = node.left
            else:
                node.father.right = node.left
            node.sucessor.father = node.father
        else:
            if node.sucessor.father != node:
                if node.sucessor.right:
                    node.sucessor.father.left = node.sucessor.right
                    node.sucessor.right.father = node.sucessor.father
                else:
                    node.sucessor.father.left = None
            node.sucessor.father = node.father
            if node.sucessor != node.left:
                node.sucessor.left = node.left
            if node.sucessor != node.right:
                node.sucessor.right = node.right
            if node.father and node.father.left == node:
                node.father.left = node.sucessor
            elif node.father:
                node.father.right = node.sucessor
            if node.left != node.sucessor:
                node.left.father = node.sucessor
            if node.right != node.sucessor:
                node.right.father = node.sucessor
        while above:
            self.updateHeight(above)
            self.updateBalance(above)
            if (-1 > above.balance) or (above.balance > 1):
                self.balanceTree(above)
            above = above.father
        
    def whoissucessor(self,node):
        if not node.right and node.left:
            node.sucessor = node.left
        elif node.right:
            s = node.right
            while s.left:
                s = s.left
            node.sucessor = s

    def find(self,value, root):
        if root and root.value != value:
            if value < root.value:
                root = self.find(value, root.left)
            else:
                root = self.find(value, root.right)
        return root
    
    def balanceTree(self,father):
        if father.left:
            self.updateBalance(father.left)
        if father.right:
            self.updateBalance(father.right)
        if father.right and father.balance > 1 and father.right.balance < 0:
            self.rightRotation(father.right)
            self.leftRotation(father)
        elif father.left and father.balance < -1 and father.left.balance > 0:
            self.leftRotation(father.left)
            self.rightRotation(father)
        elif father.balance < -1:
            self.rightRotation(father)
        elif father.balance > 1:
            self.leftRotation(father)

    def rightRotation(self, node):
        goDown = node
        goUp = node.left
        father = node.father
        if goUp.right:
            goUp.right.father = goDown
        if not father:
            self.root = goUp
        elif goDown.value > father.value:
            father.right = goUp
        else:
            father.left = goUp
        goUp.father = father
        goDown.father = goUp
        goDown.left = goUp.right
        goUp.right = goDown
        while goDown:
            self.updateHeight(goDown)
            self.updateBalance(goDown)
            goDown = goDown.father

    def leftRotation(self, node):
        goDown = node
        goUp = node.right
        father = node.father
        if goUp.left:
            goUp.left.father = goDown
        if not father:
            self.root = goUp
        elif goDown.value < father.value:
            father.left = goUp
        else:
            father.right = goUp
        goUp.father = father
        goDown.father = goUp
        goDown.right = goUp.left
        goUp.left = goDown
        while goDown:
            self.updateHeight(goDown)
            self.updateBalance(goDown)
            goDown = goDown.father

    def updateHeight(self, node):
        if not node.right and not node.left:
            node.height = 0
        elif not node.right and node.left:
            node.height = node.left.height + 1
        elif not node.left and node.right:
            node.height = node.right.height + 1
        elif node.right.height > node.left.height:
            node.height = node.right.height + 1
        else:
            node.height = node.left.height + 1

    def updateBalance(self,node):
        if not node.right:
            if not node.left:
                node.balance = 0
            else:
                node.balance = 0 - node.left.height - 1
        elif not node.left:
            node.balance = node.right.height + 1
        else:
            node.balance = node.right.height - node.left.height

    def nodeDepth(self, value, root, nivel):
        if root.value != value:
            nivel += 1
            if value < root.value:
                root, nivel = self.nodeDepth(value, root.left, nivel)
            else:
                root, nivel = self.nodeDepth(value, root.right, nivel)
        return root, nivel
    
    def preOrder(self, node):
        if not node:
            return
        else:
            self.qtd += 1
            if self.qtd < self.nodeqt:
                print(node.value, end=',')
            else:
                print(node.value, end='')
            self.preOrder(node.left)
            self.preOrder(node.right)
                
    def postOrder(self, node):
        if not node:
            return
        else:
            self.postOrder(node.left)
            self.postOrder(node.right)
            self.qtd += 1
            if self.qtd < self.nodeqt:
                print(node.value, end=',')
            else:
                print(node.value, end='')

    def inOrder(self, node):
        if not node:
            return
        else:
            self.inOrder(node.left)
            self.qtd += 1
            if self.qtd < self.nodeqt:
                print(node.value, end=',')
            else:
                print(node.value, end='')
            self.inOrder(node.right)

def main():
    action = input()
    tree = Tree()
    while action != 'FIM':
        action = action.split(' ')
        function = action[0]
        value = action[1]
        if function == 'ADICIONA' and not tree.find(int(value), tree.root):
            value = Node(value)
            tree.add(value)
        elif function == 'REMOVE':
            if not tree.find(int(value), tree.root):
                print('Valor',value,'inexistente')
            else:
                tree.remove(value)
        elif function == 'NIVEL':
            if not tree.find(int(value), tree.root):
                print('Valor',value,'inexistente')
            else:
                node, nivel = tree.nodeDepth(int(value), tree.root,0)
                print('Nivel de ',value,': ',nivel, sep='')
        elif value == 'PREORDEM':
            tree.qtd = 0
            print('[',end='')
            if tree.root:
                tree.preOrder(tree.root,)
            print(']')
        elif value == 'POSORDEM':
            tree.qtd = 0
            print('[',end='')
            if tree.root:
                tree.postOrder(tree.root)
            print(']')
        elif value == 'EMORDEM':
            tree.qtd = 0
            print('[',end='')
            if tree.root:
                tree.inOrder(tree.root)
            print(']')
        action = input()

if __name__ == '__main__':
    main()

