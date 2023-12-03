class Node:
    def __init__(self, data=None):
        """
        Node კლასი რომ წარადგინო linked listის ყოველი ელემენტი.

        Parameters:
        - data: რაც Node კლასში შეინახება.
        """
        self.data = data
        self.next = None  # შემდეგი node-ის აღმნშვნელი


class LinkedList:
    def __init__(self):
        """
        LinkedList კალსი რომ წარადგინო დალინკული ლისტი.

        ინიციალიზირებს ცარიელ დალინკულ ლისტს.
        """
        self.head = None  # პირველი node ლისტში (თავდაპირველად None)

    def is_empty(self):
        """
        ამოწმებს ცარიელია თუ არა linked list-ი.

        Returns:
        - True თუ ლისტი ცარიელია, სხვა შემთხვევაში False.
        """
        return self.head is None

    def append(self, data):
        """
        ამატებს ახალ node-ს მოცემული data-თი linked list-ის ბოლოს.

        Parameters:
        - data: data სადაც შეინახება ინფო.
        """
        new_node = Node(data)

        if self.is_empty():
            # თუ ლისტი ცარიელია ახალ node-ს აყენებს თავში
            self.head = new_node
        else:
            # გადახედავს სიას რომ იპოვოს ბოლო node და დაამატოს ახალი
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        """
        აჩვენებს linked list-ის ელემენტებს.

        პრინტავს ყველა node-ის data-ს list-ში.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# მაგალითი:
if __name__ == "__main__":
    # შექმენი linked list-ი
    my_linked_list = LinkedList()

    # დაამატე ელემენტები linked list-ში
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)

    # აჩვენე linked list-ი
    my_linked_list.display()
