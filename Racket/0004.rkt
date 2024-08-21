(define/contract (find-median-sorted-arrays nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) flonum?)
  
  (define (find-kth-smallest k nums1 nums2)
    (cond
      [(empty? nums1) (list-ref nums2 k)]
      [(empty? nums2) (list-ref nums1 k)]
      [(= k 0) (min (car nums1) (car nums2))]
      [else
       (let* ([mid1 (min (length nums1) (quotient (+ k 1) 2))]
              [mid2 (min (length nums2) (quotient (+ k 1) 2))]
              [median1 (list-ref nums1 (sub1 mid1))]
              [median2 (list-ref nums2 (sub1 mid2))])
         (cond
           [(< median1 median2)
            (find-kth-smallest (- k mid1) (drop nums1 mid1) nums2)]
           [else
            (find-kth-smallest (- k mid2) nums1 (drop nums2 mid2))]))]))
  
  (define (find-median)
    (let* ([m (length nums1)]
           [n (length nums2)]
           [total-length (+ m n)]
           [half-length (quotient total-length 2)])
      (if (even? total-length)
          (/ (+ (exact->inexact (find-kth-smallest half-length nums1 nums2))
                (exact->inexact (find-kth-smallest (sub1 half-length) nums1 nums2)))
             2.0)
          (exact->inexact (find-kth-smallest half-length nums1 nums2)))))
  
  (find-median))