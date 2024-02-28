def find_number():
    remember = []

    for x in range(1, 101):
        for y in range(2, 101):
            z = (x ** 2 + y ** 2) ** 0.5
            if int(z) == z and int(z) <= 100:
                remember.append((x, y, int(z)))

    return remember
 
pisagor_triples = find_number()
for triple in pisagor_triples:
    print(triple)
