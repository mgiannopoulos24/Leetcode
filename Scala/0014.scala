import scala.util.control.Breaks._

object Solution {
    def longestCommonPrefix(strs: Array[String]): String = {
        if (strs.isEmpty) return ""
        
        var prefix = strs(0)
        
        breakable {
            for (i <- 1 until strs.length) {
                while (strs(i).indexOf(prefix) != 0) {
                    prefix = prefix.substring(0, prefix.length - 1)
                    if (prefix.isEmpty) break
                }
            }
        }
        
        prefix
    }
}