(define/contract (max-area height)
  (-> (listof exact-integer?) exact-integer?)
  (define (max-area-helper height left right max-area)
    (if (>= left right)
        max-area
        (let* ([left-height (list-ref height left)]
               [right-height (list-ref height right)]
               [width (- right left)]
               [current-area (* (min left-height right-height) width)]
               [new-max-area (max max-area current-area)])
          (if (< left-height right-height)
              (max-area-helper height (+ left 1) right new-max-area)
              (max-area-helper height left (- right 1) new-max-area)))))

  (max-area-helper height 0 (- (length height) 1) 0))