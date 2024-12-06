class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        # Process each row for gravity effect
        for row in box:
            write_position = n - 1
            for col in range(n - 1, -1, -1):
                if row[col] == '*':
                    write_position = col - 1
                elif row[col] == '#':
                    row[col], row[write_position] = row[write_position], row[col]
                    write_position -= 1
        
        # Rotate the box 90 degrees clockwise
        rotated_box = [[box[m - 1 - row][col] for row in range(m)] for col in range(n)]
        
        return rotated_box
