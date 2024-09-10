#include <string>
#include <vector>

class Solution {
public:
    std::string intToRoman(int num) {
        // Define the Roman numeral symbols and their values
        std::vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        std::vector<std::string> symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        std::string roman;
        
        for (size_t i = 0; i < values.size(); ++i) {
            while (num >= values[i]) {
                num -= values[i];
                roman += symbols[i];
            }
        }
        
        return roman;
    }
};
