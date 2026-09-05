class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Total time needed decreases as the eating speed increases -> answer lies in a sorted search space from 1 to max(piles)
        # set left = 1, right = max(piles)
        #while left <= right: compute total hours needed then check with the max time it can eat, if yes -> record, then find a smaller one. Otherwise, if speed is too slow, search on the right

        left, right = 1, max(piles)
        minimum_speed = right

        while left <= right:
            eating_speed = (left + right) // 2
            total_hours = 0

            for pile in piles:
                hours_per_pile = math.ceil(pile / eating_speed)
                total_hours += hours_per_pile
            if total_hours <= h:
                minimum_speed = eating_speed
                right = eating_speed - 1
            else: left = eating_speed + 1
        
        return minimum_speed