import sys
import requests
from functools import cache
from collections import defaultdict, Counter, deque

def get_input(day, year, session_cookie):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_cookie}
    r = requests.get(url, cookies=cookies)
    r.raise_for_status()
    return r.text

session = "53616c7465645f5f11058e67d15f3400575f0a901b2649d6b36a3579a078b07dca4cf14f41eeebdc3fe309bab5d984016012f85401fad64f6c983be67303f966"
D = get_input(7, 2025, session)
G = [list(row) for row in D.splitlines()]
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c]=='S':
            sr,sc = r,c

@cache
def score(r,c):
    if r+1==R:
        return 1
    if G[r+1][c]=='^':
        return score(r+1,c-1)+score(r+1,c+1)
    else:
        return score(r+1,c)

p1 = 0
Q = deque([(sr,sc)])
SEEN = set()
while Q:
    r,c = Q.popleft()
    if (r,c) in SEEN:
        continue
    SEEN.add((r,c))
    if r+1==R:
        continue
    if G[r+1][c]=='^':
        Q.append((r+1, c-1))
        Q.append((r+1, c+1))
        p1 += 1
    else:
        Q.append((r+1,c))

print(p1)
p2 = score(sr,sc)
print(p2)