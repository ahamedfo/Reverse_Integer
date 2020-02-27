class Solution(object):
    def reverse(self, x):
        print(str(2 ** 31 - 1))
        overflow = True
        if x > -2 ** 31 or x < 2 ** 31 - 1:
            overflow = False
            sum = 0
            k = 0
            neg = False
            for num in str(x):
                if num is "-":
                    neg = True
                    continue
                if k <= len(str(x)):
                    sum += int(num) * (10 ** k)
                    k += 1
            if neg:
                sum *= -1
            sum
        if sum < -2 ** 31 or sum > 2 ** 31 - 1 or overflow:
            return 0
        return sum
        """
        :type x: int
        :rtype: int
        """
