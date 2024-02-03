(parents, children) = (1, 1)
while children < 100:
    print(
        "parents {parents}, children {children}".format(
            parents=parents, children=children
        )
    )
    (parents, children) = (children, parents + children)
