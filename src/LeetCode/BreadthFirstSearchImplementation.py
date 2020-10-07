#Todo

def BFS(s, Adj):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            print("frontier -> " + u)
            for v in Adj[u]:
                print("v in Adj -> " + v)
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
                print("Next is: " + str(next))
                frontier = next
                i += 1


root = "s"
Adj = {"s": ["a", "x"],
       "a": ["z", "s"],
       "z": ["a"],
       "x": ["s", "c", "d"],
       "c": ["x", "d", "f", "v"],
       "d": ["x", "c", "f"],
       "f": ["d", "c", "v"],
       "v": ["c", "f"],
       }

BFS(root, Adj)
