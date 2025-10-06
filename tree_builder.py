class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.
    '''
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # if tree is empty
        if not self.root:
            print("⚠️ Add a team lead first before adding employees.")
            return
        
        if current_node is None:
            current_node = self.root

        # if we find the manager
        if current_node.name.lower() == manager_name.lower():
            new_employee = EmployeeNode(employee_name)
            if side == "left":
                if current_node.left is None:
                    current_node.left = new_employee
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}.")
                else:
                    print(f"⚠️ {manager_name} already has a left subordinate.")
            elif side == "right":
                if current_node.right is None:
                    current_node.right = new_employee
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}.")
                else:
                    print(f"⚠️ {manager_name} already has a right subordinate.")
            else:
                print("❌ Invalid side. Choose 'left' or 'right'.")
            return True

        # recursively search left and right
        if current_node.left:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True
        if current_node.right:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True
        
        # if manager not found at all
        if current_node == self.root:
            print(f"❌ Manager '{manager_name}' not found in the team.")
        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
            if node is None:
                print("⚠️ No team lead or employees added yet.")
                return
        
        indent = "    " * level
        print(f"{indent}- {node.name}")
        if node.left:
            self.print_tree(node.left, level + 1)
        if node.right:
            self.print_tree(node.right, level + 1)


# ------------------------------
# CLI functionality
# ------------------------------
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower().strip()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")


# Uncomment below to run interactively:
company_directory()
