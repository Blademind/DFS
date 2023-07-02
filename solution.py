def lengthPath(mat, pattern):
    ROWS, COLS =  len(mat), len(mat[0])
    visited = set()
    def dfs(r, c, depth):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or mat[r][c] not in pattern:
            return depth

        visited.add((r,c))
        count = 0
        count += max(dfs(r + 1,c, depth + 1), dfs(r - 1,c, depth + 1), dfs(r,c + 1, depth + 1),  dfs(r,c - 1, depth + 1))

        visited.remove((r,c))
        return count
    
    return dfs(0, 0, 0)
        
    
m = [["a","c","b","c","@","a"],["b","x","z","c","s","a"], ["?","c","d","*","c","d"], ["b","c","a","8","b","b"], ["c","2","x","+","b","c"]]

print(lengthPath(m,"abc"))

