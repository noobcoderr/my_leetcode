class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        abs_x = str_x = list_x = result = 0
        if x < 0:
            abs_x = abs(x)
        else:
            abs_x = x
        str_x = str(abs_x)
        list_x = list(str_x)
        list_x.reverse()
        while list_x == '0':
            del list_x[0]
        result = ''.join(list_x)
        result = int(result)
        if x < 0:
            result = -result
        if not(-2**31 < result <2**31-1):
            result = 0
        return result

