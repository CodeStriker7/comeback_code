class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        korgan_sonlarimiz = {}
        for i, son in enumerate(nums):
            kerakli_son = target - son
            if kerakli_son in korgan_sonlarimiz:
                return [korgan_sonlarimiz[kerakli_son], i]
            korgan_sonlarimiz[son] = i


javob = Solution()
m_nums = [2,3,5,6,7,12,34,56,23,45]
m_target = 30

natija = javob.twoSum(m_nums, m_target)
print(natija)