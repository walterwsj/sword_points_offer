from typing import List
from typing import Optional, Callable, Any, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # words = ["alice","bob","charlie"], s = "abc"
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join(i[0] for i in words) == s

    # 有效括号
    def isValid(self, s: str) -> bool:
        if s[0] in ["}", "]", ")"]:
            return False
        dic = {"}": "{", "]": "[", ")": "("}
        stack = []
        for item in s:
            if stack and item in dic:
                if stack[-1] == dic[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return stack is None

    # 两数之和
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {v: i for i, v in enumerate(nums)}
        for num in nums:
            if (target - num) in num_dic and num_dic[num] != nums.index(target - num):
                return [num_dic[num], num_dic[target - num]]
        return None

    # 爬楼梯
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre = head
        cur = head.next
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        head.next = None
        return pre

    # 山脉数组
    def validMountainArray(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        if n < 3:
            return False
        l, r = 0, n - 1
        while l < n - 1 and maxHeights[l] <= maxHeights[l + 1]:
            l += 1
        while r > 0 and maxHeights[r] <= maxHeights[r - 1]:
            r -= 1
        if l == r and l != 0 and r != n - 1:
            return True
        return False

    # 美丽塔I
    def maximumSumOfHeights(self, maxHeights):
        res,n=0,len(maxHeights)
        for i in range(n):
            cur=tmp=maxHeights[i]

            for j in range(i-1,-1,-1):
                if maxHeights[j]<cur:
                    cur=maxHeights[j]
                tmp+=cur
            cur=maxHeights[i]
            for j in range(i+1,n):
                if maxHeights[j]<cur:
                    cur=maxHeights[j]
                tmp+=cur
            res=max(res,tmp)
        return res

    # nextGreaterElement下一个最大元素
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res=[]
        mapping={}
        for num in nums2:
            while stack and num>stack[-1]:
                mapping[stack[-1]]=num
                stack.pop()
            stack.append(num)    
        for num in nums1:
            if num in mapping:
                res.append(mapping[num])
            else:
                res.append(-1)
        return res

    # 每日温度
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        res=[0]*n
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx=stack.pop()
                res[idx]=i-idx
            stack.append(i)
        return res

# 最小栈
class MinStack:
    def __init__(self):
        self.slave = []
        self.master = []

    def push(self, val: int) -> None:
        if not self.slave or val <= self.slave[-1]:
            self.slave.append(val)
        self.master.append(val)

    def pop(self) -> None:
        if self.master.pop() == self.slave[-1]:
            self.slave.pop()

    def top(self) -> int:
        return self.master[-1]

    def getMin(self) -> int:
        return self.slave[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSumOfHeights([6,5,3,9,2,7]))
    xx=[i for i in range(0 - 1, -1, -1)]
    print(''.join(xx))
