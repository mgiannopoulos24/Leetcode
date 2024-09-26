(define/contract (roman-to-int s)
  (-> string? exact-integer?)
  (define roman-map
    (hash "I" 1 "V" 5 "X" 10 "L" 50 "C" 100 "D" 500 "M" 1000))
  
  (define (char-to-int ch)
    (hash-ref roman-map (string ch))) ; Convert character to string to match hash keys
  
  (define (process-roman lst prev-val total)
    (if (null? lst)
        total
        (let* ((current-val (char-to-int (car lst))) ; Use (car lst) to extract the character
               (new-total (if (< current-val prev-val)
                              (- total current-val)
                              (+ total current-val))))
          (process-roman (cdr lst) current-val new-total))))
  
  (process-roman (reverse (string->list s)) 0 0))
