from typing import List


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
    print(s.isAcronym(["alice", "bob", "charlie"], "abc"))
