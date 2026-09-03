dict1 = {"name": "John", "job": "Developer"}
dict2 = {"name": "Jane", "job": "Manager"}

# Parallel iteration over keys and values
for (k1, v1), (k2, v2) in zip(dict1.items(), dict2.items()):
    print(k1, v1, k2, v2)