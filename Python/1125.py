class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Number of required skills
        n = len(req_skills)
        
        # Mapping from skill name to a bitmask index
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        
        # DP dictionary: key is a bitmask representing the skills covered, value is the list of people covering those skills
        dp = {0: []}  # Start with no skills covered (bitmask 0) with no people
        
        # Iterate over each person and update the DP table
        for i, person_skills in enumerate(people):
            # Calculate the bitmask of the skills this person contributes
            person_skill_mask = 0
            for skill in person_skills:
                if skill in skill_index:
                    person_skill_mask |= 1 << skill_index[skill]  # Set the bit for this skill
            
            # Iterate over all current states in DP and try to improve them by adding this person
            new_dp = dp.copy()  # Make a copy to avoid mutating dp while iterating
            
            for skill_mask, team in dp.items():
                # New skill set if we add this person's skills
                new_skill_mask = skill_mask | person_skill_mask
                
                # If this new skill set isn't in new_dp or we found a smaller team, update it
                if new_skill_mask not in new_dp or len(new_dp[new_skill_mask]) > len(team) + 1:
                    new_dp[new_skill_mask] = team + [i]
            
            dp = new_dp  # Update dp to new_dp after considering this person
        
        # The final bitmask is when all skills are covered, i.e., (1 << n) - 1
        full_skill_mask = (1 << n) - 1
        
        # Return the team that covers all the skills
        return dp[full_skill_mask]
