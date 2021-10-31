# Falsy
print(bool(''))
print(bool(0))
print(bool(0.0))
print(bool({}))
print(bool(()))
print(bool([]))

# Truthy
print(bool('string'))
print(bool(1))
print(bool(1.0))
print(bool({'id': 10}))
print(bool(({'id': 10})))
print(bool([{'id': 10}]))
