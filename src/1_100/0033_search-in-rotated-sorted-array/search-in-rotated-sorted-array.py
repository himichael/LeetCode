class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(nums==None or len(nums)==0):
            return -1
        if(len(nums) == 1):
            return 0 if(nums[0]==target) else -1

        def findMin():
            begin = 0
            end = len(nums)-1
            if(nums[begin] < nums[end]):
                return begin
            while(begin <= end):
                mid = (begin+end)/2
                if(nums[mid] > nums[mid+1]):
                    return mid+1
                else:
                    if(nums[mid] < nums[begin]):
                        end = mid-1
                    else:
                        begin = mid+1
        
        def binary_search(begin,end):
            while(begin <= end):
                mid = (begin+end)/2
                if(target < nums[mid]):
                    end = mid-1
                elif(target > nums[mid]):
                    begin = mid+1
                else:
                    return mid
            return -1

        min_num_pos = findMin()
        print "min->" + str(min_num_pos)
        if(nums[min_num_pos]==target):
            return min_num_pos
        if(min_num_pos == 0):
            return binary_search(0,len(nums)-1)
        if(target < nums[0]):
            return binary_search(min_num_pos,len(nums)-1)
        else:
            return binary_search(0,min_num_pos)
			
			
			
			
			
	# 新实现方式，find_min()时，while循环中的else判断是 nums[mid]>=nums[0]		
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if not nums:
			return -1
		if len(nums)==1:
			return 0 if nums[0]==target else -1
			
		def find_min():
			begin,end = 0,len(nums)-1
			if nums[begin]<nums[end]:
				return begin
			while begin<=end:
				mid = begin+(end-begin)/2
				if nums[mid]>nums[mid+1]:
					return mid+1
				else:
					if nums[mid]>=nums[0]:
						begin = mid+1
					else:
						end = mid-1
			return begin
		
		def binary_search(begin,end):
			while begin<=end:
				mid = begin+(end-begin)/2
				if nums[mid]>target:
					end = mid-1
				elif nums[mid]<target:
					begin = mid+1
				else:
					return mid
			return -1
			
		min_index = find_min()	
		#print "min_index->"+str(min_index)
		if min_index==0:
			return binary_search(0,len(nums)-1)
		if nums[0]<=target:
			return binary_search(0,min_index-1)
		else:
			return binary_search(min_index,len(nums)-1)