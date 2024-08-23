func convert(s string, numRows int) string {
	if numRows == 1 || numRows >= len(s) {
		return s
	}

	rows := make([][]rune, numRows)
	direction := 1 // 1 for down, -1 for up
	row := 0

	for _, char := range s {
		rows[row] = append(rows[row], char)

		if row == 0 {
			direction = 1
		} else if row == numRows-1 {
			direction = -1
		}

		row += direction
	}

	var result []rune
	for _, r := range rows {
		result = append(result, r...)
	}

	return string(result)
}