(define/contract (length-of-longest-substring s)
  (-> string? exact-integer?)
  (let ([char-index-map (make-hash)]
        [start 0]
        [max-length 0])
    
    (for ([index (in-naturals)]
          [char (in-string s)])
      
      (let ([prev-index (hash-ref char-index-map char #f)])
        (when (and prev-index (>= prev-index start))
          (set! start (+ prev-index 1))))
      
      (hash-set! char-index-map char index)
      
      (set! max-length (max max-length (- (+ index 1) start))))
    
    max-length))