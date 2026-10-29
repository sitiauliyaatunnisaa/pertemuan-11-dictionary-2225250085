data = {"nama": "Ayu", "nilai": 85, "kelas": "A"}

print("Menelusuri Key:")
for key in data:
    print(key)

print("\nMenelusuri Value:")
for value in data.values():
    print(value)

print("\nMenelusuri Key dan Value:")
for key, value in data.items():
    print(f"{key}: {value}")