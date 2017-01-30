# Water-Jug problem using BFS
## Production Rules:
* (x, y) -> (a, y)  if x < a
* (x, y) -> (x, b) if y < b
* (x, y) -> (0, y) if x > 0
* (x, y) -> (x, 0) if y > 0
* (x, y) -> (min(x+a), max(0, x+y - a)) if y > 0
* (x, y) -> (max(0, x+y - b), min(x+y, b)) if x > 0

