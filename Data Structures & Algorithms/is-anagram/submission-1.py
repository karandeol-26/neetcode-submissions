class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict_s ={}
        my_dict_t ={}

        for i in s:
            if i not in my_dict_s:
                my_dict_s[i] = 1
            else:
                my_dict_s[i] += 1

        for i in t:
            if i not in my_dict_t:
                my_dict_t[i] = 1
            else:
                my_dict_t[i] += 1

        if my_dict_s == my_dict_t:
            return True
        else:
            return False


        