(define/contract (convert s numRows)
  (-> string? exact-integer? string?)
  (define (zigzag s numRows)
    (if (<= numRows 1)
        s
        (let* ([len (string-length s)]
               [rows (make-vector numRows "")]
               [step (* 2 (sub1 numRows))]) ; Adjusted step calculation
          (for ([i (in-range len)])
            (let* ([char (string-ref s i)]
                   [pos (modulo i step)]
                   [current-row (if (< pos numRows)
                                    pos
                                    (- step pos))])
              (vector-set! rows current-row
                           (string-append (vector-ref rows current-row) (string char)))))
          (apply string-append (vector->list rows)))))
  (zigzag s numRows))