# Water-Jug problem using BFS
## Production Rules:
* (x, y) -> (a, y)  if x < a
* (x, y) -> (x, b) if y < b
* (x, y) -> (0, y) if x > 0
* (x, y) -> (x, 0) if y > 0
* (x, y) -> (min(x+y, a), max(0, x+y - a)) if y > 0
* (x, y) -> (max(0, x+y - b), min(x+y, b)) if x > 0
<br />
These production rules are used to find the neighbouring states from the current states.<br />

The Algorithm goes like this:<br />

0. Create an empty `path` list.
1. Add start state to the `front` queue.
2. Mark it visited by adding it in `visited` list.
3. While `front` is not empty, follow the steps(4 - 6) below.
4. Pop out a state from `front` and call it `current`.Add `current` to `path` list.
5. Expand all it's neighbours following the production rules.
6. If the neighbours are not in `visited` , then add them to `visited` list and also add them to the `front` queue.
7. return `path`.
        
