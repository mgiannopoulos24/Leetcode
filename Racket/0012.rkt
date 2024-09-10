(define (int-to-roman num)
  (define values '(1000 900 500 400 100 90 50 40 10 9 5 4 1))
  (define symbols '("M" "CM" "D" "CD" "C" "XC" "L" "XL" "X" "IX" "V" "IV" "I"))

  ;; Create a list of pairs of values and symbols
  (define value-symbols (map cons values symbols))
  
  (define (convert n value-symbols)
    (cond
      [(empty? value-symbols) ""]
      [else
       (define value (car (car value-symbols)))
       (define symbol (cdr (car value-symbols)))
       (if (>= n value)
           (string-append symbol
                          (convert (- n value) value-symbols))
           (convert n (cdr value-symbols)))]))
  
  (convert num value-symbols))