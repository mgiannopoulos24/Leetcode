class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                tx -= max((tx - sx) // ty * ty, ty)
            else:
                ty -= max((ty - sy) // tx * tx, tx)
        return False
