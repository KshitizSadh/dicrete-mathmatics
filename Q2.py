class Relation:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def is_reflexive(self):
        for i in range(self.size):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

    def is_transitive(self):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    if self.matrix[i][j] == 1 and self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                        return False
        return True

def check_relation_type(relation):
    if relation.is_reflexive() and relation.is_symmetric() and relation.is_transitive():
        return "Equivalence Relation"
    elif relation.is_reflexive() and relation.is_antisymmetric() and relation.is_transitive():
        return "Partial Order Relation"
    else:
        return "None"

# Example usage
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

relation = Relation(matrix)

print("Is Reflexive:", relation.is_reflexive())
print("Is Symmetric:", relation.is_symmetric())
print("Is Antisymmetric:", relation.is_antisymmetric())
print("Is Transitive:", relation.is_transitive())
print("Type of Relation:", check_relation_type(relation))