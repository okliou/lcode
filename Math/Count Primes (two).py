"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


class Solution:
    #   TimeOut
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        for i in range(2, n):
            b = []
            for j in range(2, i):
                if i % j == 0:
                    b.append(j)
                    break
            if len(b) == 0:
                a += 1
        return a

    '''
    西元前250年，希腊数学家厄拉多塞(Eeatosthese)想到了一个非常美妙的质数筛法，减少了逐一检查每个数的的步骤，
    可以比较简单的从一大堆数字之中，筛选出质数来，这方法被称作厄拉多塞筛法(Sieve of Eeatosthese)。 
    具体操作：先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；
    第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；
    现在既未画圈又没有被划去的第一个数是5，将它画圈，并划去5的其他倍数……依次类推，
    一直到所有小于或等于n的各数都画了圈或划去为止。这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数。
    '''

    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        p = [True] * n
        p[0] = p[1] = False
        for i in range(2, int(n ** 0.5) + 1):  # 见底部注释
            if p[i]:
                p[i * i: n: i] = [False] * len(p[i * i: n: i])
        return sum(p)

    '''
    不必用从2到N一1的所有素数去除，只需用小于等于√N(根号N)的所有素数去除就可以了。这一点可以用反证法来证明：
    如果N是合数，则一定存在大于1小于N的整数d1和d2，使得N=d1×d2。
    如果d1和d2均大于√N，则有：N＝d1×d2>√N×√N＝N。
    而这是不可能的，所以，d1和d2中必有一个小于或等于√N。
    基于上述分析，设计算法如下：
    '''


if __name__ == '__main__':
    print(Solution().countPrimes1(499979))
