# Created by jesse at 2023/12/28 12:48
# leetgo: 1.3.13
# https://leetcode.com/problems/two-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(nums, target)

    print("\noutput:", serialize(ans))
