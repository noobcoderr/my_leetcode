class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        """
        dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        lists = list(s)
        length = len(lists)
        sum1=sum2=sum3=sum4=sum5=sum6=0
        i = 0
        if length == 1:
            return dict1[lists[0]]
        elif length == 2:
            if dict1[lists[0]] < dict1[lists[1]]:
                sum1 = dict1[lists[1]]-dict1[lists[0]]
                return sum1
            elif dict1[lists[0]] >= dict1[lists[1]]:
                sum2 = dict1[lists[1]]+dict1[lists[0]]
                return sum2
        elif length > 2:
            while i < length:
                if dict1[lists[i]] >= dict1[lists[i+1]]:
                    sum3 += dict1[lists[i]]
                    if i == length-2:
                        sum3 += dict1[lists[length-1]]
                        break
                    i += 1
                elif dict1[lists[i]] < dict1[lists[i+1]]:
                    sums = dict1[lists[i+1]]-dict1[lists[i]]
                    sum3 += sums
                    if i == length-2:
                        break
                    i += 2
                    if i == length-1:
                        sum3 += dict1[lists[length-1]]
                        break
            return sum3

