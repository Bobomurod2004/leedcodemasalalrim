class Solution(object):
    def isHappy(self, n:int):
        seen=set()
        cuur=str(n)

        while cuur not in seen:
            seen.add(cuur)
            summ=0
            for digin in cuur:
                summ += int(digin)**2

            if summ == 1:

                return True
            else:
                cuur = str(summ)

        return False

natija=Solution()
print(natija.isHappy(19))

