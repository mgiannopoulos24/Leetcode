class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        Determine if the player who starts the game can guarantee a win.
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0
