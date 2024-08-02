(define/contract (add-two-numbers l1 l2)
  (-> (or/c list-node? #f) (or/c list-node? #f) (or/c list-node? #f))
  (let loop ((l1 l1) (l2 l2) (carry 0) (result #f) (tail #f))
    (if (and (not l1) (not l2) (zero? carry))
        result
        (let* ((val1 (if l1 (list-node-val l1) 0))
               (val2 (if l2 (list-node-val l2) 0))
               (sum (+ val1 val2 carry))
               (new-carry (if (>= sum 10) 1 0))
               (new-val (modulo sum 10))
               (new-node (make-list-node new-val)))
          (if tail
              (set-list-node-next! tail new-node)
              (set! result new-node))
          (loop (if l1 (list-node-next l1) #f)
                (if l2 (list-node-next l2) #f)
                new-carry
                result
                new-node)))))