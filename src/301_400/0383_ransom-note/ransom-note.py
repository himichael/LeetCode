class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		"""
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		if not ransomNote:
			return True
		r_dict = dict()
		m_dict = dict()
		for i in ransomNote:
			r_dict[i] = r_dict.setdefault(i,0)+1
		for i in magazine:
			m_dict[i] = m_dict.setdefault(i,0)+1
		for key in r_dict.keys():
			if key not in m_dict:
				return False
			if r_dict[key]>m_dict[key]:
				return False
		return True