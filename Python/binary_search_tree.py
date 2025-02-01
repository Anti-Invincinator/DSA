'''
Binary Search Tree; An intuitive data structure where each node's left subtree contains values less than the node and the right subtree contains the values greater.

Efficient searching, insertion and deletion (O(log n)), uses a set of recursive functions to achieve this.

I have used Tkinter to vizualise the BST, mapping it and drawing it out
'''

import tkinter as tk
from tkinter import simpledialog, messagebox


# ----------------------------------------
# Binary Search Tree
# ----------------------------------------

class Node:
    def __init__(self, key):
        self.key = key       # key is value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None  

    def insert(self, key):
        # insert a new value to BST
        if self.root is None : # the tree is empty
            self.root = Node(key)

        else :
            self._insert(self.root, key)


    def _insert(self, node, key):
        # Recursively inserts a new key to either left or right subtree
        if key < node.key:  # inserts to the left subtree
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)

        else: 
            # inserts to the right subtree
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return None # Reached a leaf without finding the key value
        if node.key == key:
            return node
        
        # Compare the key value and decide to recure down left or right subtree
        if key < node.key:
            return self._search(node.left, key)
        
        else:
            return self._search(node.right, key)
        
# ----------------------------------------
# Computing Node Positions (Layout of BST)
# ----------------------------------------
def compute_position(root, horizontal_spacing = 80, vertical_spacing = 80, margin = 40):
    '''
    Compute (X, y) coordinates for each node using an in-order traversal.
    X is determined by in-order index
    y is determined by depth
    '''
    positions = {}
    x_counter = [0] # to keep track of x-index

    def traverse(node, depth):
        if node is None:
            return # empty tree or end of tree
        # Left ST
        traverse(node.left, depth + 1)

        # Assign position for current node
        x = margin + x_counter[0] * horizontal_spacing
        y = margin + depth * vertical_spacing
        positions[node] = (x, y)
        x_counter[0] += 1

        # Right ST
        traverse(node.right, depth + 1)

    traverse(root, 0)
    return positions

# ----------------------------
# Drawing the BST
# ----------------------------

def draw_bst(canvas, bst):
    """
    Tkinter to draw the BST
    Computes the positions, then draws the edges, finally the leaves (nodes)
    """
    canvas.delete("all")

    positions = compute_position(bst.root,
                                  horizontal_spacing = 80,
                                    vertical_spacing = 80,
                                      margin = 40)
    
    def draw_edges(node):
        if node is None:
            return # Recursion break at end of tree.
        
        # Draw line to left child.
        if node.left:
            x1, y1 = positions[node]
            x2, y2 = positions[node.left]
            canvas.create_line(x1, y1, x2, y2)
            draw_edges(node.left)

        # Draw line to right child.
        if node.right:
            x1, y1 = positions[node]
            x2, y2 = positions[node.right]
            canvas.create_line(x1, y1, x2, y2)  
            draw_edges(node.right)

    draw_edges(bst.root)

    # Draw the leaves as circles with the node key inside.
    node_radius = 10
    for node, (x, y) in positions.items():
        canvas.create_oval(x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill="lightgreen")
        canvas.create_text(x, y, text=str(node.key))

def main():
    # Example usage:
    bst = BinarySearchTree()
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)
    target = 12
    result = bst.search(target)
    if result:
        print(f"Target {target} found in BST.")
    else:
        print("Target not found in BST.")



    # ----------------------------
    # TkinterI
    # ----------------------------    

    # Initialize the main Tkinter window.
    root_window = tk.Tk()
    root_window.title("BST Visualization")
    
    # Create a top frame for the canvas.
    top_frame = tk.Frame(root_window)
    top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    # Create a bottom frame for the button.
    bottom_frame = tk.Frame(root_window)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Create the canvas to draw the BST.
    canvas = tk.Canvas(top_frame, width=600, height=400, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)
    
    # Draw the initial BST.
    draw_bst(canvas, bst)

    # ----------------------------
    # Inserting values via GUI
    # ----------------------------
    def insert_value():
        """
        Opens a dialog to enter a new integer value.
        Inserts the value into the BST and redraws the tree.
        """
        new_val_str = simpledialog.askstring("Insert", "Enter value to insert:")
        if new_val_str is not None:
            try:
                new_val = int(new_val_str)
                bst.insert(new_val)
                draw_bst(canvas, bst)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid integer.")
    
    # Create the Insert Node button in the bottom frame.
    insert_button = tk.Button(bottom_frame, text="Insert Node", command=insert_value)
    insert_button.pack(pady=10)

    # Start the Tkinter main loop.
    root_window.mainloop()


if __name__ == "__main__":
    main()