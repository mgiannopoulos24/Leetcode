class Solution {

    /**
     * @param Integer $x
     * @return Integer
     */
    function reverse($x) {
        $rev = 0;
        $INT_MAX = 2147483647; // Max value for a 32-bit signed integer
        $INT_MIN = -2147483648; // Min value for a 32-bit signed integer
        
        while ($x != 0) {
            $pop = $x % 10;
            $x = (int)($x / 10); // Use (int) to truncate towards zero
            
            // Check for overflow/underflow before multiplying rev by 10 and adding pop
            if ($rev > ($INT_MAX - $pop) / 10 || $rev < ($INT_MIN - $pop) / 10) {
                return 0;
            }
            
            $rev = $rev * 10 + $pop;
        }
        
        return $rev;
    }
}
