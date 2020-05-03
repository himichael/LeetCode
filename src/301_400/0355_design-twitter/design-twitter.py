class Twitter(object):
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.twitter_list = list()
		self.follow_map = dict()
		self.max_size = 10


	def postTweet(self, userId, tweetId):
		"""
		Compose a new tweet.
		:type userId: int
		:type tweetId: int
		:rtype: None
		"""
		self.twitter_list.append( (userId,tweetId) )


	def getNewsFeed(self, userId):
		"""
		Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
		:type userId: int
		:rtype: List[int]
		"""
		n = len(self.twitter_list)
		following_set = self.follow_map.setdefault(userId,set())
		ans = []
		for i in xrange(n-1,-1,-1):
			t = self.twitter_list[i]
			if t[0]==userId or t[0] in following_set:
				ans.append(t[1])
			if len(ans)==self.max_size:
				break
		return ans

			
		
       
	def follow(self, followerId, followeeId):
		"""
		Follower follows a followee. If the operation is invalid, it should be a no-op.
		:type followerId: int
		:type followeeId: int
		:rtype: None
		"""
		if followerId==followeeId:
			return
		following_set = self.follow_map.setdefault(followerId,set())
		following_set.add(followeeId)
			
		

	def unfollow(self, followerId, followeeId):
		"""
		Follower unfollows a followee. If the operation is invalid, it should be a no-op.
		:type followerId: int
		:type followeeId: int
		:rtype: None
		"""
		if followerId==followeeId:
			return
		following_set = self.follow_map.setdefault(followerId,set())
		following_set.discard(followeeId)
		


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)



"""
    另一种实现 
"""
class Twitter(object):
	def __init__(self):
		self.messages_list = dict()
		self.follow_map = dict()
		self.time = 0

	def postTweet(self, userId, tweetId):
		self.time += 1
		self.messages_list.setdefault(userId,list()).append( (self.time,tweetId) )

	def getNewsFeed(self, userId):
		max_heap = []
		if userId in self.messages_list and self.messages_list[userId]:
			#x = 
			heapq.heappush(max_heap, (-self.messages_list[userId][-1][0],userId,0) )
		for uid in self.follow_map.setdefault(userId,set()):
			if uid in self.messages_list and self.messages_list[uid]:
				heapq.heappush(max_heap, (-self.messages_list[uid][-1][0],uid,0) )
		ans = []
		while max_heap and len(ans)<10:
			time,uid,cur = heapq.heappop(max_heap)
			next = cur+1
			if next<len(self.messages_list[uid]):
				heapq.heappush(max_heap, (-self.messages_list[uid][-(next+1)][0],uid,next) )
			ans.append(self.messages_list[uid][-(cur+1)][1])
		return ans
       
	def follow(self, followerId, followeeId):
		if followerId==followeeId:
			return
		self.follow_map.setdefault(followerId,set()).add(followeeId)

	def unfollow(self, followerId, followeeId):
		self.follow_map.setdefault(followerId,set()).discard(followeeId)





"""
	基于链表的实现
"""
class Node(object):
	def __init__(self,time,tid,next=None):
		self.time = time
		self.tid = tid
		self.next = next
		
	def __lt__(self,other):
		return self.time > other.time
	

class Twitter(object):
	def __init__(self):
		self.message = dict()
		self.follow_map = dict()
		self.time = 0
		
	def postTweet(self, userId, tweetId):
		self.time += 1
		node = Node(self.time,tweetId)
		node.next = self.message.setdefault(userId,None)
		self.message[userId] = node

	def getNewsFeed(self, userId):
		queue = []
		ans = []
		userId_node = self.message.setdefault(userId,None)
		if userId_node:
			heapq.heappush(queue,userId_node)
		for uid in self.follow_map.setdefault(userId,set()):
			node = self.message.setdefault(uid,None)
			if node:
				heapq.heappush(queue,node)
		while queue and len(ans)<10:
			node = heapq.heappop(queue)
			if node:
				ans.append(node.tid)
			if node.next:
				heapq.heappush(queue,node.next)
		return ans
		
	def follow(self, followerId, followeeId):
		if followerId==followeeId:
			return 
		self.follow_map.setdefault(followerId,set()).add(followeeId)


	def unfollow(self, followerId, followeeId):
		if followerId==followeeId:
			return 
		self.follow_map.setdefault(followerId,set()).discard(followeeId)
		
		
