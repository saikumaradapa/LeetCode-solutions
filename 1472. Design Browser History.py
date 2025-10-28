class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class BrowserHistory:
    
    def __init__(self, homepage: str): # O(1) time complexity
        self.curr = Node(homepage)
        
    def visit(self, url: str) -> None: # O(1) time complexity
        self.curr.next = Node(url, None, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str: # O(steps) time complexity 
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.data

    def forward(self, steps: int) -> str: # O(steps) time complexity 
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.data
