(define (is-palindrome x)
  (define (reverse-number n reversed)
    (if (= n 0)
        reversed
        (reverse-number (quotient n 10)
                        (+ (* reversed 10) (remainder n 10)))))
  
  (cond
    [(< x 0) #f] ; Negative numbers are not palindromes
    [(and (= (remainder x 10) 0) (not (= x 0))) #f] ; Numbers ending in zero (other than zero itself) are not palindromes
    [else (= x (reverse-number x 0))])) ; Reverse the number and compare it to the original