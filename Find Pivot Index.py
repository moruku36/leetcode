'''
pivotIndexメソッドでは、numsの各要素に対して、左側の合計と右側の合計が等しいかどうかを判定して、最初に見つかったインデックスを返す必要があります。 そのためには、次のようなステップが必要です。

numsの全体の合計を求める。例えば、totalという名前にします。
左側の合計を保持する変数を用意します。例えば、leftという名前にします。
numsの各要素に対して、インデックスを順番に走査するために、forループとenumerate関数を使います。
各要素に対して、右側の合計を求めるために、totalから現在の要素を引きます。
左側の合計と右側の合計が等しいかどうかを判定します。もし等しければ、現在のインデックスを返します。
左側の合計に現在の要素を加えて更新します。
forループが終わったら、条件を満たすインデックスが見つからなかったことを示すために、-1を返します。

'''
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums全体の合計
        total = sum(nums)
        # 左側の合計
        left = 0
        # nums各要素とインデックスに対してループ
        for i, num in enumerate(nums):
            # 右側の合計
            right = total - num
            # 左右が等しいか判定
            if left == right:
                # インデックスを返す
                return i
            # 左側に現在値を加える
            left += num
        # 見つからなければ-1を返す
        return -1