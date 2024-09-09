(define (is-match s p)
  (define memo (make-hash))

  (define (dp i j)
    (cond
      [(hash-has-key? memo (cons i j))
       (hash-ref memo (cons i j))]
      [(>= j (string-length p))
       (let ([result (>= i (string-length s))])
         (hash-set! memo (cons i j) result)
         result)]
      [else
       (let* ([first-match (and (< i (string-length s))
                                (or (char=? (string-ref p j) #\.)
                                    (char=? (string-ref s i) (string-ref p j))))]
              [result (if (and (< (+ j 1) (string-length p))
                               (char=? (string-ref p (+ j 1)) #\*))
                          (or (dp i (+ j 2))
                              (and first-match (dp (+ i 1) j)))
                          (and first-match (dp (+ i 1) (+ j 1))))])
         (hash-set! memo (cons i j) result)
         result)]))

  (dp 0 0))