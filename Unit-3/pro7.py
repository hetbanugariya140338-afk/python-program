class A:
    def process(self):
        print("In Class A")

class B(A):
    def process(self):
        print("In Class B")

class C(A):
    def process(self):
        print("In Class C")

class D(B, C):
    pass

# Displaying MRO
print("MRO for Class D:", D.mro())
# Output shows: D -> B -> C -> A -> object