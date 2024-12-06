class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_changes = [0] * 101  # For years 1950 to 2050

        for birth, death in logs:
            population_changes[birth - 1950] += 1
            population_changes[death - 1950] -= 1

        max_population = 0
        current_population = 0
        earliest_year = 1950

        for year in range(101):
            current_population += population_changes[year]
            if current_population > max_population:
                max_population = current_population
                earliest_year = 1950 + year

        return earliest_year
