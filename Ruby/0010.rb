# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
    m = s.length
    n = p.length
    
    # Create a DP table with (m+1) x (n+1) dimensions
    dp = Array.new(m + 1) { Array.new(n + 1, false) }
    
    # Base case: empty string matches empty pattern
    dp[0][0] = true
    
    # Initialize DP table for patterns that can match an empty string
    (1..n).each do |j|
      if p[j - 1] == '*'
        dp[0][j] = dp[0][j - 2]
      end
    end
    
    # Fill the DP table
    (1..m).each do |i|
      (1..n).each do |j|
        if p[j - 1] == s[i - 1] || p[j - 1] == '.'
          dp[i][j] = dp[i - 1][j - 1]
        elsif p[j - 1] == '*'
          dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (p[j - 2] == s[i - 1] || p[j - 2] == '.'))
        end
      end
    end
    
    dp[m][n]
  end