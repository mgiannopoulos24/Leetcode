class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.children = {}  # Dictionary to store the children of each person
        self.dead = set()    # Set to store the names of dead people
        self.children[kingName] = []  # Initialize the king with no children

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.children:
            self.children[parentName] = []
        self.children[parentName].append(childName)
        self.children[childName] = []  # Initialize the child with no children

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        result = []
        
        # Pre-order traversal to generate the inheritance order
        def preorder(person: str):
            if person not in self.dead:
                result.append(person)
            # Visit the person's children
            for child in self.children.get(person, []):
                preorder(child)
        
        preorder(self.king)  # Start the traversal from the king
        return result


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()