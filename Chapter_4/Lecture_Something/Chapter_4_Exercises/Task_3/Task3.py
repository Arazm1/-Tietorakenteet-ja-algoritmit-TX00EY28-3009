class StackBasedQueue():
    def __init__(self):
        # YOUR CODE HERE
        self._InboundStack = []
        self._OutboundStack = []
        self._size = 0
        
    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = []

        # outbound is already in correct dequeue order (top is front)
        values.extend(self._OutboundStack)

        # inbound must be reversed to show correct queue order
        values.extend(self._InboundStack[::-1])

        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(map(str, values))}]>'

    def enqueue(self, data):
        # YOUR CODE HERE
        self._InboundStack.append(data)
        self._size += 1

    def dequeue(self):
        # YOUR CODE HERE

        # Inbound:  [A, B, C] -> Outbound: [C, B, A]
        if not self._OutboundStack:
            while self._InboundStack:
                self._OutboundStack.append(self._InboundStack.pop())


        if not self._OutboundStack:
            return None

        self._size -= 1
        return self._OutboundStack.pop()


q = StackBasedQueue()
print(q)

q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.dequeue()

print(q)