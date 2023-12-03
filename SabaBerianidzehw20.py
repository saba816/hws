class TreeNode:
    def __init__(self, data):
        """
        TreeNode class რომ წარადგინო ყველა node-ი binary tree-ში.

        Parameters:
        - data: data რომელიც შეინახება node-ში.
        """
        self.data = data
        self.left = None  # მარცხენა subtree-ის მაჩვენებელი
        self.right = None  # მარჯვენა subtree-ის მაჩვენებელი


class BinaryTree:
    def __init__(self):
        """
        BinaryTree კლასი რომ წარადგინო  ორობითი/მეორეული ხე.

        ინიციალიზირებს ცარიელ binary tree-ის.
        """
        self.root = None  # binary tree-ის root-ი (თავდაპირველად None)

    def is_empty(self):
        """
        ამოწმებს ცარიელია თუ არა binary tree-ი.

        Returns:
        - True თუ tree არის ცარიელი, სხვაშემთხვევაში False.
        """
        return self.root is None

    def insert(self, data):
        """
        სვავს ახალ node-ს მოცემული data-თი binary tree-ში.

        Parameters:
        - data: data რომელიც შეინახება new node-ში.
        """
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        """
        დამხმარე ფუნქცია რომელიც რეკურსიულად სვავს new node-ს binary tree-ში.

        Parameters:
        - root: მიმდინარე subtree-ს root-ი.
        - data: data რომელიც შეინახება new node-ში.

        Returns:
        - განახლებულ subtree-ის root-ს ჩასმის შემდეგ.
        """
        if root is None:
            return TreeNode(data)
        elif data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root

    def display(self):
        """
        
        ორობითი ხის ელემენტების ჩვენება თანმიმდევრული გადაკვეთის გამოყენებით.

        პრინტავს tree-ში ყველა node-ის data-ს.
        """
        self._display(self.root)
        print()

    def _display(self, root):
        """
        დამხმარე ფუნქცია ბინარული ხის ელემენტების რეკურსიულად გამოსაჩენად.

        Parameters:
        - root:  მიმდინარე subtree-ს root-ი.
        """
        if root:
            self._display(root.left)
            print(root.data, end=" ")
            self._display(root.right)


# მაგალითი:
if __name__ == "__main__":
    # შექმენი ბინარული ხე
    my_binary_tree = BinaryTree()

    # ჩსვი ელემენტები ბინარულ ხეში
    my_binary_tree.insert(5)
    my_binary_tree.insert(3)
    my_binary_tree.insert(7)
    my_binary_tree.insert(2)
    my_binary_tree.insert(4)

    # აჩვენე ბინარული ხე
    my_binary_tree.display()
