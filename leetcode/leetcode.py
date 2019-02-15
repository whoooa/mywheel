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


if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    s = Solution()
    r = s.longestCommonPrefix(strs)
    print r
