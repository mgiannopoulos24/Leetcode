object Solution {
    def isValid(s: String): Boolean = {
        val stack = scala.collection.mutable.Stack[Char]()
        val matchingBracket = Map(')' -> '(', '}' -> '{', ']' -> '[')

        var isValid = true

        for (char <- s if isValid) {
            char match {
                case '(' | '{' | '[' =>
                    stack.push(char)
                case ')' | '}' | ']' =>
                    if (stack.isEmpty || stack.pop() != matchingBracket(char)) {
                        isValid = false
                    }
                case _ =>
                    // Invalid character (not expected based on the problem constraints)
                    isValid = false
            }
        }

        isValid && stack.isEmpty
    }
}
