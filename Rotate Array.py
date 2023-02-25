'''
rotateメソッドでは、numsをk回右に回転させる必要があります。つまり、numsの末尾の要素を先頭に移動させる操作をk回繰り返します。 そのためには、次のようなステップが必要です。

kがnumsの長さ以上の場合、実際に回転する回数はkをnumsの長さで割った余りと等しいことに注意します。例えば、numsが[1,2,3]でkが4の場合、実際には1回だけ回転すればよいです。
numsを右に1回回転させるためには、numsの末尾の要素をpopメソッドで取り出して、insertメソッドで先頭に挿入します。
これをk回繰り返します。
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # kをnumsの長さで割った余りを求める
        k = k % len(nums)
        # k回ループ
        for _ in range(k):
            # numsの末尾を取り出す
            last = nums.pop()
            # numsの先頭に挿入する
            nums.insert(0, last)

'''
Time Limit Exceededというエラーは、コードが実行時間の制限を超えたことを意味します。 上記のコードでは、k回ループしてnumsの要素をpopとinsertするために、O(kn)の時間がかかります。ここでnはnumsの長さです。 もっと効率的な方法として、numsを3回反転させることで回転させることができます。その場合、O(n)の時間で済みます。 具体的には、次のようなステップが必要です。

kをnumsの長さで割った余りを求める
nums全体を反転させる
numsの先頭からk番目までを反転させる
numsのk+1番目から末尾までを反転させる
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # kをnumsの長さで割った余りを求める
        k = k % len(nums)
        # nums全体を反転する
        self.reverse(nums, 0, len(nums) - 1)
        # numsの先頭からk番目までを反転する
        self.reverse(nums, 0, k - 1)
        # numsのk+1番目から末尾までを反転する
        self.reverse(nums, k, len(nums) - 1)

    # リストの一部分を反転するヘルパーメソッド
    def reverse(self, nums, start, end):
        # startとendが交差するまでループ
        while start < end:
            # startとendの要素を入れ替える
            nums[start], nums[end] = nums[end], nums[start]
            # startはインクリメント、endはデクリメントする
            start += 1
            end -= 1