## 部署步骤
1. Fork本仓库
2. 配置GitHub Actions所需的参数
    - 点击仓库下的Settings->Secrets->New repository secret, 分别添加以下secret
        - Name:LEETCODE_EMAIL  Value:你的LeetCode账号
        - Name:LEETCODE_PASSWORD  Value:你的LeetCode密码
    - 点击[tokens](https://github.com/settings/tokens)->Generate new token
        - Note:GITHUB_TOKEN
        - Select scopes:建议全部勾选

> 重刷次数的计算规则为: 累计所有提交通过且互为不同一天的记录次数

| 最近提交时间 | 题目 | 题目难度 | 提交次数| 重刷次数 |
| ---- | ---- | ---- | ---- | ---- |
| 2021-05-26 16:04 | [#461 汉明距离](https://leetcode-cn.com/problems/hamming-distance) | EASY | 4 | **3** |
| 2021-05-26 15:07 | [#743 网络延迟时间](https://leetcode-cn.com/problems/network-delay-time) | MEDIUM | 1 | 1 |
| 2021-05-26 13:42 | [#1190 反转每对括号间的子串](https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses) | MEDIUM | 1 | 1 |
| 2021-05-25 14:33 | [#934 最短的桥](https://leetcode-cn.com/problems/shortest-bridge) | MEDIUM | 6 | 1 |
| 2021-05-24 23:56 | [#1787 使所有区间的异或结果为零](https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero) | HARD | 1 | 1 |
| 2021-05-24 23:54 | [#1162 地图分析](https://leetcode-cn.com/problems/as-far-from-land-as-possible) | MEDIUM | 8 | **3** |
| 2021-05-24 15:16 | [#664 奇怪的打印机](https://leetcode-cn.com/problems/strange-printer) | HARD | 1 | 1 |
| 2021-05-24 14:22 | [#542 01 矩阵](https://leetcode-cn.com/problems/01-matrix) | MEDIUM | 7 | **3** |
| 2021-05-24 12:58 | [#200 岛屿数量](https://leetcode-cn.com/problems/number-of-islands) | MEDIUM | 4 | **3** |
| 2021-05-23 09:26 | [#1707 与数组中元素的最大异或值](https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array) | HARD | 1 | 1 |
| 2021-05-23 09:19 | [#127 单词接龙](https://leetcode-cn.com/problems/word-ladder) | HARD | 3 | **2** |
| 2021-05-22 08:25 | [#810 黑板异或游戏](https://leetcode-cn.com/problems/chalkboard-xor-game) | HARD | 1 | 1 |
| 2021-05-21 13:13 | [#1035 不相交的线](https://leetcode-cn.com/problems/uncrossed-lines) | MEDIUM | 1 | 1 |
| 2021-05-20 14:00 | [#692 前K个高频单词](https://leetcode-cn.com/problems/top-k-frequent-words) | MEDIUM | 1 | 1 |
| 2021-05-19 14:33 | [#101 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree) | EASY | 13 | **3** |
| 2021-05-19 13:30 | [#1738 找出第 K 大的异或坐标值](https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value) | MEDIUM | 1 | 1 |
| 2021-05-19 00:30 | [#515 在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row) | MEDIUM | 1 | 1 |
| 2021-05-19 00:25 | [#429 N 叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal) | MEDIUM | 5 | 1 |
| 2021-05-18 23:43 | [#111 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) | EASY | 2 | **2** |
| 2021-05-18 23:34 | [#103 二叉树的锯齿形层序遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal) | MEDIUM | 2 | 1 |
| 2021-05-18 15:46 | [#199 二叉树的右视图](https://leetcode-cn.com/problems/binary-tree-right-side-view) | MEDIUM | 1 | 1 |
| 2021-05-18 15:20 | [#104 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) | EASY | 5 | **4** |
| 2021-05-18 14:19 | [#102 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal) | MEDIUM | 3 | **2** |
| 2021-05-18 12:56 | [#1442 形成两个异或相等数组的三元组数目](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor) | MEDIUM | 1 | 1 |
| 2021-05-17 16:48 | [#129 求根节点到叶节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers) | MEDIUM | 2 | 1 |
| 2021-05-17 15:36 | [#124 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum) | HARD | 3 | **3** |
| 2021-05-17 14:21 | [#993 二叉树的堂兄弟节点](https://leetcode-cn.com/problems/cousins-in-binary-tree) | EASY | 1 | 1 |
| 2021-05-16 14:55 | [#130 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions) | MEDIUM | 3 | 1 |
| 2021-05-16 10:30 | [#733 图像渲染](https://leetcode-cn.com/problems/flood-fill) | EASY | 7 | 1 |
| 2021-05-16 04:05 | [#421 数组中两个数的最大异或值](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array) | MEDIUM | 1 | 1 |
| 2021-05-15 11:58 | [#53 最大子序和](https://leetcode-cn.com/problems/maximum-subarray) | EASY | 16 | **5** |
| 2021-05-15 10:45 | [#279 完全平方数](https://leetcode-cn.com/problems/perfect-squares) | MEDIUM | 6 | **3** |
| 2021-05-15 09:21 | [#13 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer) | EASY | 1 | 1 |
| 2021-05-14 14:01 | [#37 解数独](https://leetcode-cn.com/problems/sudoku-solver) | HARD | 3 | **3** |
| 2021-05-13 23:09 | [#12 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman) | MEDIUM | 1 | 1 |
| 2021-05-13 15:39 | [#301 删除无效的括号](https://leetcode-cn.com/problems/remove-invalid-parentheses) | HARD | 2 | 1 |
| 2021-05-12 23:58 | [#22 括号生成](https://leetcode-cn.com/problems/generate-parentheses) | MEDIUM | 12 | **5** |
| 2021-05-12 23:40 | [#1269 停在原地的方案数](https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps) | HARD | 1 | 1 |
| 2021-05-12 22:48 | [#996 正方形数组的数目](https://leetcode-cn.com/problems/number-of-squareful-arrays) | HARD | 4 | 1 |
| 2021-05-12 13:34 | [#784 字母大小写全排列](https://leetcode-cn.com/problems/letter-case-permutation) | MEDIUM | 4 | **2** |
| 2021-05-11 23:55 | [#1310 子数组异或查询](https://leetcode-cn.com/problems/xor-queries-of-a-subarray) | MEDIUM | 1 | 1 |
| 2021-05-11 14:36 | [#47 全排列 II](https://leetcode-cn.com/problems/permutations-ii) | MEDIUM | 2 | 1 |
| 2021-05-11 13:45 | [#1734 解码异或后的排列](https://leetcode-cn.com/problems/decode-xored-permutation) | MEDIUM | 2 | 1 |
| 2021-05-11 13:38 | [#46 全排列](https://leetcode-cn.com/problems/permutations) | MEDIUM | 5 | **4** |
| 2021-05-10 13:23 | [#216 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii) | MEDIUM | 1 | 1 |
| 2021-05-09 23:50 | [#90 子集 II](https://leetcode-cn.com/problems/subsets-ii) | MEDIUM | 4 | **2** |
| 2021-05-09 23:38 | [#78 子集](https://leetcode-cn.com/problems/subsets) | MEDIUM | 4 | **4** |
| 2021-05-09 23:17 | [#77 组合](https://leetcode-cn.com/problems/combinations) | MEDIUM | 2 | **2** |
| 2021-05-09 22:52 | [#40 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii) | MEDIUM | 4 | 1 |
| 2021-05-09 22:44 | [#872 叶子相似的树](https://leetcode-cn.com/problems/leaf-similar-trees) | EASY | 2 | 1 |
| 2021-05-09 13:26 | [#39 组合总和](https://leetcode-cn.com/problems/combination-sum) | MEDIUM | 7 | **5** |
| 2021-05-09 06:02 | [#17 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number) | MEDIUM | 5 | **4** |
| 2021-05-08 17:08 | [#1482 制作 m 束花所需的最少天数](https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets) | MEDIUM | 1 | 1 |
| 2021-05-08 11:25 | [#1723 完成所有工作的最短时间](https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs) | HARD | 1 | 1 |
| 2021-05-07 15:06 | [#304 二维区域和检索 - 矩阵不可变](https://leetcode-cn.com/problems/range-sum-query-2d-immutable) | MEDIUM | 2 | **2** |
| 2021-05-07 00:24 | [#1486 数组异或操作](https://leetcode-cn.com/problems/xor-operation-in-an-array) | EASY | 1 | 1 |
| 2021-05-06 15:10 | [#221 最大正方形](https://leetcode-cn.com/problems/maximal-square) | MEDIUM | 4 | **3** |
| 2021-05-06 14:04 | [#740 删除并获得点数](https://leetcode-cn.com/problems/delete-and-earn) | MEDIUM | 2 | 1 |
| 2021-05-06 14:01 | [#1720 解码异或后的数组](https://leetcode-cn.com/problems/decode-xored-array) | EASY | 1 | 1 |
| 2021-05-05 08:48 | [#1218 最长定差子序列](https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference) | MEDIUM | 7 | 1 |
| 2021-05-05 06:45 | [#303 区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable) | EASY | 2 | **2** |
| 2021-05-05 05:56 | [#1137 第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number) | EASY | 1 | 1 |
| 2021-05-04 17:49 | [#746 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs) | EASY | 2 | 1 |
| 2021-05-04 15:25 | [#337 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii) | MEDIUM | 9 | **4** |
| 2021-05-04 13:27 | [#72 编辑距离](https://leetcode-cn.com/problems/edit-distance) | HARD | 6 | **4** |
| 2021-05-04 07:43 | [#1473 粉刷房子 III](https://leetcode-cn.com/problems/paint-house-iii) | HARD | 1 | 1 |
| 2021-05-03 15:25 | [#354 俄罗斯套娃信封问题](https://leetcode-cn.com/problems/russian-doll-envelopes) | HARD | 6 | **3** |
| 2021-05-03 13:52 | [#1143 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence) | MEDIUM | 4 | **3** |
| 2021-05-03 03:42 | [#300 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence) | MEDIUM | 9 | **4** |
| 2021-05-03 02:53 | [#7 整数反转](https://leetcode-cn.com/problems/reverse-integer) | EASY | 1 | 1 |
| 2021-05-02 12:51 | [#198 打家劫舍](https://leetcode-cn.com/problems/house-robber) | MEDIUM | 7 | **4** |
| 2021-05-02 06:12 | [#931 下降路径最小和](https://leetcode-cn.com/problems/minimum-falling-path-sum) | MEDIUM | 3 | 1 |
| 2021-05-02 02:44 | [#554 砖墙](https://leetcode-cn.com/problems/brick-wall) | MEDIUM | 1 | 1 |
| 2021-05-01 19:49 | [#剑指 Offer 63 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof) | MEDIUM | 4 | 1 |
| 2021-05-01 19:42 | [#121 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock) | EASY | 2 | **2** |
| 2021-05-01 18:27 | [#70 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | EASY | 6 | **3** |
| 2021-05-01 17:10 | [#120 三角形最小路径和](https://leetcode-cn.com/problems/triangle) | MEDIUM | 1 | 1 |
| 2021-05-01 13:57 | [#64 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum) | MEDIUM | 15 | **2** |
| 2021-05-01 13:08 | [#690 员工的重要性](https://leetcode-cn.com/problems/employee-importance) | EASY | 1 | 1 |
| 2021-05-01 03:20 | [#63 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii) | MEDIUM | 15 | **2** |
| 2021-04-30 12:34 | [#137 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii) | MEDIUM | 1 | 1 |
| 2021-04-29 14:38 | [#62 不同路径](https://leetcode-cn.com/problems/unique-paths) | MEDIUM | 4 | **2** |
| 2021-04-29 14:27 | [#403 青蛙过河](https://leetcode-cn.com/problems/frog-jump) | HARD | 1 | 1 |
| 2021-04-29 03:10 | [#518 零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2) | MEDIUM | 11 | **3** |
| 2021-04-29 03:00 | [#322 零钱兑换](https://leetcode-cn.com/problems/coin-change) | MEDIUM | 8 | **3** |
| 2021-04-28 15:20 | [#416 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum) | MEDIUM | 11 | **5** |
| 2021-04-28 13:09 | [#633 平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers) | MEDIUM | 3 | 1 |
| 2021-04-27 13:16 | [#938 二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst) | EASY | 2 | 1 |
| 2021-04-26 12:22 | [#1011 在 D 天内送达包裹的能力](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days) | MEDIUM | 1 | 1 |
| 2021-04-25 03:19 | [#897 递增顺序搜索树](https://leetcode-cn.com/problems/increasing-order-search-tree) | EASY | 1 | 1 |
| 2021-04-24 12:47 | [#377 组合总和 Ⅳ](https://leetcode-cn.com/problems/combination-sum-iv) | MEDIUM | 1 | 1 |
| 2021-04-23 13:27 | [#368 最大整除子集](https://leetcode-cn.com/problems/largest-divisible-subset) | MEDIUM | 1 | 1 |
| 2021-04-22 13:23 | [#363 矩形区域不超过 K 的最大数值和](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k) | HARD | 1 | 1 |
| 2021-04-21 12:51 | [#91 解码方法](https://leetcode-cn.com/problems/decode-ways) | MEDIUM | 1 | 1 |
| 2021-04-20 15:56 | [#341 扁平化嵌套列表迭代器](https://leetcode-cn.com/problems/flatten-nested-list-iterator) | MEDIUM | 3 | **2** |
| 2021-04-19 16:34 | [#28 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr) | EASY | 1 | 1 |
| 2021-04-19 13:53 | [#27 移除元素](https://leetcode-cn.com/problems/remove-element) | EASY | 1 | 1 |
| 2021-04-18 05:44 | [#26 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | EASY | 1 | 1 |
| 2021-04-17 13:36 | [#220 存在重复元素 III](https://leetcode-cn.com/problems/contains-duplicate-iii) | MEDIUM | 1 | 1 |
| 2021-04-16 02:27 | [#87 扰乱字符串](https://leetcode-cn.com/problems/scramble-string) | HARD | 1 | 1 |
| 2021-04-15 13:01 | [#213 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii) | MEDIUM | 3 | **2** |
| 2021-04-14 15:39 | [#206 反转链表](https://leetcode-cn.com/problems/reverse-linked-list) | EASY | 4 | **3** |
| 2021-04-14 14:04 | [#208 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree) | MEDIUM | 1 | 1 |
| 2021-04-13 14:03 | [#530 二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst) | EASY | 2 | 1 |
| 2021-04-13 13:56 | [#783 二叉搜索树节点最小距离](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes) | EASY | 2 | 1 |
| 2021-04-12 17:14 | [#739 每日温度](https://leetcode-cn.com/problems/daily-temperatures) | MEDIUM | 2 | **2** |
| 2021-04-12 15:52 | [#496 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i) | EASY | 1 | 1 |
| 2021-04-12 14:52 | [#236 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree) | MEDIUM | 3 | **2** |
| 2021-04-12 14:15 | [#222 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes) | MEDIUM | 1 | 1 |
| 2021-04-12 13:41 | [#179 最大数](https://leetcode-cn.com/problems/largest-number) | MEDIUM | 1 | 1 |
| 2021-04-11 14:39 | [#450 删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst) | MEDIUM | 1 | 1 |
| 2021-04-11 13:57 | [#700 二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree) | EASY | 1 | 1 |
| 2021-04-11 13:27 | [#98 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree) | MEDIUM | 16 | **3** |
| 2021-04-11 13:01 | [#145 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal) | EASY | 1 | 1 |
| 2021-04-11 12:40 | [#460 LFU 缓存](https://leetcode-cn.com/problems/lfu-cache) | HARD | 2 | **2** |
| 2021-04-11 09:59 | [#264 丑数 II](https://leetcode-cn.com/problems/ugly-number-ii) | MEDIUM | 1 | 1 |
| 2021-04-10 10:21 | [#146 LRU 缓存机制](https://leetcode-cn.com/problems/lru-cache) | MEDIUM | 7 | **3** |
| 2021-04-10 10:04 | [#263 丑数](https://leetcode-cn.com/problems/ugly-number) | EASY | 1 | 1 |
| 2021-04-09 12:34 | [#154 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii) | HARD | 1 | 1 |
| 2021-04-08 12:48 | [#153 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array) | MEDIUM | 1 | 1 |
| 2021-04-07 13:47 | [#81 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii) | MEDIUM | 1 | 1 |
| 2021-04-06 13:06 | [#80 删除有序数组中的重复项 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii) | MEDIUM | 1 | 1 |
| 2021-04-05 12:52 | [#494 目标和](https://leetcode-cn.com/problems/target-sum) | MEDIUM | 4 | **2** |
| 2021-04-05 04:43 | [#88 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) | EASY | 2 | **2** |
| 2021-04-05 02:30 | [#312 戳气球](https://leetcode-cn.com/problems/burst-balloons) | HARD | 6 | **2** |
| 2021-04-04 14:20 | [#887 鸡蛋掉落](https://leetcode-cn.com/problems/super-egg-drop) | HARD | 10 | **2** |
| 2021-04-04 03:00 | [#10 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching) | HARD | 3 | **2** |
| 2021-04-04 01:07 | [#781 森林中的兔子](https://leetcode-cn.com/problems/rabbits-in-forest) | MEDIUM | 1 | 1 |
| 2021-04-03 15:54 | [#1312 让字符串成为回文串的最少插入次数](https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome) | HARD | 1 | 1 |
| 2021-04-03 12:48 | [#516 最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence) | MEDIUM | 1 | 1 |
| 2021-04-02 13:04 | [#面试题 17.21 直方图的水量](https://leetcode-cn.com/problems/volume-of-histogram-lcci) | HARD | 1 | 1 |
| 2021-04-01 13:05 | [#1006 笨阶乘](https://leetcode-cn.com/problems/clumsy-factorial) | MEDIUM | 1 | 1 |
| 2021-03-30 13:11 | [#74 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix) | MEDIUM | 1 | 1 |
| 2021-03-29 13:21 | [#173 二叉搜索树迭代器](https://leetcode-cn.com/problems/binary-search-tree-iterator) | MEDIUM | 1 | 1 |
| 2021-03-29 13:20 | [#190 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits) | EASY | 1 | 1 |
| 2021-03-27 12:32 | [#61 旋转链表](https://leetcode-cn.com/problems/rotate-list) | MEDIUM | 1 | 1 |
| 2021-03-26 13:31 | [#83 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list) | EASY | 1 | 1 |
| 2021-03-25 13:49 | [#82 删除排序链表中的重复元素 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii) | MEDIUM | 1 | 1 |
| 2021-03-24 13:27 | [#456 132 模式](https://leetcode-cn.com/problems/132-pattern) | MEDIUM | 1 | 1 |
| 2021-03-22 13:11 | [#191 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits) | EASY | 1 | 1 |
| 2021-03-21 09:56 | [#73 矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes) | MEDIUM | 1 | 1 |
| 2021-03-20 08:49 | [#150 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation) | MEDIUM | 1 | 1 |
| 2021-03-19 12:23 | [#1603 设计停车系统](https://leetcode-cn.com/problems/design-parking-system) | EASY | 1 | 1 |
| 2021-03-18 13:07 | [#92 反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii) | MEDIUM | 1 | 1 |
| 2021-03-18 13:06 | [#59 螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii) | MEDIUM | 2 | **2** |
| 2021-03-17 12:48 | [#115 不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences) | HARD | 1 | 1 |
| 2021-03-15 12:37 | [#54 螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix) | MEDIUM | 1 | 1 |
| 2021-03-14 12:40 | [#706 设计哈希映射](https://leetcode-cn.com/problems/design-hashmap) | EASY | 1 | 1 |
| 2021-03-13 05:03 | [#705 设计哈希集合](https://leetcode-cn.com/problems/design-hashset) | EASY | 1 | 1 |
| 2021-03-12 13:25 | [#331 验证二叉树的前序序列化](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree) | MEDIUM | 1 | 1 |
| 2021-03-11 14:11 | [#227 基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii) | MEDIUM | 1 | 1 |
| 2021-03-10 13:22 | [#224 基本计算器](https://leetcode-cn.com/problems/basic-calculator) | HARD | 1 | 1 |
| 2021-03-09 14:13 | [#1047 删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string) | EASY | 1 | 1 |
| 2021-03-08 13:32 | [#132 分割回文串 II](https://leetcode-cn.com/problems/palindrome-partitioning-ii) | HARD | 2 | 1 |
| 2021-03-07 15:02 | [#131 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning) | MEDIUM | 1 | 1 |
| 2021-03-06 13:11 | [#503 下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-ii) | MEDIUM | 1 | 1 |
| 2021-03-05 13:48 | [#232 用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks) | EASY | 1 | 1 |
| 2021-03-03 13:25 | [#338 比特位计数](https://leetcode-cn.com/problems/counting-bits) | EASY | 4 | **3** |
| 2021-02-28 11:35 | [#896 单调数列](https://leetcode-cn.com/problems/monotonic-array) | EASY | 2 | 1 |
| 2021-02-27 13:00 | [#395 至少有 K 个重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters) | MEDIUM | 1 | 1 |
| 2021-02-26 12:31 | [#1178 猜字谜](https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle) | HARD | 1 | 1 |
| 2021-02-25 13:22 | [#867 转置矩阵](https://leetcode-cn.com/problems/transpose-matrix) | EASY | 1 | 1 |
| 2021-02-24 13:26 | [#832 翻转图像](https://leetcode-cn.com/problems/flipping-an-image) | EASY | 1 | 1 |
| 2021-02-23 12:27 | [#1052 爱生气的书店老板](https://leetcode-cn.com/problems/grumpy-bookstore-owner) | MEDIUM | 1 | 1 |
| 2021-02-22 13:03 | [#766 托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix) | EASY | 1 | 1 |
| 2021-02-20 17:21 | [#1438 绝对差不超过限制的最长连续子数组](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit) | MEDIUM | 1 | 1 |
| 2021-02-19 18:51 | [#697 数组的度](https://leetcode-cn.com/problems/degree-of-an-array) | EASY | 1 | 1 |
| 2021-02-19 05:01 | [#1004 最大连续1的个数 III](https://leetcode-cn.com/problems/max-consecutive-ones-iii) | MEDIUM | 1 | 1 |
| 2021-02-18 03:47 | [#995 K 连续位的最小翻转次数](https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips) | HARD | 3 | 1 |
| 2021-02-17 05:54 | [#566 重塑矩阵](https://leetcode-cn.com/problems/reshape-the-matrix) | EASY | 1 | 1 |
| 2021-02-16 02:55 | [#561 数组拆分 I](https://leetcode-cn.com/problems/array-partition-i) | EASY | 1 | 1 |
| 2021-02-15 02:40 | [#485 最大连续 1 的个数](https://leetcode-cn.com/problems/max-consecutive-ones) | EASY | 1 | 1 |
| 2021-02-14 07:32 | [#765 情侣牵手](https://leetcode-cn.com/problems/couples-holding-hands) | HARD | 1 | 1 |
| 2021-02-13 04:59 | [#119 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii) | EASY | 1 | 1 |
| 2021-02-13 04:58 | [#448 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array) | EASY | 3 | **2** |
| 2021-02-11 03:11 | [#703 数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream) | EASY | 1 | 1 |
| 2021-02-10 12:49 | [#567 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string) | MEDIUM | 1 | 1 |
| 2021-02-09 02:30 | [#992 K 个不同整数的子数组](https://leetcode-cn.com/problems/subarrays-with-k-different-integers) | HARD | 1 | 1 |
| 2021-02-08 05:40 | [#978 最长湍流子数组](https://leetcode-cn.com/problems/longest-turbulent-subarray) | MEDIUM | 2 | 1 |
| 2021-02-07 11:33 | [#665 非递减数列](https://leetcode-cn.com/problems/non-decreasing-array) | EASY | 1 | 1 |
| 2021-02-06 14:20 | [#1423 可获得的最大点数](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards) | MEDIUM | 1 | 1 |
| 2021-02-05 13:42 | [#1208 尽可能使字符串相等](https://leetcode-cn.com/problems/get-equal-substrings-within-budget) | MEDIUM | 3 | 1 |
| 2021-02-04 14:16 | [#643 子数组最大平均数 I](https://leetcode-cn.com/problems/maximum-average-subarray-i) | EASY | 1 | 1 |
| 2021-02-03 13:31 | [#480 滑动窗口中位数](https://leetcode-cn.com/problems/sliding-window-median) | HARD | 1 | 1 |
| 2021-02-02 15:08 | [#424 替换后的最长重复字符](https://leetcode-cn.com/problems/longest-repeating-character-replacement) | MEDIUM | 1 | 1 |
| 2021-02-01 13:47 | [#888 公平的糖果棒交换](https://leetcode-cn.com/problems/fair-candy-swap) | EASY | 1 | 1 |
| 2021-01-30 16:28 | [#839 相似字符串组](https://leetcode-cn.com/problems/similar-string-groups) | HARD | 1 | 1 |
| 2021-01-30 02:39 | [#778 水位上升的泳池中游泳](https://leetcode-cn.com/problems/swim-in-rising-water) | HARD | 1 | 1 |
| 2021-01-29 13:51 | [#1631 最小体力消耗路径](https://leetcode-cn.com/problems/path-with-minimum-effort) | MEDIUM | 1 | 1 |
| 2021-01-28 13:12 | [#724 寻找数组的中心下标](https://leetcode-cn.com/problems/find-pivot-index) | EASY | 2 | **2** |
| 2021-01-27 12:29 | [#1579 保证图可完全遍历](https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable) | HARD | 1 | 1 |
| 2021-01-26 13:51 | [#1128 等价多米诺骨牌对的数量](https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs) | EASY | 1 | 1 |
| 2021-01-25 12:36 | [#959 由斜杠划分区域](https://leetcode-cn.com/problems/regions-cut-by-slashes) | MEDIUM | 1 | 1 |
| 2021-01-24 12:09 | [#674 最长连续递增序列](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence) | EASY | 1 | 1 |
| 2021-01-23 12:27 | [#1319 连通网络的操作次数](https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected) | MEDIUM | 1 | 1 |
| 2021-01-22 12:27 | [#989 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer) | EASY | 1 | 1 |
| 2021-01-21 14:05 | [#1489 找到最小生成树里的关键边和伪关键边](https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree) | HARD | 1 | 1 |
| 2021-01-20 13:46 | [#628 三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers) | EASY | 2 | 1 |
| 2021-01-19 14:42 | [#1584 连接所有点的最小费用](https://leetcode-cn.com/problems/min-cost-to-connect-all-points) | MEDIUM | 1 | 1 |
| 2021-01-18 12:59 | [#721 账户合并](https://leetcode-cn.com/problems/accounts-merge) | MEDIUM | 1 | 1 |
| 2021-01-17 08:50 | [#1232 缀点成线](https://leetcode-cn.com/problems/check-if-it-is-a-straight-line) | EASY | 1 | 1 |
| 2021-01-16 13:59 | [#803 打砖块](https://leetcode-cn.com/problems/bricks-falling-when-hit) | HARD | 1 | 1 |
| 2021-01-15 12:54 | [#947 移除最多的同行或同列石头](https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column) | MEDIUM | 1 | 1 |
| 2021-01-14 13:10 | [#1018 可被 5 整除的二进制前缀](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5) | EASY | 1 | 1 |
| 2021-01-13 13:53 | [#684 冗余连接](https://leetcode-cn.com/problems/redundant-connection) | MEDIUM | 1 | 1 |
| 2021-01-12 12:52 | [#1203 项目管理](https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies) | HARD | 1 | 1 |
| 2021-01-11 13:53 | [#1202 交换字符串中的元素](https://leetcode-cn.com/problems/smallest-string-with-swaps) | MEDIUM | 1 | 1 |
| 2021-01-10 06:32 | [#228 汇总区间](https://leetcode-cn.com/problems/summary-ranges) | EASY | 2 | 1 |
| 2021-01-09 12:55 | [#123 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii) | HARD | 1 | 1 |
| 2021-01-08 12:56 | [#189 旋转数组](https://leetcode-cn.com/problems/rotate-array) | MEDIUM | 1 | 1 |
| 2021-01-07 13:47 | [#547 省份数量](https://leetcode-cn.com/problems/number-of-provinces) | MEDIUM | 1 | 1 |
| 2021-01-06 13:20 | [#399 除法求值](https://leetcode-cn.com/problems/evaluate-division) | MEDIUM | 3 | **2** |
| 2021-01-05 13:29 | [#830 较大分组的位置](https://leetcode-cn.com/problems/positions-of-large-groups) | EASY | 3 | 1 |
| 2021-01-04 05:35 | [#509 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number) | EASY | 1 | 1 |
| 2021-01-03 08:11 | [#86 分隔链表](https://leetcode-cn.com/problems/partition-list) | MEDIUM | 1 | 1 |
| 2021-01-02 04:59 | [#94 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) | EASY | 5 | **3** |
| 2021-01-02 04:13 | [#144 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal) | EASY | 1 | 1 |
| 2021-01-02 03:39 | [#239 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum) | HARD | 3 | **2** |
| 2020-12-31 18:01 | [#605 种花问题](https://leetcode-cn.com/problems/can-place-flowers) | EASY | 1 | 1 |
| 2020-12-10 14:20 | [#860 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change) | EASY | 1 | 1 |
| 2020-04-14 13:53 | [#445 两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii) | MEDIUM | 1 | 1 |
| 2020-04-13 13:33 | [#355 设计推特](https://leetcode-cn.com/problems/design-twitter) | MEDIUM | 1 | 1 |
| 2020-04-10 13:42 | [#151 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string) | MEDIUM | 1 | 1 |
| 2020-04-08 13:52 | [#剑指 Offer 13 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof) | MEDIUM | 1 | 1 |
| 2020-04-07 09:19 | [#面试题 01.07 旋转矩阵](https://leetcode-cn.com/problems/rotate-matrix-lcci) | MEDIUM | 1 | 1 |
| 2020-04-04 12:42 | [#42 接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | HARD | 2 | **2** |
| 2020-04-03 14:58 | [#8 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi) | MEDIUM | 1 | 1 |
| 2020-04-02 11:58 | [#289 生命游戏](https://leetcode-cn.com/problems/game-of-life) | MEDIUM | 1 | 1 |
| 2020-04-01 14:16 | [#1111 有效括号的嵌套深度](https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings) | MEDIUM | 1 | 1 |
| 2020-03-30 02:10 | [#剑指 Offer 62 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof) | EASY | 1 | 1 |
| 2020-03-26 13:07 | [#999 可以被一步捕获的棋子数](https://leetcode-cn.com/problems/available-captures-for-rook) | EASY | 1 | 1 |
| 2020-03-24 09:49 | [#面试题 17.16 按摩师](https://leetcode-cn.com/problems/the-masseuse-lcci) | EASY | 1 | 1 |
| 2020-03-22 12:09 | [#945 使数组唯一的最小增量](https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique) | MEDIUM | 1 | 1 |
| 2020-03-21 09:40 | [#365 水壶问题](https://leetcode-cn.com/problems/water-and-jug-problem) | MEDIUM | 1 | 1 |
| 2020-03-20 12:55 | [#剑指 Offer 40 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof) | EASY | 3 | 1 |
| 2020-03-19 12:51 | [#409 最长回文串](https://leetcode-cn.com/problems/longest-palindrome) | EASY | 1 | 1 |
| 2020-03-18 14:01 | [#836 矩形重叠](https://leetcode-cn.com/problems/rectangle-overlap) | EASY | 5 | 1 |
| 2020-03-17 13:36 | [#1160 拼写单词](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters) | EASY | 2 | 1 |
| 2020-03-16 07:28 | [#面试题 01.06 字符串压缩](https://leetcode-cn.com/problems/compress-string-lcci) | EASY | 1 | 1 |
| 2020-03-15 06:45 | [#695 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island) | MEDIUM | 1 | 1 |
| 2020-03-13 15:46 | [#169 多数元素](https://leetcode-cn.com/problems/majority-element) | EASY | 3 | **2** |
| 2020-02-26 07:16 | [#剑指 Offer 10- I 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof) | EASY | 2 | 1 |
| 2020-02-26 07:07 | [#剑指 Offer 09 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof) | EASY | 2 | 1 |
| 2020-02-26 07:01 | [#剑指 Offer 07 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof) | MEDIUM | 1 | 1 |
| 2020-02-26 06:57 | [#剑指 Offer 06 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof) | EASY | 1 | 1 |
| 2020-02-26 06:51 | [#剑指 Offer 05 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof) | EASY | 1 | 1 |
| 2020-02-12 10:04 | [#剑指 Offer 04 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof) | MEDIUM | 1 | 1 |
| 2020-02-12 10:02 | [#剑指 Offer 03 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof) | EASY | 1 | 1 |
| 2020-02-11 15:09 | [#96 不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees) | MEDIUM | 2 | **2** |
| 2020-02-11 08:04 | [#136 只出现一次的数字](https://leetcode-cn.com/problems/single-number) | EASY | 2 | **2** |
| 2020-02-11 07:15 | [#3 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters) | MEDIUM | 6 | **2** |
| 2020-02-11 06:54 | [#79 单词搜索](https://leetcode-cn.com/problems/word-search) | MEDIUM | 2 | **2** |
| 2020-02-11 05:13 | [#617 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees) | EASY | 3 | **3** |
| 2020-02-10 16:50 | [#538 把二叉搜索树转换为累加树](https://leetcode-cn.com/problems/convert-bst-to-greater-tree) | MEDIUM | 5 | **3** |
| 2020-02-10 16:45 | [#437 路径总和 III](https://leetcode-cn.com/problems/path-sum-iii) | MEDIUM | 3 | **3** |
| 2020-01-20 08:38 | [#148 排序链表](https://leetcode-cn.com/problems/sort-list) | MEDIUM | 3 | **2** |
| 2020-01-20 07:44 | [#56 合并区间](https://leetcode-cn.com/problems/merge-intervals) | MEDIUM | 4 | **2** |
| 2020-01-20 07:04 | [#406 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height) | MEDIUM | 1 | 1 |
| 2020-01-17 06:45 | [#114 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list) | MEDIUM | 5 | **2** |
| 2020-01-16 10:38 | [#226 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree) | EASY | 2 | **2** |
| 2020-01-16 08:44 | [#297 二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree) | HARD | 4 | **3** |
| 2020-01-14 07:14 | [#543 二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree) | EASY | 10 | **2** |
| 2020-01-03 15:07 | [#647 回文子串](https://leetcode-cn.com/problems/palindromic-substrings) | MEDIUM | 3 | 1 |
| 2020-01-03 06:15 | [#621 任务调度器](https://leetcode-cn.com/problems/task-scheduler) | MEDIUM | 1 | 1 |
| 2020-01-03 05:20 | [#581 最短无序连续子数组](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray) | MEDIUM | 6 | 1 |
| 2020-01-02 15:38 | [#560 和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k) | MEDIUM | 3 | 1 |
| 2019-12-30 14:28 | [#438 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string) | MEDIUM | 1 | 1 |
| 2019-12-30 06:43 | [#394 字符串解码](https://leetcode-cn.com/problems/decode-string) | MEDIUM | 2 | 1 |
| 2019-12-24 07:29 | [#347 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements) | MEDIUM | 2 | 1 |
| 2019-12-19 15:51 | [#309 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) | MEDIUM | 1 | 1 |
| 2019-12-16 09:58 | [#287 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number) | MEDIUM | 1 | 1 |
| 2019-12-16 09:30 | [#283 移动零](https://leetcode-cn.com/problems/move-zeroes) | EASY | 7 | 1 |
| 2019-12-15 10:09 | [#5 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring) | MEDIUM | 8 | **2** |
| 2019-12-13 15:14 | [#240 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii) | MEDIUM | 1 | 1 |
| 2019-12-13 07:50 | [#238 除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self) | MEDIUM | 1 | 1 |
| 2019-12-12 15:46 | [#234 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list) | EASY | 1 | 1 |
| 2019-12-11 15:40 | [#215 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array) | MEDIUM | 2 | 1 |
| 2019-12-10 15:27 | [#160 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists) | EASY | 2 | 1 |
| 2019-12-10 14:34 | [#155 最小栈](https://leetcode-cn.com/problems/min-stack) | EASY | 5 | 1 |
| 2019-12-10 05:17 | [#139 单词拆分](https://leetcode-cn.com/problems/word-break) | MEDIUM | 2 | **2** |
| 2019-12-09 10:18 | [#152 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray) | MEDIUM | 2 | 1 |
| 2019-12-06 09:45 | [#142 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii) | MEDIUM | 1 | 1 |
| 2019-12-06 09:34 | [#141 环形链表](https://leetcode-cn.com/problems/linked-list-cycle) | EASY | 3 | 1 |
| 2019-12-05 14:40 | [#128 最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence) | MEDIUM | 1 | 1 |
| 2019-12-01 06:09 | [#105 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) | MEDIUM | 1 | 1 |
| 2019-11-27 09:56 | [#84 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram) | HARD | 1 | 1 |
| 2019-11-26 14:20 | [#43 字符串相乘](https://leetcode-cn.com/problems/multiply-strings) | MEDIUM | 1 | 1 |
| 2019-11-25 06:48 | [#76 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring) | HARD | 1 | 1 |
| 2019-11-24 04:27 | [#75 颜色分类](https://leetcode-cn.com/problems/sort-colors) | MEDIUM | 2 | 1 |
| 2019-11-20 13:30 | [#55 跳跃游戏](https://leetcode-cn.com/problems/jump-game) | MEDIUM | 1 | 1 |
| 2019-11-20 08:18 | [#49 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams) | MEDIUM | 9 | 1 |
| 2019-11-19 13:45 | [#48 旋转图像](https://leetcode-cn.com/problems/rotate-image) | MEDIUM | 2 | 1 |
| 2019-11-13 07:51 | [#34 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array) | MEDIUM | 1 | 1 |
| 2019-11-13 06:50 | [#33 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array) | MEDIUM | 4 | **2** |
| 2019-11-12 06:46 | [#32 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses) | HARD | 4 | 1 |
| 2019-11-12 05:46 | [#31 下一个排列](https://leetcode-cn.com/problems/next-permutation) | MEDIUM | 1 | 1 |
| 2019-11-12 05:29 | [#23 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists) | HARD | 2 | **2** |
| 2019-11-08 09:25 | [#21 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | EASY | 2 | 1 |
| 2019-11-08 08:17 | [#20 有效的括号](https://leetcode-cn.com/problems/valid-parentheses) | EASY | 3 | 1 |
| 2019-11-08 07:08 | [#19 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list) | MEDIUM | 4 | 1 |
| 2019-11-06 08:14 | [#15 三数之和](https://leetcode-cn.com/problems/3sum) | MEDIUM | 4 | 1 |
| 2019-11-06 06:46 | [#11 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | MEDIUM | 1 | 1 |
| 2019-11-05 07:02 | [#4 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays) | HARD | 3 | 1 |
| 2019-11-04 10:16 | [#2 两数相加](https://leetcode-cn.com/problems/add-two-numbers) | MEDIUM | 3 | 1 |
| 2019-11-04 08:22 | [#1 两数之和](https://leetcode-cn.com/problems/two-sum) | EASY | 4 | 1 |
