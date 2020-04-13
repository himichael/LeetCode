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