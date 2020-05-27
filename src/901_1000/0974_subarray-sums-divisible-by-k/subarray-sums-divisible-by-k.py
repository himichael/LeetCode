class Solution:
	def subarraysDivByK(self, A, K):
		if not A:
			return 0
		d = dict()
		d[0] = 1
		total = 0
		ans = 0
		for i in A:
			total += i
			modulus = total%K
			same = d.get(modulus,0)
			ans += same
			d[modulus] = same + 1
		return ans