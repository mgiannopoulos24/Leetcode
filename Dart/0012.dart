class Solution {
  String intToRoman(int num) {
    // Define the Roman numeral symbols and their values
    List<int> values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    List<String> symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    
    StringBuffer roman = StringBuffer();
    
    for (int i = 0; i < values.length; i++) {
      while (num >= values[i]) {
        num -= values[i];
        roman.write(symbols[i]);
      }
    }
    
    return roman.toString();
  }
}
