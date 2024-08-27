class Solution {
  int reverse(int x) {
    const int intMax = 2147483647;
    const int intMin = -2147483648;
    int rev = 0;
    int sign = (x < 0) ? -1 : 1;
    x = x * sign;  // Make x positive for simplicity

    while (x != 0) {
      int pop = x % 10;
      x ~/= 10;

      // Check for overflow/underflow before multiplying rev by 10 and adding pop
      if (rev > intMax ~/ 10 || (rev == intMax ~/ 10 && pop > 7)) return 0;
      if (rev < intMin ~/ 10 || (rev == intMin ~/ 10 && pop < -8)) return 0;

      rev = rev * 10 + pop;
    }

    return rev * sign;  // Restore the original sign
  }
}
