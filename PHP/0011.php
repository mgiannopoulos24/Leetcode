class Solution {

/**
 * @param Integer[] $height
 * @return Integer
 */
function maxArea($height) {
    $left = 0;
    $right = count($height) - 1;
    $maxArea = 0;

    while ($left < $right) {
        $width = $right - $left;
        $currentHeight = min($height[$left], $height[$right]);
        $area = $width * $currentHeight;
        $maxArea = max($maxArea, $area);

        // Move the pointer pointing to the shorter line
        if ($height[$left] < $height[$right]) {
            $left++;
        } else {
            $right--;
        }
    }

    return $maxArea;
}
}
