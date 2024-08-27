(define/contract (reverse x)
  (-> exact-integer? exact-integer?)
  (define (reverse-helper n rev)
    (if (= n 0)
        rev
        (let* ([pop (modulo n 10)]
               [new-rev (+ (* rev 10) pop)])
          (cond
            [(or (and (positive? rev) (> new-rev (sub1 (expt 2 31))))
                 (and (negative? rev) (< new-rev (- (expt 2 31)))))
             0]
            [else
             (reverse-helper (quotient n 10) new-rev)]))))
  
  (let ([abs-x (abs x)])
    (if (negative? x)
        (let ([result (reverse-helper abs-x 0)])
          (if (< result (- (expt 2 31)))
              0
              (- result)))
        (let ([result (reverse-helper abs-x 0)])
          (if (> result (sub1 (expt 2 31)))
              0
              result)))))
