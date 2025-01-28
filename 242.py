class Solution(object):
    def isAnagram(self, s:str, t:str):
        if len(s) != len(t):
            return False

        s_data={}
        t_data={}
        for i in range(0, len(s)):
            s_data[s[i] ] = 1 + s_data.get(s[i], 0)
            t_data[t[i]] = 1 + t_data.get(t[i], 0)
            # print(s_data, t_data)
        return  s_data == t_data
            # t_data += 1
            # print(s[i], t[i])


natija=Solution()
print(natija.isAnagram("mana","nama"))

