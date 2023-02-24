class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 新しいリストを作成
        result = []
        # 合計値を保持する変数
        total = 0
        # numsの各要素に対してループ
        for num in nums:
            # totalに現在の要素を加える
            total += num
            # totalをresultに追加する
            result.append(total)
        # resultを返す
        return result

'''
runningSumメソッドでは、numsの各要素に対して、それまでの要素の合計を計算して新しいリストに追加する必要があります。 そのためには、次のようなステップが必要です。
新しいリストを作成する。例えば、resultという名前にします。
numsの要素を順番に走査するために、forループを使います。
各要素に対して、それまでの合計を保持する変数を用意します。例えば、totalという名前にします。
totalに現在の要素を加えて更新します。
totalをresultに追加します。
forループが終わったら、resultを返します。
'''