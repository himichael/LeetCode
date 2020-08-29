class Solution:
    def findItinerary(self, tickets):
        if not tickets:
            return []
        d = dict() #collections.defaultdict(list)
        stack = []
        def dfs(cur):
            if cur not in d:
                pass #print "cur->" + str(cur)
            while cur in d and len(d[cur])>0:
                #print d[cur]
                tmp = heapq.heappop(d[cur])
                dfs(tmp)
            stack.append(cur)
        for start,end in tickets:
            if start not in d:
                d[start] = []
            d[start].append(end)
        for key in d.keys():
            heapq.heapify(d[key])
        dfs("JFK")
        return stack[::-1]