"""
Problem: 871 - Minimum Number of Refueling Stops
URL: https://leetcode.com/problems/minimum-number-of-refueling-stops/

Solution by Pablo Dávila Herrero (https://pablodavila.eu)
"""

import heapq


class Solution:

    def minRefuelStops(
        self,
        target: int,
        startFuel: int,
        stations: list[list[int]],
    ) -> int:
        if target <= startFuel:
            return 0

        position = startFuel
        reached_stations = []
        n_stops = 0
        s = 0
        while s < len(stations):
            station = stations[s]
            if station[0] <= position:
                fuel_neg = -station[1]
                heapq.heappush(reached_stations, fuel_neg)
                s += 1
            elif len(reached_stations) == 0:
                print("No enough stations behind:", station[0])
                return -1
            else:
                n_stops += 1
                fuel_neg = heapq.heappop(reached_stations)
                fuel = -fuel_neg
                position += fuel

                if position >= target:
                    return n_stops

                print("Refuel:", station[0])

        if position >= target:
            return n_stops

        while len(reached_stations) > 0:
            n_stops += 1
            fuel_neg = heapq.heappop(reached_stations)
            fuel = -fuel_neg
            position += fuel

            if position >= target:
                return n_stops

        return -1
