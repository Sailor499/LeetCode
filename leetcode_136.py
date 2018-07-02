"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

"""

def siglenums(nums:list):
    tmp = 0
    for value in nums:
        tmp ^= value

    return tmp

if __name__ == '__main__':
    print(siglenums([2,2,1]))
    print(siglenums([4,1,2,1,2]))