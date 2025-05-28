class MyQueue:

    def __init__(self):
        # Stack s1 for enqueue operations (push)
        # Stack s2 for dequeue operations (pop, peek)
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # Always push the new elements to s1
        self.s1.append(x)

    def pop(self) -> int:
        # If s2 is empty, we transfer all elements from s1 to s2
        # This reverses the order to simulate queue behavior
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # Now pop the top of s2 (front of the queue)
        return self.s2.pop()

    def peek(self) -> int:
        # If s2 is empty, transfer elements from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        # Return the top of s2 without removing it (peek at front)
        return self.s2[-1]

    def empty(self) -> bool:
        # Queue is empty only if both the stacks are empty
        return max(len(self.s1), len(self.s2)) == 0
     
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
