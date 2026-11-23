import heapq

def h(s, goal):
    return sum(s[i] != goal[i] and s[i] != 0 for i in range(9))

def astar(start, goal):
    q = [(h(start, goal), 0, start, [start])]
    visited = set()

    while q:
        f, g, s, path = heapq.heappop(q)

        if s == goal:
            return path
        if s in visited:
            continue
        visited.add(s)

        z = s.index(0)
        r, c = divmod(z, 3)

        for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
            nr, nc = r+dr, c+dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                n = list(s)
                k = nr*3 + nc
                n[z], n[k] = n[k], n[z]
                n = tuple(n)

                if n not in visited:
                    heapq.heappush(q, (g+1+h(n,goal), g+1, n, path+[n]))

    return None

def read():
    return tuple(int(x) for _ in range(3) for x in input().split())

start = read()
goal = read()
path = astar(start, goal)

if path:
    for step, s in enumerate(path):
        print(f"\nStep {step}:")
        for i in range(0, 9, 3):
            print(*['_' if x == 0 else x for x in s[i:i+3]])
    print("Total moves:", len(path)-1)
else:
    print("No solution")
