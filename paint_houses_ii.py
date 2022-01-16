class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
        time: n (houses) * k (colors)
        space: 1
        """
        n_houses = len(costs)
        if n_houses == 0:
            return 0

        # (color, cost)
        prev_min_cost = prev_second_min_cost = prev_min_color = None
        for color, cost in enumerate(costs[0]):
            # check if lower than min_cost
            if prev_min_cost is None or cost < prev_min_cost:
                prev_second_min_cost = prev_min_cost
                prev_min_color = color
                prev_min_cost = cost

            # check if lower than second_min_cost
            elif prev_second_min_cost is None or cost < prev_second_min_cost:
                prev_second_min_cost = cost

        n_colors = len(costs[0])
        for house in range(1, n_houses):
            min_cost = second_min_cost = min_color = None
            for color in range(n_colors):
                cost = costs[house][color]

                # add previous cost
                if color == prev_min_color:
                    cost += prev_second_min_cost
                else:
                    cost += prev_min_cost

                # check if lower than min_cost
                if min_cost is None or cost < min_cost:
                    second_min_cost = min_cost
                    min_color = color
                    min_cost = cost

                # check if lower than second_min_cost
                elif second_min_cost is None or cost < second_min_cost:
                    second_min_cost = cost

            prev_min_cost = min_cost
            prev_min_color = min_color
            prev_second_min_cost = second_min_cost

        return prev_min_cost
