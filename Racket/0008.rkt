(define INT_MIN -2147483648)
(define INT_MAX 2147483647)

(define (my-atoi s)
  ;; Trim leading and trailing whitespace
  (define trimmed (string-trim s))
  
  ;; If the string is empty after trimming, return 0
  (if (= (string-length trimmed) 0)
      0
      (let* ([first-char (string-ref trimmed 0)]
             [rest (cond
                     [(char=? first-char #\space) (substring trimmed 1)]
                     [(char=? first-char #\+) (substring trimmed 1)]
                     [(char=? first-char #\-) (substring trimmed 1)]
                     [else trimmed])]
             [sign (cond
                     [(char=? first-char #\space) 1]
                     [(char=? first-char #\+) 1]
                     [(char=? first-char #\-) -1]
                     [else 1])])
        
        ;; Convert the string to an integer
        (define (parse-integer str sign)
          (let loop ([index 0] [result 0])
            (if (>= index (string-length str))
                (if (zero? result)
                    0
                    (if (< result 0) (max result INT_MIN) (min result INT_MAX)))
                (let ([char (string-ref str index)])
                  (cond
                    [(char-numeric? char)
                     (let* ([digit (- (char->integer char) (char->integer #\0))]
                            [new-result (+ (* result 10) (* sign digit))]
                            [overflow (or (> new-result INT_MAX) (< new-result INT_MIN))])
                       (if overflow
                           (if (> new-result 0) INT_MAX INT_MIN)
                           (loop (+ index 1) new-result)))]
                    [else (if (zero? result) 0
                              (if (< result 0) (max result INT_MIN) (min result INT_MAX)))])))))

        ;; Call parse-integer with the appropriate sign
        (parse-integer rest sign))))