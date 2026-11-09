
import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k, arrival, load):

        # Step 1: Initially all servers are available
        available = SortedList(range(k))

        # Step 2: Store (finish_time, server_id)
        busy = []

        # Step 3: Count requests handled by each server
        count = [0] * k

        # Step 4: Process each request
        for i in range(len(arrival)):

            time = arrival[i]

            # Step 5: Release finished servers
            while busy and busy[0][0] <= time:
                finish_time, server = heapq.heappop(busy)
                available.add(server)

            # Step 6: Drop request if all servers are busy
            if not available:
                continue

            # Step 7: Preferred server
            target = i % k

            # Step 8: Find next available server
            pos = available.bisect_left(target)

            # Step 9: Circular wrap-around
            if pos == len(available):
                pos = 0

            server = available[pos]

            # Step 10: Mark server busy
            available.remove(server)

            finish_time = time + load[i]
            heapq.heappush(busy, (finish_time, server))

            # Step 11: Update request count
            count[server] += 1

        # Step 12: Find maximum requests
        maximum = max(count)

        # Step 13: Return all servers with maximum count
        return [
            i for i in range(k)
            if count[i] == maximum
        ]
