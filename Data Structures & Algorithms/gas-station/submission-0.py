
from typing import List

class Solution:
    def canCompleteCircuit(
        self, gas: List[int], cost: List[int]
    ) -> int:
        total_gas = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]
            total_gas += net
            current_gas += net
            if current_gas < 0:
                start = i + 1
                current_gas = 0
        if total_gas < 0:
            return -1
        return start
