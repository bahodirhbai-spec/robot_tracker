def add_vectors(position, vector):
    position[0] += vector[0]
    position[1] += vector[1]
    return position


def multiply_vector(vector, scalar):
    return [vector[0] * scalar, vector[1] * scalar]


position = [0, 0]

moves = [
    [2, 3],
    [-1, 2],
    [3, -2]
]

for move in moves:
    position = add_vectors(position, move)
    print("Current position:", position)

print("Final position:", position)

# Scalar Multiplication
vector = [2, 3]
scalar = 3

print("Scalar result:", multiply_vector(vector, scalar))
