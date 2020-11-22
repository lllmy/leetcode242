# 有效的字母异位词
# 给定两个字符串 s 和 t ，
# 编写一个函数来判断 t 是否是 s 的字母异位词。


def isanagram(s,t):
    # 第一种方法排序 时间复杂度高 sort 就是按照ascii值排序的
    return True if sorted(s) == sorted(t) else False
    # 另外一种方法根据集合  时间复杂度低
    # if len(s) != len(t):
    #     return False
    # s1 = set(s)
    # for i in s1:
    #     if s.count(i) != t.count(i):
    #         return False
    # else:
    #     return True



# print(isanagram("anagram","nagaram"))
print(isanagram("tar","car"))