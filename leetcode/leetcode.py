# coding:utf-8
from __future__ import unicode_literals


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        编写一个函数来查找字符串数组中的最长公共前缀。
        如果不存在公共前缀，返回空字符串 ""。
        示例 1:
        输入: ["flower","flow","flight"]
        输出: "fl"
        示例 2:
        输入: ["dog","racecar","car"]
        输出: ""
        解释: 输入不存在公共前缀。

        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        str_min = min([len(i) for i in strs])
        tar_str = strs[0][:str_min]
        for j in range(str_min):
            if all([x.startswith(tar_str) for x in strs]):
                return tar_str
            else:
                tar_str = tar_str[:len(tar_str) - 1]
        return ""

    def isValid(self, s):
        """
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
        有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。
        示例 1:
        输入: "()"
        输出: true
        示例 2:
        输入: "()[]{}"
        输出: true
        示例 3:
        输入: "(]"
        输出: false
        示例 4:
        输入: "([)]"
        输出: false
        示例 5:
        输入: "{[]}"
        输出: true
        :type s: str
        :rtype: bool
        """
        # if not s:
        #     return True
        # s_end = s.replace("()", "").replace("[]", "").replace("{}", "")
        # if s_end == s:
        #     return False
        # else:
        #     return self.isValid(s_end)
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            elif stack:
                s_pop = stack.pop()
                if (s_pop + i) in ["()", "[]", "{}"]:
                    continue
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        return False

    def mergeTwoLists(self, l1, l2):

        """

        将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
        示例：
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
        # class ListNode(object):
               def __init__(self, x):
               self.val = x
               self.next = None
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


if __name__ == "__main__":
    ss = "{[]}"
    s = Solution()
    r = s.isValid(ss)
    print r
