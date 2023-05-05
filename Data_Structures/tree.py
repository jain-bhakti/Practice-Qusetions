class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self,child):
        child.parent = self
        if len(self.children)<2:
            self.children.append(child)
        else:
            return
            
    def get_level(self):
        level = 0
        p = self.parent
        while p :
            level += 1 
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        print(spaces+self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = TreeNode("Electronics")

    cell_phone = TreeNode("cell_phones")
    cell_phone.add_child(TreeNode("Motorola"))
    cell_phone.add_child(TreeNode("nokia"))
    cell_phone.add_child(TreeNode("mi"))

    TV = TreeNode("TV")
    TV.add_child(TreeNode("LG"))
    TV.add_child(TreeNode("HP"))

    root.add_child(cell_phone)
    root.add_child(TV)

    root.print_tree()

if __name__ == "__main__":
    build_tree()
