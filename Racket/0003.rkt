(define (count-substr str character-vec [start 0] [end 0] [longest-str 0])
  (if (eq? end (string-length str))
      longest-str
      (let ([end-index (char->integer (string-ref str end))])
           (if (eq? (vector-ref character-vec end-index) 1)
               (begin
                 (vector-set! character-vec
                              (char->integer (string-ref str start))
                              0)
                 (count-substr str character-vec
                               (add1 start) end
                               longest-str))
               (begin
                 (vector-set! character-vec end-index 1)
                 (count-substr str character-vec
                               start (add1 end)
                               (max longest-str 
                                    (add1 (- end start)))))))))

(define/contract (length-of-longest-substring s)
  (-> string? exact-integer?)
    (count-substr s (make-vector 256 0)))