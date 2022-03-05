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

| 最近提交 | 题目 | 题目难度 | 提交 | 重刷 |
| ---- | ---- | ---- | ---- | ---- |
| 2022-03-05 18:18 | [#521 最长特殊序列 Ⅰ](https://leetcode-cn.com/problems/longest-uncommon-subsequence-i) | ★ | 1 | 1 |
| 2022-03-04 19:56 | [#2104 子数组范围和](https://leetcode-cn.com/problems/sum-of-subarray-ranges) | ★★ | 1 | 1 |
| 2022-03-03 21:47 | [#258 各位相加](https://leetcode-cn.com/problems/add-digits) | ★ | 1 | 1 |
| 2022-03-02 21:46 | [#564 寻找最近的回文数](https://leetcode-cn.com/problems/find-the-closest-palindrome) | ★★★ | 1 | 1 |
| 2022-03-01 17:07 | [#6 Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion) | ★★ | 1 | 1 |
| 2022-02-28 20:52 | [#1601 最多可达成的换楼请求数目](https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests) | ★★★ | 1 | 1 |
| 2022-02-27 20:16 | [#553 最优除法](https://leetcode-cn.com/problems/optimal-division) | ★★ | 1 | 1 |
| 2022-02-26 13:24 | [#2016 增量元素之间的最大差值](https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements) | ★ | 3 | 1 |
| 2022-02-25 21:53 | [#537 复数乘法](https://leetcode-cn.com/problems/complex-number-multiplication) | ★★ | 2 | 1 |
| 2022-02-24 20:28 | [#1706 球会落何处](https://leetcode-cn.com/problems/where-will-the-ball-fall) | ★★ | 1 | 1 |
| 2022-02-23 23:13 | [#917 仅仅反转字母](https://leetcode-cn.com/problems/reverse-only-letters) | ★ | 4 | 1 |
| 2022-02-22 21:09 | [#1994 好子集的数目](https://leetcode-cn.com/problems/the-number-of-good-subsets) | ★★★ | 1 | 1 |
| 2022-02-21 19:33 | [#838 推多米诺](https://leetcode-cn.com/problems/push-dominoes) | ★★ | 1 | 1 |
| 2022-02-20 16:43 | [#717 1 比特与 2 比特字符](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters) | ★ | 1 | 1 |
| 2022-02-19 20:34 | [#969 煎饼排序](https://leetcode-cn.com/problems/pancake-sorting) | ★★ | 1 | 1 |
| 2022-02-18 21:55 | [#1791 找出星型图的中心节点](https://leetcode-cn.com/problems/find-center-of-star-graph) | ★ | 2 | 1 |
| 2022-02-17 21:50 | [#1389 按既定顺序创建目标数组](https://leetcode-cn.com/problems/create-target-array-in-the-given-order) | ★ | 1 | 1 |
| 2022-02-17 21:38 | [#1385 两个数组间的距离值](https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays) | ★ | 1 | 1 |
| 2022-02-17 21:07 | [#1374 生成每种字符都是奇数个的字符串](https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts) | ★ | 1 | 1 |
| 2022-02-17 20:39 | [#688 骑士在棋盘上的概率](https://leetcode-cn.com/problems/knight-probability-in-chessboard) | ★★ | 1 | 1 |
| 2022-02-16 22:14 | [#2053 数组中第 K 个独一无二的字符串](https://leetcode-cn.com/problems/kth-distinct-string-in-an-array) | ★ | 1 | 1 |
| 2022-02-16 21:13 | [#1719 重构一棵树的方案数](https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree) | ★★★ | 1 | 1 |
| 2022-02-15 22:20 | [#459 重复的子字符串](https://leetcode-cn.com/problems/repeated-substring-pattern) | ★ | 4 | 1 |
| 2022-02-15 21:46 | [#1380 矩阵中的幸运数](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix) | ★ | 1 | 1 |
| 2022-02-14 20:28 | [#2148 元素计数](https://leetcode-cn.com/problems/count-elements-with-strictly-smaller-and-greater-elements) | ★ | 2 | 1 |
| 2022-02-14 17:56 | [#540 有序数组中的单一元素](https://leetcode-cn.com/problems/single-element-in-a-sorted-array) | ★★ | 4 | 1 |
| 2022-02-13 16:05 | [#1189 “气球” 的最大数量](https://leetcode-cn.com/problems/maximum-number-of-balloons) | ★ | 1 | 1 |
| 2022-02-12 03:40 | [#1020 飞地的数量](https://leetcode-cn.com/problems/number-of-enclaves) | ★★ | 1 | 1 |
| 2022-02-11 20:14 | [#1984 学生分数的最小差值](https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores) | ★ | 1 | 1 |
| 2022-02-10 20:33 | [#1447 最简分数](https://leetcode-cn.com/problems/simplified-fractions) | ★★ | 1 | 1 |
| 2022-02-09 23:23 | [#2006 差的绝对值为 K 的数对数目](https://leetcode-cn.com/problems/count-number-of-pairs-with-absolute-difference-k) | ★ | 2 | 1 |
| 2022-02-08 12:11 | [#1001 网格照明](https://leetcode-cn.com/problems/grid-illumination) | ★★★ | 1 | 1 |
| 2022-02-07 02:58 | [#1405 最长快乐字符串](https://leetcode-cn.com/problems/longest-happy-string) | ★★ | 3 | 1 |
| 2022-02-06 16:16 | [#1219 黄金矿工](https://leetcode-cn.com/problems/path-with-maximum-gold) | ★★ | 3 | 2 |
| 2022-02-06 00:20 | [#1748 唯一元素的和](https://leetcode-cn.com/problems/sum-of-unique-elements) | ★ | 2 | 1 |
| 2022-02-04 21:24 | [#1725 可以形成最大正方形的矩形数目](https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square) | ★ | 2 | 1 |
| 2022-02-03 17:28 | [#1414 和为 K 的最少斐波那契数字数目](https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k) | ★★ | 7 | 1 |
| 2022-02-02 11:03 | [#2000 反转单词前缀](https://leetcode-cn.com/problems/reverse-prefix-of-word) | ★ | 1 | 1 |
| 2022-02-01 23:28 | [#1763 最长的美好子字符串](https://leetcode-cn.com/problems/longest-nice-substring) | ★ | 5 | 1 |
| 2022-01-31 13:02 | [#1342 将数字变成 0 的操作次数](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero) | ★ | 1 | 1 |
| 2022-01-30 14:40 | [#884 两句话中的不常见单词](https://leetcode-cn.com/problems/uncommon-words-from-two-sentences) | ★ | 3 | 1 |
| 2022-01-29 13:45 | [#1765 地图中的最高点](https://leetcode-cn.com/problems/map-of-highest-peak) | ★★ | 1 | 1 |
| 2022-01-28 23:16 | [#1996 游戏中弱角色的数量](https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game) | ★★ | 4 | 1 |
| 2022-01-27 17:24 | [#2047 句子中的有效单词数](https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence) | ★ | 5 | 1 |
| 2022-01-26 20:43 | [#2013 检测正方形](https://leetcode-cn.com/problems/detect-squares) | ★★ | 1 | 1 |
| 2022-01-25 21:02 | [#1688 比赛中的配对次数](https://leetcode-cn.com/problems/count-of-matches-in-tournament) | ★ | 1 | 1 |
| 2022-01-24 19:45 | [#2045 到达目的地的第二短时间](https://leetcode-cn.com/problems/second-minimum-time-to-reach-destination) | ★★★ | 1 | 1 |
| 2022-01-23 12:32 | [#2034 股票价格波动](https://leetcode-cn.com/problems/stock-price-fluctuation) | ★★ | 2 | 1 |
| 2022-01-22 15:40 | [#1332 删除回文子序列](https://leetcode-cn.com/problems/remove-palindromic-subsequences) | ★ | 1 | 1 |
| 2022-01-21 17:12 | [#1345 跳跃游戏 IV](https://leetcode-cn.com/problems/jump-game-iv) | ★★★ | 4 | 1 |
| 2022-01-20 16:53 | [#2029 石子游戏 IX](https://leetcode-cn.com/problems/stone-game-ix) | ★★ | 1 | 1 |
| 2022-01-19 12:44 | [#438 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string) | ★★ | 4 | **3** |
| 2022-01-19 11:53 | [#219 存在重复元素 II](https://leetcode-cn.com/problems/contains-duplicate-ii) | ★ | 4 | 1 |
| 2022-01-18 17:31 | [#539 最小时间差](https://leetcode-cn.com/problems/minimum-time-difference) | ★★ | 3 | 1 |
| 2022-01-17 18:10 | [#1220 统计元音字母序列的数目](https://leetcode-cn.com/problems/count-vowels-permutation) | ★★★ | 1 | 1 |
| 2022-01-16 16:51 | [#382 链表随机节点](https://leetcode-cn.com/problems/linked-list-random-node) | ★★ | 1 | 1 |
| 2022-01-15 12:17 | [#1716 计算力扣银行的钱](https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank) | ★ | 1 | 1 |
| 2022-01-14 21:11 | [#373 查找和最小的 K 对数字](https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums) | ★★ | 14 | **3** |
| 2022-01-13 23:28 | [#747 至少是其他数字两倍的最大数](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others) | ★ | 1 | 1 |
| 2022-01-12 21:13 | [#334 递增的三元子序列](https://leetcode-cn.com/problems/increasing-triplet-subsequence) | ★★ | 1 | 1 |
| 2022-01-11 22:22 | [#28 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr) | ★ | 6 | 2 |
| 2022-01-11 22:10 | [#1036 逃离大迷宫](https://leetcode-cn.com/problems/escape-a-large-maze) | ★★★ | 1 | 1 |
| 2022-01-11 00:40 | [#640 求解方程](https://leetcode-cn.com/problems/solve-the-equation) | ★★ | 5 | 1 |
| 2022-01-10 22:47 | [#306 累加数](https://leetcode-cn.com/problems/additive-number) | ★★ | 1 | 1 |
| 2022-01-10 22:36 | [#1876 长度为三且各字符不同的子字符串](https://leetcode-cn.com/problems/substrings-of-size-three-with-distinct-characters) | ★ | 2 | 1 |
| 2022-01-09 17:14 | [#1629 按键持续时间最长的键](https://leetcode-cn.com/problems/slowest-key) | ★ | 2 | 1 |
| 2022-01-08 23:02 | [#89 格雷编码](https://leetcode-cn.com/problems/gray-code) | ★★ | 1 | 1 |
| 2022-01-07 20:05 | [#1614 括号的最大嵌套深度](https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses) | ★ | 1 | 1 |
| 2022-01-06 20:47 | [#71 简化路径](https://leetcode-cn.com/problems/simplify-path) | ★★ | 1 | 1 |
| 2022-01-05 20:32 | [#1576 替换所有的问号](https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters) | ★ | 1 | 1 |
| 2022-01-05 15:33 | [#463 岛屿的周长](https://leetcode-cn.com/problems/island-perimeter) | ★ | 6 | 1 |
| 2022-01-04 21:01 | [#913 猫和老鼠](https://leetcode-cn.com/problems/cat-and-mouse) | ★★★ | 1 | 1 |
| 2022-01-03 01:06 | [#1185 一周中的第几天](https://leetcode-cn.com/problems/day-of-the-week) | ★ | 1 | 1 |
| 2022-01-03 01:06 | [#390 消除游戏](https://leetcode-cn.com/problems/elimination-game) | ★★ | 1 | 1 |
| 2022-01-01 19:58 | [#2022 将一维数组转变成二维数组](https://leetcode-cn.com/problems/convert-1d-array-into-2d-array) | ★ | 1 | 1 |
| 2021-12-31 01:20 | [#507 完美数](https://leetcode-cn.com/problems/perfect-number) | ★ | 1 | 1 |
| 2021-12-30 21:09 | [#846 一手顺子](https://leetcode-cn.com/problems/hand-of-straights) | ★★ | 1 | 1 |
| 2021-12-29 22:34 | [#912 排序数组](https://leetcode-cn.com/problems/sort-an-array) | ★★ | 4 | 2 |
| 2021-12-29 21:37 | [#1995 统计特殊四元组](https://leetcode-cn.com/problems/count-special-quadruplets) | ★ | 1 | 1 |
| 2021-12-28 21:39 | [#472 连接词](https://leetcode-cn.com/problems/concatenated-words) | ★★★ | 1 | 1 |
| 2021-12-28 00:56 | [#51 N 皇后](https://leetcode-cn.com/problems/n-queens) | ★★★ | 7 | 1 |
| 2021-12-27 19:44 | [#825 适龄的朋友](https://leetcode-cn.com/problems/friends-of-appropriate-ages) | ★★ | 1 | 1 |
| 2021-12-26 20:34 | [#1078 Bigram 分词](https://leetcode-cn.com/problems/occurrences-after-bigram) | ★ | 1 | 1 |
| 2021-12-25 20:47 | [#1609 奇偶树](https://leetcode-cn.com/problems/even-odd-tree) | ★★ | 1 | 1 |
| 2021-12-24 21:08 | [#1705 吃苹果的最大数目](https://leetcode-cn.com/problems/maximum-number-of-eaten-apples) | ★★ | 1 | 1 |
| 2021-12-23 23:41 | [#111 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) | ★ | 3 | **3** |
| 2021-12-23 23:34 | [#199 二叉树的右视图](https://leetcode-cn.com/problems/binary-tree-right-side-view) | ★★ | 4 | **3** |
| 2021-12-23 23:29 | [#104 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) | ★ | 7 | **6** |
| 2021-12-23 23:18 | [#102 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal) | ★★ | 5 | **4** |
| 2021-12-23 22:34 | [#124 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum) | ★★★ | 6 | **5** |
| 2021-12-23 22:27 | [#129 求根节点到叶节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers) | ★★ | 4 | **3** |
| 2021-12-23 22:23 | [#1044 最长重复子串](https://leetcode-cn.com/problems/longest-duplicate-substring) | ★★★ | 1 | 1 |
| 2021-12-22 23:12 | [#993 二叉树的堂兄弟节点](https://leetcode-cn.com/problems/cousins-in-binary-tree) | ★ | 2 | 2 |
| 2021-12-22 23:03 | [#130 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions) | ★★ | 4 | 2 |
| 2021-12-22 22:20 | [#200 岛屿数量](https://leetcode-cn.com/problems/number-of-islands) | ★★ | 6 | **4** |
| 2021-12-22 21:13 | [#733 图像渲染](https://leetcode-cn.com/problems/flood-fill) | ★ | 8 | 2 |
| 2021-12-22 20:31 | [#686 重复叠加字符串匹配](https://leetcode-cn.com/problems/repeated-string-match) | ★★ | 1 | 1 |
| 2021-12-21 21:16 | [#1154 一年中的第几天](https://leetcode-cn.com/problems/day-of-the-year) | ★ | 1 | 1 |
| 2021-12-20 23:28 | [#46 全排列](https://leetcode-cn.com/problems/permutations) | ★★ | 6 | **5** |
| 2021-12-20 23:11 | [#78 子集](https://leetcode-cn.com/problems/subsets) | ★★ | 7 | **6** |
| 2021-12-20 23:03 | [#77 组合](https://leetcode-cn.com/problems/combinations) | ★★ | 3 | **3** |
| 2021-12-20 22:56 | [#40 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii) | ★★ | 6 | 2 |
| 2021-12-20 22:36 | [#39 组合总和](https://leetcode-cn.com/problems/combination-sum) | ★★ | 9 | **6** |
| 2021-12-20 22:22 | [#17 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number) | ★★ | 6 | **5** |
| 2021-12-20 16:17 | [#475 供暖器](https://leetcode-cn.com/problems/heaters) | ★★ | 1 | 1 |
| 2021-12-19 23:09 | [#1289 下降路径最小和  II](https://leetcode-cn.com/problems/minimum-falling-path-sum-ii) | ★★★ | 6 | 2 |
| 2021-12-19 22:59 | [#120 三角形最小路径和](https://leetcode-cn.com/problems/triangle) | ★★ | 3 | **3** |
| 2021-12-19 22:35 | [#63 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii) | ★★ | 18 | **4** |
| 2021-12-19 21:37 | [#62 不同路径](https://leetcode-cn.com/problems/unique-paths) | ★★ | 7 | **5** |
| 2021-12-19 20:11 | [#997 找到小镇的法官](https://leetcode-cn.com/problems/find-the-town-judge) | ★ | 1 | 1 |
| 2021-12-18 19:32 | [#419 甲板上的战舰](https://leetcode-cn.com/problems/battleships-in-a-board) | ★★ | 1 | 1 |
| 2021-12-17 18:40 | [#1518 换酒问题](https://leetcode-cn.com/problems/water-bottles) | ★ | 1 | 1 |
| 2021-12-16 21:15 | [#1610 可见点的最大数目](https://leetcode-cn.com/problems/maximum-number-of-visible-points) | ★★★ | 1 | 1 |
| 2021-12-15 21:18 | [#851 喧闹和富有](https://leetcode-cn.com/problems/loud-and-rich) | ★★ | 1 | 1 |
| 2021-12-14 21:56 | [#630 课程表 III](https://leetcode-cn.com/problems/course-schedule-iii) | ★★★ | 1 | 1 |
| 2021-12-13 17:12 | [#807 保持城市天际线](https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline) | ★★ | 1 | 1 |
| 2021-12-12 21:30 | [#709 转换成小写字母](https://leetcode-cn.com/problems/to-lower-case) | ★ | 1 | 1 |
| 2021-12-11 20:06 | [#911 在线选举](https://leetcode-cn.com/problems/online-election) | ★★ | 1 | 1 |
| 2021-12-10 21:29 | [#748 最短补全词](https://leetcode-cn.com/problems/shortest-completing-word) | ★ | 1 | 1 |
| 2021-12-09 21:00 | [#794 有效的井字游戏](https://leetcode-cn.com/problems/valid-tic-tac-toe-state) | ★★ | 1 | 1 |
| 2021-12-08 20:37 | [#689 三个无重叠子数组的最大和](https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays) | ★★★ | 1 | 1 |
| 2021-12-07 21:57 | [#1034 边界着色](https://leetcode-cn.com/problems/coloring-a-border) | ★★ | 1 | 1 |
| 2021-12-06 21:25 | [#1816 截断句子](https://leetcode-cn.com/problems/truncate-sentence) | ★ | 1 | 1 |
| 2021-12-05 21:53 | [#372 超级次方](https://leetcode-cn.com/problems/super-pow) | ★★ | 1 | 1 |
| 2021-12-04 20:34 | [#383 赎金信](https://leetcode-cn.com/problems/ransom-note) | ★ | 1 | 1 |
| 2021-12-03 20:44 | [#1005 K 次取反后最大化的数组和](https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations) | ★ | 1 | 1 |
| 2021-12-02 20:11 | [#506 相对名次](https://leetcode-cn.com/problems/relative-ranks) | ★ | 1 | 1 |
| 2021-12-01 22:13 | [#1446 连续字符](https://leetcode-cn.com/problems/consecutive-characters) | ★ | 2 | 1 |
| 2021-11-30 22:40 | [#400 第 N 位数字](https://leetcode-cn.com/problems/nth-digit) | ★★ | 1 | 1 |
| 2021-11-29 18:14 | [#786 第 K 个最小的素数分数](https://leetcode-cn.com/problems/k-th-smallest-prime-fraction) | ★★★ | 1 | 1 |
| 2021-11-27 20:39 | [#519 随机翻转矩阵](https://leetcode-cn.com/problems/random-flip-matrix) | ★★ | 1 | 1 |
| 2021-11-26 22:12 | [#700 二叉搜索树中的搜索](https://leetcode-cn.com/problems/search-in-a-binary-search-tree) | ★ | 2 | 2 |
| 2021-11-25 22:38 | [#458 可怜的小猪](https://leetcode-cn.com/problems/poor-pigs) | ★★★ | 1 | 1 |
| 2021-11-24 21:03 | [#423 从英文中重建数字](https://leetcode-cn.com/problems/reconstruct-original-digits-from-english) | ★★ | 1 | 1 |
| 2021-11-23 20:44 | [#859 亲密字符串](https://leetcode-cn.com/problems/buddy-strings) | ★ | 1 | 1 |
| 2021-11-22 18:07 | [#384 打乱数组](https://leetcode-cn.com/problems/shuffle-an-array) | ★★ | 1 | 1 |
| 2021-11-21 17:42 | [#559 N 叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree) | ★ | 1 | 1 |
| 2021-11-20 11:10 | [#594 最长和谐子序列](https://leetcode-cn.com/problems/longest-harmonious-subsequence) | ★ | 1 | 1 |
| 2021-11-19 21:53 | [#397 整数替换](https://leetcode-cn.com/problems/integer-replacement) | ★★ | 1 | 1 |
| 2021-11-18 21:55 | [#563 二叉树的坡度](https://leetcode-cn.com/problems/binary-tree-tilt) | ★ | 1 | 1 |
| 2021-11-17 22:18 | [#318 最大单词长度乘积](https://leetcode-cn.com/problems/maximum-product-of-word-lengths) | ★★ | 1 | 1 |
| 2021-11-16 22:11 | [#391 完美矩形](https://leetcode-cn.com/problems/perfect-rectangle) | ★★★ | 1 | 1 |
| 2021-11-15 17:18 | [#319 灯泡开关](https://leetcode-cn.com/problems/bulb-switcher) | ★★ | 1 | 1 |
| 2021-11-14 15:16 | [#677 键值映射](https://leetcode-cn.com/problems/map-sum-pairs) | ★★ | 1 | 1 |
| 2021-11-14 15:15 | [#520 检测大写字母](https://leetcode-cn.com/problems/detect-capital) | ★ | 2 | 2 |
| 2021-11-12 21:12 | [#375 猜数字大小 II](https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii) | ★★ | 1 | 1 |
| 2021-11-11 21:29 | [#629 K个逆序对数组](https://leetcode-cn.com/problems/k-inverse-pairs-array) | ★★★ | 1 | 1 |
| 2021-11-10 22:18 | [#495 提莫攻击](https://leetcode-cn.com/problems/teemo-attacking) | ★ | 1 | 1 |
| 2021-11-09 21:34 | [#488 祖玛游戏](https://leetcode-cn.com/problems/zuma-game) | ★★★ | 1 | 1 |
| 2021-11-08 10:52 | [#299 猜数字游戏](https://leetcode-cn.com/problems/bulls-and-cows) | ★★ | 1 | 1 |
| 2021-11-07 19:42 | [#598 范围求和 II](https://leetcode-cn.com/problems/range-addition-ii) | ★ | 1 | 1 |
| 2021-11-06 17:32 | [#268 丢失的数字](https://leetcode-cn.com/problems/missing-number) | ★ | 1 | 1 |
| 2021-11-05 17:43 | [#1218 最长定差子序列](https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference) | ★★ | 8 | 2 |
| 2021-11-04 22:03 | [#367 有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square) | ★ | 1 | 1 |
| 2021-11-03 21:10 | [#407 接雨水 II](https://leetcode-cn.com/problems/trapping-rain-water-ii) | ★★★ | 1 | 1 |
| 2021-11-02 21:36 | [#237 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list) | ★ | 2 | 2 |
| 2021-11-01 21:53 | [#575 分糖果](https://leetcode-cn.com/problems/distribute-candies) | ★ | 1 | 1 |
| 2021-10-31 03:31 | [#500 键盘行](https://leetcode-cn.com/problems/keyboard-row) | ★ | 1 | 1 |
| 2021-10-30 19:18 | [#260 只出现一次的数字 III](https://leetcode-cn.com/problems/single-number-iii) | ★★ | 1 | 1 |
| 2021-10-29 22:17 | [#335 路径交叉](https://leetcode-cn.com/problems/self-crossing) | ★★★ | 1 | 1 |
| 2021-10-28 21:07 | [#869 重新排序得到 2 的幂](https://leetcode-cn.com/problems/reordered-power-of-2) | ★★ | 1 | 1 |
| 2021-10-27 21:18 | [#301 删除无效的括号](https://leetcode-cn.com/problems/remove-invalid-parentheses) | ★★★ | 3 | 2 |
| 2021-10-26 22:02 | [#496 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i) | ★ | 4 | **3** |
| 2021-10-25 21:07 | [#240 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii) | ★★ | 2 | 2 |
| 2021-10-24 19:55 | [#638 大礼包](https://leetcode-cn.com/problems/shopping-offers) | ★★ | 1 | 1 |
| 2021-10-23 20:55 | [#492 构造矩形](https://leetcode-cn.com/problems/construct-the-rectangle) | ★ | 1 | 1 |
| 2021-10-22 21:48 | [#229 求众数 II](https://leetcode-cn.com/problems/majority-element-ii) | ★★ | 1 | 1 |
| 2021-10-21 21:25 | [#66 加一](https://leetcode-cn.com/problems/plus-one) | ★ | 1 | 1 |
| 2021-10-20 21:05 | [#453 最小操作次数使数组元素相等](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements) | ★ | 1 | 1 |
| 2021-10-19 21:54 | [#211 添加与搜索单词 - 数据结构设计](https://leetcode-cn.com/problems/design-add-and-search-words-data-structure) | ★★ | 1 | 1 |
| 2021-10-18 16:56 | [#476 数字的补数](https://leetcode-cn.com/problems/number-complement) | ★ | 1 | 1 |
| 2021-10-17 00:40 | [#230 二叉搜索树中第K小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst) | ★★ | 1 | 1 |
| 2021-10-16 17:04 | [#282 给表达式添加运算符](https://leetcode-cn.com/problems/expression-add-operators) | ★★★ | 1 | 1 |
| 2021-10-15 21:53 | [#38 外观数列](https://leetcode-cn.com/problems/count-and-say) | ★★ | 1 | 1 |
| 2021-10-14 21:05 | [#剑指 Offer II 069 山峰数组的顶部](https://leetcode-cn.com/problems/B1IidL) | ★ | 1 | 1 |
| 2021-10-13 20:58 | [#412 Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz) | ★ | 1 | 1 |
| 2021-10-12 20:56 | [#29 两数相除](https://leetcode-cn.com/problems/divide-two-integers) | ★★ | 2 | 1 |
| 2021-10-11 17:19 | [#273 整数转换英文表示](https://leetcode-cn.com/problems/integer-to-english-words) | ★★★ | 1 | 1 |
| 2021-10-10 14:36 | [#441 排列硬币](https://leetcode-cn.com/problems/arranging-coins) | ★ | 1 | 1 |
| 2021-10-09 04:12 | [#352 将数据流变为多个不相交区间](https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals) | ★★★ | 1 | 1 |
| 2021-10-08 16:46 | [#187 重复的DNA序列](https://leetcode-cn.com/problems/repeated-dna-sequences) | ★★ | 1 | 1 |
| 2021-10-07 15:01 | [#434 字符串中的单词数](https://leetcode-cn.com/problems/number-of-segments-in-a-string) | ★ | 1 | 1 |
| 2021-10-06 00:18 | [#414 第三大的数](https://leetcode-cn.com/problems/third-maximum-number) | ★ | 1 | 1 |
| 2021-10-05 18:01 | [#284 顶端迭代器](https://leetcode-cn.com/problems/peeking-iterator) | ★★ | 2 | 1 |
| 2021-10-04 13:18 | [#482 密钥格式化](https://leetcode-cn.com/problems/license-key-formatting) | ★ | 1 | 1 |
| 2021-10-03 09:21 | [#166 分数到小数](https://leetcode-cn.com/problems/fraction-to-recurring-decimal) | ★★ | 1 | 1 |
| 2021-10-02 17:46 | [#1436 旅行终点站](https://leetcode-cn.com/problems/destination-city) | ★ | 1 | 1 |
| 2021-10-02 17:45 | [#405 数字转换为十六进制数](https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal) | ★ | 1 | 1 |
| 2021-09-30 21:13 | [#223 矩形面积](https://leetcode-cn.com/problems/rectangle-area) | ★★ | 1 | 1 |
| 2021-09-29 21:36 | [#517 超级洗衣机](https://leetcode-cn.com/problems/super-washing-machines) | ★★★ | 1 | 1 |
| 2021-09-28 20:39 | [#437 路径总和 III](https://leetcode-cn.com/problems/path-sum-iii) | ★★ | 4 | **4** |
| 2021-09-27 22:48 | [#639 解码方法 II](https://leetcode-cn.com/problems/decode-ways-ii) | ★★★ | 1 | 1 |
| 2021-09-26 02:34 | [#371 两整数之和](https://leetcode-cn.com/problems/sum-of-two-integers) | ★★ | 2 | 1 |
| 2021-09-25 20:59 | [#583 两个字符串的删除操作](https://leetcode-cn.com/problems/delete-operation-for-two-strings) | ★★ | 1 | 1 |
| 2021-09-24 21:44 | [#430 扁平化多级双向链表](https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list) | ★★ | 1 | 1 |
| 2021-09-23 20:55 | [#326 3 的幂](https://leetcode-cn.com/problems/power-of-three) | ★ | 1 | 1 |
| 2021-09-22 20:50 | [#725 分隔链表](https://leetcode-cn.com/problems/split-linked-list-in-parts) | ★★ | 1 | 1 |
| 2021-09-21 21:35 | [#58 最后一个单词的长度](https://leetcode-cn.com/problems/length-of-last-word) | ★ | 1 | 1 |
| 2021-09-20 16:10 | [#650 只有两个键的键盘](https://leetcode-cn.com/problems/2-keys-keyboard) | ★★ | 3 | 1 |
| 2021-09-20 16:08 | [#673 最长递增子序列的个数](https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence) | ★★ | 1 | 1 |
| 2021-09-18 16:56 | [#292 Nim 游戏](https://leetcode-cn.com/problems/nim-game) | ★ | 1 | 1 |
| 2021-09-17 22:55 | [#36 有效的数独](https://leetcode-cn.com/problems/valid-sudoku) | ★★ | 2 | 1 |
| 2021-09-16 21:42 | [#212 单词搜索 II](https://leetcode-cn.com/problems/word-search-ii) | ★★★ | 1 | 1 |
| 2021-09-15 20:45 | [#162 寻找峰值](https://leetcode-cn.com/problems/find-peak-element) | ★★ | 2 | 2 |
| 2021-09-14 18:23 | [#524 通过删除字母匹配到字典里最长单词](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting) | ★★ | 1 | 1 |
| 2021-09-13 20:25 | [#447 回旋镖的数量](https://leetcode-cn.com/problems/number-of-boomerangs) | ★★ | 1 | 1 |
| 2021-09-12 20:01 | [#678 有效的括号字符串](https://leetcode-cn.com/problems/valid-parenthesis-string) | ★★ | 1 | 1 |
| 2021-09-11 18:26 | [#600 不含连续1的非负整数](https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones) | ★★★ | 1 | 1 |
| 2021-09-10 21:20 | [#1894 找到需要补充粉笔的学生编号](https://leetcode-cn.com/problems/find-the-student-that-will-replace-the-chalk) | ★★ | 1 | 1 |
| 2021-09-09 21:45 | [#68 文本左右对齐](https://leetcode-cn.com/problems/text-justification) | ★★★ | 1 | 1 |
| 2021-09-08 20:38 | [#502 IPO](https://leetcode-cn.com/problems/ipo) | ★★★ | 1 | 1 |
| 2021-09-07 21:47 | [#1221 分割平衡字符串](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings) | ★ | 1 | 1 |
| 2021-09-06 22:06 | [#704 二分查找](https://leetcode-cn.com/problems/binary-search) | ★ | 8 | **4** |
| 2021-09-05 20:55 | [#470 用 Rand7() 实现 Rand10()](https://leetcode-cn.com/problems/implement-rand10-using-rand7) | ★★ | 1 | 1 |
| 2021-09-04 20:45 | [#剑指 Offer 10- I 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof) | ★ | 3 | 2 |
| 2021-09-03 21:11 | [#面试题 17.14 最小K个数](https://leetcode-cn.com/problems/smallest-k-lcci) | ★★ | 1 | 1 |
| 2021-09-02 20:43 | [#剑指 Offer 22 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof) | ★ | 1 | 1 |
| 2021-09-01 20:44 | [#165 比较版本号](https://leetcode-cn.com/problems/compare-version-numbers) | ★★ | 1 | 1 |
| 2021-08-31 20:56 | [#1109 航班预订统计](https://leetcode-cn.com/problems/corporate-flight-bookings) | ★★ | 1 | 1 |
| 2021-08-30 21:12 | [#528 按权重随机选择](https://leetcode-cn.com/problems/random-pick-with-weight) | ★★ | 1 | 1 |
| 2021-08-29 19:28 | [#1588 所有奇数长度子数组的和](https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays) | ★ | 1 | 1 |
| 2021-08-28 19:46 | [#1480 一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array) | ★ | 1 | 1 |
| 2021-08-27 22:43 | [#295 数据流的中位数](https://leetcode-cn.com/problems/find-median-from-data-stream) | ★★★ | 2 | 1 |
| 2021-08-26 20:40 | [#881 救生艇](https://leetcode-cn.com/problems/boats-to-save-people) | ★★ | 1 | 1 |
| 2021-08-25 20:54 | [#797 所有可能的路径](https://leetcode-cn.com/problems/all-paths-from-source-to-target) | ★★ | 1 | 1 |
| 2021-08-24 20:43 | [#787 K 站中转内最便宜的航班](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops) | ★★ | 5 | 1 |
| 2021-08-23 20:35 | [#1646 获取生成数组中的最大值](https://leetcode-cn.com/problems/get-maximum-in-generated-array) | ★ | 1 | 1 |
| 2021-08-22 20:29 | [#789 逃脱阻碍者](https://leetcode-cn.com/problems/escape-the-ghosts) | ★★ | 1 | 1 |
| 2021-08-21 20:44 | [#443 压缩字符串](https://leetcode-cn.com/problems/string-compression) | ★★ | 1 | 1 |
| 2021-08-20 21:50 | [#541 反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii) | ★ | 1 | 1 |
| 2021-08-19 20:48 | [#345 反转字符串中的元音字母](https://leetcode-cn.com/problems/reverse-vowels-of-a-string) | ★ | 1 | 1 |
| 2021-08-18 20:40 | [#552 学生出勤记录 II](https://leetcode-cn.com/problems/student-attendance-record-ii) | ★★★ | 1 | 1 |
| 2021-08-17 21:13 | [#551 学生出勤记录 I](https://leetcode-cn.com/problems/student-attendance-record-i) | ★ | 1 | 1 |
| 2021-08-16 21:16 | [#526 优美的排列](https://leetcode-cn.com/problems/beautiful-arrangement) | ★★ | 1 | 1 |
| 2021-08-15 21:24 | [#576 出界的路径数](https://leetcode-cn.com/problems/out-of-boundary-paths) | ★★ | 1 | 1 |
| 2021-08-14 20:33 | [#1583 统计不开心的朋友](https://leetcode-cn.com/problems/count-unhappy-friends) | ★★ | 1 | 1 |
| 2021-08-13 20:58 | [#233 数字 1 的个数](https://leetcode-cn.com/problems/number-of-digit-one) | ★★★ | 1 | 1 |
| 2021-08-12 21:05 | [#516 最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence) | ★★ | 2 | 2 |
| 2021-08-11 21:37 | [#446 等差数列划分 II - 子序列](https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence) | ★★★ | 1 | 1 |
| 2021-08-10 21:21 | [#413 等差数列划分](https://leetcode-cn.com/problems/arithmetic-slices) | ★★ | 1 | 1 |
| 2021-08-09 22:41 | [#313 超级丑数](https://leetcode-cn.com/problems/super-ugly-number) | ★★ | 1 | 1 |
| 2021-08-08 14:22 | [#1137 第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number) | ★ | 2 | 2 |
| 2021-08-07 21:42 | [#457 环形数组是否存在循环](https://leetcode-cn.com/problems/circular-array-loop) | ★★ | 1 | 1 |
| 2021-08-06 15:47 | [#847 访问所有节点的最短路径](https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes) | ★★★ | 1 | 1 |
| 2021-08-05 21:11 | [#802 找到最终的安全状态](https://leetcode-cn.com/problems/find-eventual-safe-states) | ★★ | 1 | 1 |
| 2021-08-04 20:21 | [#611 有效三角形的个数](https://leetcode-cn.com/problems/valid-triangle-number) | ★★ | 1 | 1 |
| 2021-08-03 21:21 | [#581 最短无序连续子数组](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray) | ★★ | 7 | 2 |
| 2021-08-02 20:18 | [#743 网络延迟时间](https://leetcode-cn.com/problems/network-delay-time) | ★★ | 3 | 2 |
| 2021-08-01 20:04 | [#1337 矩阵中战斗力最弱的 K 行](https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix) | ★ | 1 | 1 |
| 2021-07-31 02:20 | [#987 二叉树的垂序遍历](https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree) | ★★★ | 1 | 1 |
| 2021-07-30 20:18 | [#171 Excel 表列序号](https://leetcode-cn.com/problems/excel-sheet-column-number) | ★ | 1 | 1 |
| 2021-07-30 20:17 | [#1104 二叉树寻路](https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree) | ★★ | 2 | 2 |
| 2021-07-28 21:15 | [#863 二叉树中所有距离为 K 的结点](https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree) | ★★ | 1 | 1 |
| 2021-07-27 20:16 | [#671 二叉树中第二小的节点](https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree) | ★ | 1 | 1 |
| 2021-07-26 17:06 | [#1713 得到子序列的最少操作次数](https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence) | ★★★ | 1 | 1 |
| 2021-07-25 20:45 | [#1743 从相邻元素对还原数组](https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs) | ★★ | 1 | 1 |
| 2021-07-24 20:22 | [#1736 替换隐藏数字得到的最晚时间](https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits) | ★ | 1 | 1 |
| 2021-07-23 20:58 | [#1893 检查是否区域内所有整数都被覆盖](https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered) | ★ | 1 | 1 |
| 2021-07-22 21:09 | [#138 复制带随机指针的链表](https://leetcode-cn.com/problems/copy-list-with-random-pointer) | ★★ | 6 | **3** |
| 2021-07-21 21:59 | [#1575 统计所有可行路径](https://leetcode-cn.com/problems/count-all-possible-routes) | ★★★ | 2 | 2 |
| 2021-07-21 21:09 | [#剑指 Offer 52 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof) | ★ | 1 | 1 |
| 2021-07-20 22:39 | [#931 下降路径最小和](https://leetcode-cn.com/problems/minimum-falling-path-sum) | ★★ | 5 | 2 |
| 2021-07-20 17:30 | [#121 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock) | ★ | 3 | **3** |
| 2021-07-20 17:22 | [#350 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii) | ★ | 1 | 1 |
| 2021-07-20 16:48 | [#88 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) | ★ | 4 | **3** |
| 2021-07-20 16:32 | [#1 两数之和](https://leetcode-cn.com/problems/two-sum) | ★ | 5 | 2 |
| 2021-07-20 16:23 | [#1877 数组中最大数对和的最小值](https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array) | ★★ | 1 | 1 |
| 2021-07-19 22:17 | [#64 最小路径和](https://leetcode-cn.com/problems/minimum-path-sum) | ★★ | 16 | **3** |
| 2021-07-19 07:43 | [#1838 最高频元素的频数](https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element) | ★★ | 1 | 1 |
| 2021-07-18 14:58 | [#53 最大子数组和](https://leetcode-cn.com/problems/maximum-subarray) | ★ | 19 | **7** |
| 2021-07-18 14:50 | [#217 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate) | ★ | 3 | 1 |
| 2021-07-18 11:50 | [#189 轮转数组](https://leetcode-cn.com/problems/rotate-array) | ★★ | 2 | 2 |
| 2021-07-18 11:28 | [#977 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array) | ★ | 1 | 1 |
| 2021-07-18 10:08 | [#面试题 10.02 变位词组](https://leetcode-cn.com/problems/group-anagrams-lcci) | ★★ | 1 | 1 |
| 2021-07-17 17:13 | [#35 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position) | ★ | 5 | 2 |
| 2021-07-17 17:13 | [#278 第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version) | ★ | 3 | **3** |
| 2021-07-17 16:31 | [#341 扁平化嵌套列表迭代器](https://leetcode-cn.com/problems/flatten-nested-list-iterator) | ★★ | 5 | **4** |
| 2021-07-17 14:42 | [#1603 设计停车系统](https://leetcode-cn.com/problems/design-parking-system) | ★ | 4 | **3** |
| 2021-07-17 14:34 | [#剑指 Offer 42 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof) | ★ | 1 | 1 |
| 2021-07-16 21:28 | [#421 数组中两个数的最大异或值](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array) | ★★ | 2 | 2 |
| 2021-07-16 20:40 | [#剑指 Offer 53 - I 在排序数组中查找数字 I](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof) | ★ | 1 | 1 |
| 2021-07-16 16:08 | [#208 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree) | ★★ | 2 | 2 |
| 2021-07-15 22:10 | [#703 数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream) | ★ | 6 | **4** |
| 2021-07-15 21:13 | [#706 设计哈希映射](https://leetcode-cn.com/problems/design-hashmap) | ★ | 2 | 2 |
| 2021-07-15 20:47 | [#1846 减小和重新排列数组后的最大元素](https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging) | ★★ | 1 | 1 |
| 2021-07-14 22:04 | [#1818 绝对差值和](https://leetcode-cn.com/problems/minimum-absolute-sum-difference) | ★★ | 1 | 1 |
| 2021-07-14 17:26 | [#705 设计哈希集合](https://leetcode-cn.com/problems/design-hashset) | ★ | 2 | 2 |
| 2021-07-14 15:20 | [#155 最小栈](https://leetcode-cn.com/problems/min-stack) | ★ | 7 | 2 |
| 2021-07-14 14:58 | [#面试题 03.01 三合一](https://leetcode-cn.com/problems/three-in-one-lcci) | ★ | 2 | 1 |
| 2021-07-13 22:24 | [#225 用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues) | ★ | 1 | 1 |
| 2021-07-13 22:14 | [#232 用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks) | ★ | 2 | 2 |
| 2021-07-13 20:46 | [#218 天际线问题](https://leetcode-cn.com/problems/the-skyline-problem) | ★★★ | 1 | 1 |
| 2021-07-12 18:09 | [#274 H 指数](https://leetcode-cn.com/problems/h-index) | ★★ | 1 | 1 |
| 2021-07-12 18:07 | [#275 H 指数 II](https://leetcode-cn.com/problems/h-index-ii) | ★★ | 1 | 1 |
| 2021-07-12 00:20 | [#887 鸡蛋掉落](https://leetcode-cn.com/problems/super-egg-drop) | ★★★ | 13 | **3** |
| 2021-07-10 20:58 | [#981 基于时间的键值存储](https://leetcode-cn.com/problems/time-based-key-value-store) | ★★ | 1 | 1 |
| 2021-07-09 20:41 | [#面试题 17.10 主要元素](https://leetcode-cn.com/problems/find-majority-element-lcci) | ★ | 1 | 1 |
| 2021-07-08 21:35 | [#930 和相同的二元子数组](https://leetcode-cn.com/problems/binary-subarrays-with-sum) | ★★ | 1 | 1 |
| 2021-07-07 21:43 | [#1711 大餐计数](https://leetcode-cn.com/problems/count-good-meals) | ★★ | 1 | 1 |
| 2021-07-07 00:00 | [#378 有序矩阵中第 K 小的元素](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix) | ★★ | 4 | 2 |
| 2021-07-06 21:55 | [#1418 点菜展示表](https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant) | ★★ | 1 | 1 |
| 2021-07-05 22:51 | [#1387 将整数按权重排序](https://leetcode-cn.com/problems/sort-integers-by-the-power-value) | ★★ | 7 | 2 |
| 2021-07-05 21:53 | [#23 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists) | ★★★ | 5 | **4** |
| 2021-07-05 21:38 | [#692 前K个高频单词](https://leetcode-cn.com/problems/top-k-frequent-words) | ★★ | 7 | **4** |
| 2021-07-05 21:18 | [#215 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array) | ★★ | 5 | **4** |
| 2021-07-05 20:44 | [#726 原子的数量](https://leetcode-cn.com/problems/number-of-atoms) | ★★★ | 1 | 1 |
| 2021-07-04 20:30 | [#645 错误的集合](https://leetcode-cn.com/problems/set-mismatch) | ★ | 1 | 1 |
| 2021-07-03 12:06 | [#451 根据字符出现频率排序](https://leetcode-cn.com/problems/sort-characters-by-frequency) | ★★ | 1 | 1 |
| 2021-07-02 23:58 | [#198 打家劫舍](https://leetcode-cn.com/problems/house-robber) | ★★ | 13 | **5** |
| 2021-07-02 22:58 | [#70 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | ★ | 8 | **4** |
| 2021-07-02 21:12 | [#1833 雪糕的最大数量](https://leetcode-cn.com/problems/maximum-ice-cream-bars) | ★★ | 1 | 1 |
| 2021-07-01 21:48 | [#LCP 07 传递信息](https://leetcode-cn.com/problems/chuan-di-xin-xi) | ★ | 1 | 1 |
| 2021-06-30 21:25 | [#剑指 Offer 37 序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof) | ★★★ | 1 | 1 |
| 2021-06-29 21:51 | [#303 区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable) | ★ | 4 | **3** |
| 2021-06-29 20:44 | [#168 Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title) | ★ | 2 | 1 |
| 2021-06-28 21:08 | [#815 公交路线](https://leetcode-cn.com/problems/bus-routes) | ★★★ | 1 | 1 |
| 2021-06-27 19:32 | [#909 蛇梯棋](https://leetcode-cn.com/problems/snakes-and-ladders) | ★★ | 1 | 1 |
| 2021-06-27 03:39 | [#139 单词拆分](https://leetcode-cn.com/problems/word-break) | ★★ | 4 | **3** |
| 2021-06-26 16:56 | [#773 滑动谜题](https://leetcode-cn.com/problems/sliding-puzzle) | ★★★ | 1 | 1 |
| 2021-06-25 22:15 | [#752 打开转盘锁](https://leetcode-cn.com/problems/open-the-lock) | ★★ | 1 | 1 |
| 2021-06-24 22:04 | [#149 直线上最多的点数](https://leetcode-cn.com/problems/max-points-on-a-line) | ★★★ | 5 | 1 |
| 2021-06-23 20:58 | [#535 TinyURL 的加密与解密](https://leetcode-cn.com/problems/encode-and-decode-tinyurl) | ★★ | 3 | 1 |
| 2021-06-23 20:29 | [#剑指 Offer 15 二进制中1的个数](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof) | ★ | 1 | 1 |
| 2021-06-22 21:18 | [#剑指 Offer 38 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof) | ★★ | 3 | 1 |
| 2021-06-21 20:41 | [#401 二进制手表](https://leetcode-cn.com/problems/binary-watch) | ★ | 1 | 1 |
| 2021-06-20 21:24 | [#560 和为 K 的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k) | ★★ | 4 | 2 |
| 2021-06-20 01:54 | [#1600 王位继承顺序](https://leetcode-cn.com/problems/throne-inheritance) | ★★ | 1 | 1 |
| 2021-06-19 20:43 | [#1239 串联字符串的最大长度](https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters) | ★★ | 2 | 1 |
| 2021-06-18 21:05 | [#483 最小好进制](https://leetcode-cn.com/problems/smallest-good-base) | ★★★ | 1 | 1 |
| 2021-06-17 20:47 | [#636 函数的独占时间](https://leetcode-cn.com/problems/exclusive-time-of-functions) | ★★ | 4 | 2 |
| 2021-06-17 20:29 | [#394 字符串解码](https://leetcode-cn.com/problems/decode-string) | ★★ | 4 | **3** |
| 2021-06-17 20:06 | [#65 有效数字](https://leetcode-cn.com/problems/valid-number) | ★★★ | 1 | 1 |
| 2021-06-16 20:26 | [#877 石子游戏](https://leetcode-cn.com/problems/stone-game) | ★★ | 1 | 1 |
| 2021-06-15 20:57 | [#852 山脉数组的峰顶索引](https://leetcode-cn.com/problems/peak-index-in-a-mountain-array) | ★ | 1 | 1 |
| 2021-06-14 20:17 | [#374 猜数字大小](https://leetcode-cn.com/problems/guess-number-higher-or-lower) | ★ | 2 | 2 |
| 2021-06-12 20:43 | [#1449 数位成本和为目标值的最大数字](https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target) | ★★★ | 1 | 1 |
| 2021-06-12 16:50 | [#503 下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-ii) | ★★ | 2 | 2 |
| 2021-06-12 15:36 | [#20 有效的括号](https://leetcode-cn.com/problems/valid-parentheses) | ★ | 5 | 2 |
| 2021-06-12 01:28 | [#735 行星碰撞](https://leetcode-cn.com/problems/asteroid-collision) | ★★ | 2 | 1 |
| 2021-06-11 23:12 | [#739 每日温度](https://leetcode-cn.com/problems/daily-temperatures) | ★★ | 3 | **3** |
| 2021-06-11 20:57 | [#279 完全平方数](https://leetcode-cn.com/problems/perfect-squares) | ★★ | 7 | **4** |
| 2021-06-10 23:43 | [#92 反转链表 II](https://leetcode-cn.com/problems/reverse-linked-list-ii) | ★★ | 3 | 2 |
| 2021-06-10 23:00 | [#518 零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2) | ★★ | 12 | **4** |
| 2021-06-09 22:33 | [#141 环形链表](https://leetcode-cn.com/problems/linked-list-cycle) | ★ | 6 | 2 |
| 2021-06-09 21:26 | [#879 盈利计划](https://leetcode-cn.com/problems/profitable-schemes) | ★★★ | 1 | 1 |
| 2021-06-08 23:51 | [#153 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array) | ★★ | 6 | 2 |
| 2021-06-08 23:49 | [#1049 最后一块石头的重量 II](https://leetcode-cn.com/problems/last-stone-weight-ii) | ★★ | 1 | 1 |
| 2021-06-07 23:58 | [#33 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array) | ★★ | 12 | **4** |
| 2021-06-07 22:26 | [#69 x 的平方根 ](https://leetcode-cn.com/problems/sqrtx) | ★ | 1 | 1 |
| 2021-06-07 18:47 | [#494 目标和](https://leetcode-cn.com/problems/target-sum) | ★★ | 5 | **3** |
| 2021-06-06 14:01 | [#474 一和零](https://leetcode-cn.com/problems/ones-and-zeroes) | ★★ | 1 | 1 |
| 2021-06-05 12:08 | [#203 移除链表元素](https://leetcode-cn.com/problems/remove-linked-list-elements) | ★ | 2 | 1 |
| 2021-06-04 21:04 | [#160 相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists) | ★ | 3 | 2 |
| 2021-06-03 21:47 | [#34 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array) | ★★ | 11 | 2 |
| 2021-06-03 08:04 | [#525 连续数组](https://leetcode-cn.com/problems/contiguous-array) | ★★ | 1 | 1 |
| 2021-06-02 21:42 | [#1744 你能在你最喜欢的那天吃到你最喜欢的糖果吗？](https://leetcode-cn.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day) | ★★ | 1 | 1 |
| 2021-06-02 21:41 | [#523 连续的子数组和](https://leetcode-cn.com/problems/continuous-subarray-sum) | ★★ | 1 | 1 |
| 2021-06-01 21:29 | [#80 删除有序数组中的重复项 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii) | ★★ | 4 | 2 |
| 2021-05-31 14:21 | [#342 4的幂](https://leetcode-cn.com/problems/power-of-four) | ★ | 1 | 1 |
| 2021-05-31 11:03 | [#283 移动零](https://leetcode-cn.com/problems/move-zeroes) | ★ | 10 | 2 |
| 2021-05-31 07:30 | [#42 接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | ★★★ | 4 | **3** |
| 2021-05-31 07:06 | [#11 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | ★★ | 2 | 2 |
| 2021-05-31 00:58 | [#26 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | ★ | 3 | 2 |
| 2021-05-31 00:08 | [#344 反转字符串](https://leetcode-cn.com/problems/reverse-string) | ★ | 1 | 1 |
| 2021-05-30 16:30 | [#973 最接近原点的 K 个点](https://leetcode-cn.com/problems/k-closest-points-to-origin) | ★★ | 3 | 1 |
| 2021-05-30 00:42 | [#231 2 的幂](https://leetcode-cn.com/problems/power-of-two) | ★ | 2 | 1 |
| 2021-05-29 00:53 | [#1074 元素和为目标值的子矩阵数量](https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target) | ★★★ | 1 | 1 |
| 2021-05-29 00:52 | [#477 汉明距离总和](https://leetcode-cn.com/problems/total-hamming-distance) | ★★ | 1 | 1 |
| 2021-05-27 00:04 | [#461 汉明距离](https://leetcode-cn.com/problems/hamming-distance) | ★ | 4 | **3** |
| 2021-05-26 21:42 | [#1190 反转每对括号间的子串](https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses) | ★★ | 1 | 1 |
| 2021-05-25 22:33 | [#934 最短的桥](https://leetcode-cn.com/problems/shortest-bridge) | ★★ | 6 | 1 |
| 2021-05-25 07:56 | [#1787 使所有区间的异或结果为零](https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero) | ★★★ | 1 | 1 |
| 2021-05-25 07:54 | [#1162 地图分析](https://leetcode-cn.com/problems/as-far-from-land-as-possible) | ★★ | 8 | **3** |
| 2021-05-24 23:16 | [#664 奇怪的打印机](https://leetcode-cn.com/problems/strange-printer) | ★★★ | 1 | 1 |
| 2021-05-24 22:22 | [#542 01 矩阵](https://leetcode-cn.com/problems/01-matrix) | ★★ | 7 | **3** |
| 2021-05-23 17:26 | [#1707 与数组中元素的最大异或值](https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array) | ★★★ | 1 | 1 |
| 2021-05-23 17:19 | [#127 单词接龙](https://leetcode-cn.com/problems/word-ladder) | ★★★ | 3 | 2 |
| 2021-05-22 16:25 | [#810 黑板异或游戏](https://leetcode-cn.com/problems/chalkboard-xor-game) | ★★★ | 1 | 1 |
| 2021-05-21 21:13 | [#1035 不相交的线](https://leetcode-cn.com/problems/uncrossed-lines) | ★★ | 1 | 1 |
| 2021-05-19 22:33 | [#101 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree) | ★ | 13 | **3** |
| 2021-05-19 21:30 | [#1738 找出第 K 大的异或坐标值](https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value) | ★★ | 1 | 1 |
| 2021-05-19 08:30 | [#515 在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row) | ★★ | 1 | 1 |
| 2021-05-19 08:25 | [#429 N 叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal) | ★★ | 5 | 1 |
| 2021-05-19 07:34 | [#103 二叉树的锯齿形层序遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal) | ★★ | 2 | 1 |
| 2021-05-18 20:56 | [#1442 形成两个异或相等数组的三元组数目](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor) | ★★ | 1 | 1 |
| 2021-05-15 17:21 | [#13 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer) | ★ | 1 | 1 |
| 2021-05-14 22:01 | [#37 解数独](https://leetcode-cn.com/problems/sudoku-solver) | ★★★ | 3 | **3** |
| 2021-05-14 07:09 | [#12 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman) | ★★ | 1 | 1 |
| 2021-05-13 07:58 | [#22 括号生成](https://leetcode-cn.com/problems/generate-parentheses) | ★★ | 12 | **5** |
| 2021-05-13 07:40 | [#1269 停在原地的方案数](https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps) | ★★★ | 1 | 1 |
| 2021-05-13 06:48 | [#996 正方形数组的数目](https://leetcode-cn.com/problems/number-of-squareful-arrays) | ★★★ | 4 | 1 |
| 2021-05-12 21:34 | [#784 字母大小写全排列](https://leetcode-cn.com/problems/letter-case-permutation) | ★★ | 4 | 2 |
| 2021-05-12 07:55 | [#1310 子数组异或查询](https://leetcode-cn.com/problems/xor-queries-of-a-subarray) | ★★ | 1 | 1 |
| 2021-05-11 22:36 | [#47 全排列 II](https://leetcode-cn.com/problems/permutations-ii) | ★★ | 2 | 1 |
| 2021-05-11 21:45 | [#1734 解码异或后的排列](https://leetcode-cn.com/problems/decode-xored-permutation) | ★★ | 2 | 1 |
| 2021-05-10 21:23 | [#216 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii) | ★★ | 1 | 1 |
| 2021-05-10 07:50 | [#90 子集 II](https://leetcode-cn.com/problems/subsets-ii) | ★★ | 4 | 2 |
| 2021-05-10 06:44 | [#872 叶子相似的树](https://leetcode-cn.com/problems/leaf-similar-trees) | ★ | 2 | 1 |
| 2021-05-09 01:08 | [#1482 制作 m 束花所需的最少天数](https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets) | ★★ | 1 | 1 |
| 2021-05-08 19:25 | [#1723 完成所有工作的最短时间](https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs) | ★★★ | 1 | 1 |
| 2021-05-07 23:06 | [#304 二维区域和检索 - 矩阵不可变](https://leetcode-cn.com/problems/range-sum-query-2d-immutable) | ★★ | 2 | 2 |
| 2021-05-07 08:24 | [#1486 数组异或操作](https://leetcode-cn.com/problems/xor-operation-in-an-array) | ★ | 1 | 1 |
| 2021-05-06 23:10 | [#221 最大正方形](https://leetcode-cn.com/problems/maximal-square) | ★★ | 4 | **3** |
| 2021-05-06 22:04 | [#740 删除并获得点数](https://leetcode-cn.com/problems/delete-and-earn) | ★★ | 2 | 1 |
| 2021-05-06 22:01 | [#1720 解码异或后的数组](https://leetcode-cn.com/problems/decode-xored-array) | ★ | 1 | 1 |
| 2021-05-05 01:49 | [#746 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs) | ★ | 2 | 1 |
| 2021-05-04 23:25 | [#337 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii) | ★★ | 9 | **4** |
| 2021-05-04 21:27 | [#72 编辑距离](https://leetcode-cn.com/problems/edit-distance) | ★★★ | 6 | **4** |
| 2021-05-04 15:43 | [#1473 粉刷房子 III](https://leetcode-cn.com/problems/paint-house-iii) | ★★★ | 1 | 1 |
| 2021-05-03 23:25 | [#354 俄罗斯套娃信封问题](https://leetcode-cn.com/problems/russian-doll-envelopes) | ★★★ | 6 | **3** |
| 2021-05-03 21:52 | [#1143 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence) | ★★ | 4 | **3** |
| 2021-05-03 11:42 | [#300 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence) | ★★ | 9 | **4** |
| 2021-05-03 10:53 | [#7 整数反转](https://leetcode-cn.com/problems/reverse-integer) | ★★ | 1 | 1 |
| 2021-05-02 10:44 | [#554 砖墙](https://leetcode-cn.com/problems/brick-wall) | ★★ | 1 | 1 |
| 2021-05-02 03:49 | [#剑指 Offer 63 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof) | ★★ | 4 | 1 |
| 2021-05-01 21:08 | [#690 员工的重要性](https://leetcode-cn.com/problems/employee-importance) | ★★ | 1 | 1 |
| 2021-04-30 20:34 | [#137 只出现一次的数字 II](https://leetcode-cn.com/problems/single-number-ii) | ★★ | 1 | 1 |
| 2021-04-29 22:27 | [#403 青蛙过河](https://leetcode-cn.com/problems/frog-jump) | ★★★ | 1 | 1 |
| 2021-04-29 11:00 | [#322 零钱兑换](https://leetcode-cn.com/problems/coin-change) | ★★ | 8 | **3** |
| 2021-04-28 23:20 | [#416 分割等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum) | ★★ | 11 | **5** |
| 2021-04-28 21:09 | [#633 平方数之和](https://leetcode-cn.com/problems/sum-of-square-numbers) | ★★ | 3 | 1 |
| 2021-04-27 21:16 | [#938 二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst) | ★ | 2 | 1 |
| 2021-04-26 20:22 | [#1011 在 D 天内送达包裹的能力](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days) | ★★ | 1 | 1 |
| 2021-04-25 11:19 | [#897 递增顺序搜索树](https://leetcode-cn.com/problems/increasing-order-search-tree) | ★ | 1 | 1 |
| 2021-04-24 20:47 | [#377 组合总和 Ⅳ](https://leetcode-cn.com/problems/combination-sum-iv) | ★★ | 1 | 1 |
| 2021-04-23 21:27 | [#368 最大整除子集](https://leetcode-cn.com/problems/largest-divisible-subset) | ★★ | 1 | 1 |
| 2021-04-22 21:23 | [#363 矩形区域不超过 K 的最大数值和](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k) | ★★★ | 1 | 1 |
| 2021-04-21 20:51 | [#91 解码方法](https://leetcode-cn.com/problems/decode-ways) | ★★ | 1 | 1 |
| 2021-04-19 21:53 | [#27 移除元素](https://leetcode-cn.com/problems/remove-element) | ★ | 1 | 1 |
| 2021-04-17 21:36 | [#220 存在重复元素 III](https://leetcode-cn.com/problems/contains-duplicate-iii) | ★★ | 1 | 1 |
| 2021-04-16 10:27 | [#87 扰乱字符串](https://leetcode-cn.com/problems/scramble-string) | ★★★ | 1 | 1 |
| 2021-04-15 21:01 | [#213 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii) | ★★ | 3 | 2 |
| 2021-04-14 23:39 | [#206 反转链表](https://leetcode-cn.com/problems/reverse-linked-list) | ★ | 4 | **3** |
| 2021-04-13 22:03 | [#530 二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst) | ★ | 2 | 1 |
| 2021-04-13 21:56 | [#783 二叉搜索树节点最小距离](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes) | ★ | 2 | 1 |
| 2021-04-12 22:52 | [#236 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree) | ★★ | 3 | 2 |
| 2021-04-12 22:15 | [#222 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes) | ★★ | 1 | 1 |
| 2021-04-12 21:41 | [#179 最大数](https://leetcode-cn.com/problems/largest-number) | ★★ | 1 | 1 |
| 2021-04-11 22:39 | [#450 删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst) | ★★ | 1 | 1 |
| 2021-04-11 21:27 | [#98 验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree) | ★★ | 16 | **3** |
| 2021-04-11 21:01 | [#145 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal) | ★ | 1 | 1 |
| 2021-04-11 20:40 | [#460 LFU 缓存](https://leetcode-cn.com/problems/lfu-cache) | ★★★ | 2 | 2 |
| 2021-04-11 17:59 | [#264 丑数 II](https://leetcode-cn.com/problems/ugly-number-ii) | ★★ | 1 | 1 |
| 2021-04-10 18:21 | [#146 LRU 缓存](https://leetcode-cn.com/problems/lru-cache) | ★★ | 7 | **3** |
| 2021-04-10 18:04 | [#263 丑数](https://leetcode-cn.com/problems/ugly-number) | ★ | 1 | 1 |
| 2021-04-09 20:34 | [#154 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii) | ★★★ | 1 | 1 |
| 2021-04-07 21:47 | [#81 搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii) | ★★ | 1 | 1 |
| 2021-04-05 10:30 | [#312 戳气球](https://leetcode-cn.com/problems/burst-balloons) | ★★★ | 6 | 2 |
| 2021-04-04 11:00 | [#10 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching) | ★★★ | 3 | 2 |
| 2021-04-04 09:07 | [#781 森林中的兔子](https://leetcode-cn.com/problems/rabbits-in-forest) | ★★ | 1 | 1 |
| 2021-04-03 23:54 | [#1312 让字符串成为回文串的最少插入次数](https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome) | ★★★ | 1 | 1 |
| 2021-04-02 21:04 | [#面试题 17.21 直方图的水量](https://leetcode-cn.com/problems/volume-of-histogram-lcci) | ★★★ | 1 | 1 |
| 2021-04-01 21:05 | [#1006 笨阶乘](https://leetcode-cn.com/problems/clumsy-factorial) | ★★ | 1 | 1 |
| 2021-03-30 21:11 | [#74 搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix) | ★★ | 1 | 1 |
| 2021-03-29 21:21 | [#173 二叉搜索树迭代器](https://leetcode-cn.com/problems/binary-search-tree-iterator) | ★★ | 1 | 1 |
| 2021-03-29 21:20 | [#190 颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits) | ★ | 1 | 1 |
| 2021-03-27 20:32 | [#61 旋转链表](https://leetcode-cn.com/problems/rotate-list) | ★★ | 1 | 1 |
| 2021-03-26 21:31 | [#83 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list) | ★ | 1 | 1 |
| 2021-03-25 21:49 | [#82 删除排序链表中的重复元素 II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii) | ★★ | 1 | 1 |
| 2021-03-24 21:27 | [#456 132 模式](https://leetcode-cn.com/problems/132-pattern) | ★★ | 1 | 1 |
| 2021-03-22 21:11 | [#191 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits) | ★ | 1 | 1 |
| 2021-03-21 17:56 | [#73 矩阵置零](https://leetcode-cn.com/problems/set-matrix-zeroes) | ★★ | 1 | 1 |
| 2021-03-20 16:49 | [#150 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation) | ★★ | 1 | 1 |
| 2021-03-18 21:06 | [#59 螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii) | ★★ | 2 | 2 |
| 2021-03-17 20:48 | [#115 不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences) | ★★★ | 1 | 1 |
| 2021-03-15 20:37 | [#54 螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix) | ★★ | 1 | 1 |
| 2021-03-12 21:25 | [#331 验证二叉树的前序序列化](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree) | ★★ | 1 | 1 |
| 2021-03-11 22:11 | [#227 基本计算器 II](https://leetcode-cn.com/problems/basic-calculator-ii) | ★★ | 1 | 1 |
| 2021-03-10 21:22 | [#224 基本计算器](https://leetcode-cn.com/problems/basic-calculator) | ★★★ | 1 | 1 |
| 2021-03-09 22:13 | [#1047 删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string) | ★ | 1 | 1 |
| 2021-03-08 21:32 | [#132 分割回文串 II](https://leetcode-cn.com/problems/palindrome-partitioning-ii) | ★★★ | 2 | 1 |
| 2021-03-07 23:02 | [#131 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning) | ★★ | 1 | 1 |
| 2021-03-03 21:25 | [#338 比特位计数](https://leetcode-cn.com/problems/counting-bits) | ★ | 4 | **3** |
| 2021-02-28 19:35 | [#896 单调数列](https://leetcode-cn.com/problems/monotonic-array) | ★ | 2 | 1 |
| 2021-02-27 21:00 | [#395 至少有 K 个重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters) | ★★ | 1 | 1 |
| 2021-02-26 20:31 | [#1178 猜字谜](https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle) | ★★★ | 1 | 1 |
| 2021-02-25 21:22 | [#867 转置矩阵](https://leetcode-cn.com/problems/transpose-matrix) | ★ | 1 | 1 |
| 2021-02-24 21:26 | [#832 翻转图像](https://leetcode-cn.com/problems/flipping-an-image) | ★ | 1 | 1 |
| 2021-02-23 20:27 | [#1052 爱生气的书店老板](https://leetcode-cn.com/problems/grumpy-bookstore-owner) | ★★ | 1 | 1 |
| 2021-02-22 21:03 | [#766 托普利茨矩阵](https://leetcode-cn.com/problems/toeplitz-matrix) | ★ | 1 | 1 |
| 2021-02-21 01:21 | [#1438 绝对差不超过限制的最长连续子数组](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit) | ★★ | 1 | 1 |
| 2021-02-20 02:51 | [#697 数组的度](https://leetcode-cn.com/problems/degree-of-an-array) | ★ | 1 | 1 |
| 2021-02-19 13:01 | [#1004 最大连续1的个数 III](https://leetcode-cn.com/problems/max-consecutive-ones-iii) | ★★ | 1 | 1 |
| 2021-02-18 11:47 | [#995 K 连续位的最小翻转次数](https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips) | ★★★ | 3 | 1 |
| 2021-02-17 13:54 | [#566 重塑矩阵](https://leetcode-cn.com/problems/reshape-the-matrix) | ★ | 1 | 1 |
| 2021-02-16 10:55 | [#561 数组拆分 I](https://leetcode-cn.com/problems/array-partition-i) | ★ | 1 | 1 |
| 2021-02-15 10:40 | [#485 最大连续 1 的个数](https://leetcode-cn.com/problems/max-consecutive-ones) | ★ | 1 | 1 |
| 2021-02-14 15:32 | [#765 情侣牵手](https://leetcode-cn.com/problems/couples-holding-hands) | ★★★ | 1 | 1 |
| 2021-02-13 12:59 | [#119 杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii) | ★ | 1 | 1 |
| 2021-02-13 12:58 | [#448 找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array) | ★ | 3 | 2 |
| 2021-02-10 20:49 | [#567 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string) | ★★ | 1 | 1 |
| 2021-02-09 10:30 | [#992 K 个不同整数的子数组](https://leetcode-cn.com/problems/subarrays-with-k-different-integers) | ★★★ | 1 | 1 |
| 2021-02-08 13:40 | [#978 最长湍流子数组](https://leetcode-cn.com/problems/longest-turbulent-subarray) | ★★ | 2 | 1 |
| 2021-02-07 19:33 | [#665 非递减数列](https://leetcode-cn.com/problems/non-decreasing-array) | ★★ | 1 | 1 |
| 2021-02-06 22:20 | [#1423 可获得的最大点数](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards) | ★★ | 1 | 1 |
| 2021-02-05 21:42 | [#1208 尽可能使字符串相等](https://leetcode-cn.com/problems/get-equal-substrings-within-budget) | ★★ | 3 | 1 |
| 2021-02-04 22:16 | [#643 子数组最大平均数 I](https://leetcode-cn.com/problems/maximum-average-subarray-i) | ★ | 1 | 1 |
| 2021-02-03 21:31 | [#480 滑动窗口中位数](https://leetcode-cn.com/problems/sliding-window-median) | ★★★ | 1 | 1 |
| 2021-02-02 23:08 | [#424 替换后的最长重复字符](https://leetcode-cn.com/problems/longest-repeating-character-replacement) | ★★ | 1 | 1 |
| 2021-02-01 21:47 | [#888 公平的糖果交换](https://leetcode-cn.com/problems/fair-candy-swap) | ★ | 1 | 1 |
| 2021-01-31 00:28 | [#839 相似字符串组](https://leetcode-cn.com/problems/similar-string-groups) | ★★★ | 1 | 1 |
| 2021-01-30 10:39 | [#778 水位上升的泳池中游泳](https://leetcode-cn.com/problems/swim-in-rising-water) | ★★★ | 1 | 1 |
| 2021-01-29 21:51 | [#1631 最小体力消耗路径](https://leetcode-cn.com/problems/path-with-minimum-effort) | ★★ | 1 | 1 |
| 2021-01-28 21:12 | [#724 寻找数组的中心下标](https://leetcode-cn.com/problems/find-pivot-index) | ★ | 2 | 2 |
| 2021-01-27 20:29 | [#1579 保证图可完全遍历](https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable) | ★★★ | 1 | 1 |
| 2021-01-26 21:51 | [#1128 等价多米诺骨牌对的数量](https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs) | ★ | 1 | 1 |
| 2021-01-25 20:36 | [#959 由斜杠划分区域](https://leetcode-cn.com/problems/regions-cut-by-slashes) | ★★ | 1 | 1 |
| 2021-01-24 20:09 | [#674 最长连续递增序列](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence) | ★ | 1 | 1 |
| 2021-01-23 20:27 | [#1319 连通网络的操作次数](https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected) | ★★ | 1 | 1 |
| 2021-01-22 20:27 | [#989 数组形式的整数加法](https://leetcode-cn.com/problems/add-to-array-form-of-integer) | ★ | 1 | 1 |
| 2021-01-21 22:05 | [#1489 找到最小生成树里的关键边和伪关键边](https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree) | ★★★ | 1 | 1 |
| 2021-01-20 21:46 | [#628 三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers) | ★ | 2 | 1 |
| 2021-01-19 22:42 | [#1584 连接所有点的最小费用](https://leetcode-cn.com/problems/min-cost-to-connect-all-points) | ★★ | 1 | 1 |
| 2021-01-18 20:59 | [#721 账户合并](https://leetcode-cn.com/problems/accounts-merge) | ★★ | 1 | 1 |
| 2021-01-17 16:50 | [#1232 缀点成线](https://leetcode-cn.com/problems/check-if-it-is-a-straight-line) | ★ | 1 | 1 |
| 2021-01-16 21:59 | [#803 打砖块](https://leetcode-cn.com/problems/bricks-falling-when-hit) | ★★★ | 1 | 1 |
| 2021-01-15 20:54 | [#947 移除最多的同行或同列石头](https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column) | ★★ | 1 | 1 |
| 2021-01-14 21:10 | [#1018 可被 5 整除的二进制前缀](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5) | ★ | 1 | 1 |
| 2021-01-13 21:53 | [#684 冗余连接](https://leetcode-cn.com/problems/redundant-connection) | ★★ | 1 | 1 |
| 2021-01-12 20:52 | [#1203 项目管理](https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies) | ★★★ | 1 | 1 |
| 2021-01-11 21:53 | [#1202 交换字符串中的元素](https://leetcode-cn.com/problems/smallest-string-with-swaps) | ★★ | 1 | 1 |
| 2021-01-10 14:32 | [#228 汇总区间](https://leetcode-cn.com/problems/summary-ranges) | ★ | 2 | 1 |
| 2021-01-09 20:55 | [#123 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii) | ★★★ | 1 | 1 |
| 2021-01-07 21:47 | [#547 省份数量](https://leetcode-cn.com/problems/number-of-provinces) | ★★ | 1 | 1 |
| 2021-01-06 21:20 | [#399 除法求值](https://leetcode-cn.com/problems/evaluate-division) | ★★ | 3 | 2 |
| 2021-01-05 21:29 | [#830 较大分组的位置](https://leetcode-cn.com/problems/positions-of-large-groups) | ★ | 3 | 1 |
| 2021-01-04 13:35 | [#509 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number) | ★ | 1 | 1 |
| 2021-01-03 16:11 | [#86 分隔链表](https://leetcode-cn.com/problems/partition-list) | ★★ | 1 | 1 |
| 2021-01-02 12:59 | [#94 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) | ★ | 5 | **3** |
| 2021-01-02 12:13 | [#144 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal) | ★ | 1 | 1 |
| 2021-01-02 11:39 | [#239 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum) | ★★★ | 3 | 2 |
| 2021-01-01 02:01 | [#605 种花问题](https://leetcode-cn.com/problems/can-place-flowers) | ★ | 1 | 1 |
| 2020-12-10 22:20 | [#860 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change) | ★ | 1 | 1 |
| 2020-04-14 21:53 | [#445 两数相加 II](https://leetcode-cn.com/problems/add-two-numbers-ii) | ★★ | 1 | 1 |
| 2020-04-13 21:33 | [#355 设计推特](https://leetcode-cn.com/problems/design-twitter) | ★★ | 1 | 1 |
| 2020-04-10 21:42 | [#151 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string) | ★★ | 1 | 1 |
| 2020-04-08 21:52 | [#剑指 Offer 13 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof) | ★★ | 1 | 1 |
| 2020-04-07 17:19 | [#面试题 01.07 旋转矩阵](https://leetcode-cn.com/problems/rotate-matrix-lcci) | ★★ | 1 | 1 |
| 2020-04-03 22:58 | [#8 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi) | ★★ | 1 | 1 |
| 2020-04-02 19:58 | [#289 生命游戏](https://leetcode-cn.com/problems/game-of-life) | ★★ | 1 | 1 |
| 2020-04-01 22:16 | [#1111 有效括号的嵌套深度](https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings) | ★★ | 1 | 1 |
| 2020-03-30 10:10 | [#剑指 Offer 62 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof) | ★ | 1 | 1 |
| 2020-03-26 21:07 | [#999 可以被一步捕获的棋子数](https://leetcode-cn.com/problems/available-captures-for-rook) | ★ | 1 | 1 |
| 2020-03-24 17:49 | [#面试题 17.16 按摩师](https://leetcode-cn.com/problems/the-masseuse-lcci) | ★ | 1 | 1 |
| 2020-03-22 20:09 | [#945 使数组唯一的最小增量](https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique) | ★★ | 1 | 1 |
| 2020-03-21 17:40 | [#365 水壶问题](https://leetcode-cn.com/problems/water-and-jug-problem) | ★★ | 1 | 1 |
| 2020-03-20 20:55 | [#剑指 Offer 40 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof) | ★ | 3 | 1 |
| 2020-03-19 20:51 | [#409 最长回文串](https://leetcode-cn.com/problems/longest-palindrome) | ★ | 1 | 1 |
| 2020-03-18 22:01 | [#836 矩形重叠](https://leetcode-cn.com/problems/rectangle-overlap) | ★ | 5 | 1 |
| 2020-03-17 21:36 | [#1160 拼写单词](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters) | ★ | 2 | 1 |
| 2020-03-16 15:28 | [#面试题 01.06 字符串压缩](https://leetcode-cn.com/problems/compress-string-lcci) | ★ | 1 | 1 |
| 2020-03-15 14:45 | [#695 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island) | ★★ | 1 | 1 |
| 2020-03-13 23:46 | [#169 多数元素](https://leetcode-cn.com/problems/majority-element) | ★ | 3 | 2 |
| 2020-02-26 15:07 | [#剑指 Offer 09 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof) | ★ | 2 | 1 |
| 2020-02-26 15:01 | [#剑指 Offer 07 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof) | ★★ | 1 | 1 |
| 2020-02-26 14:57 | [#剑指 Offer 06 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof) | ★ | 1 | 1 |
| 2020-02-26 14:51 | [#剑指 Offer 05 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof) | ★ | 1 | 1 |
| 2020-02-12 18:04 | [#剑指 Offer 04 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof) | ★★ | 1 | 1 |
| 2020-02-12 18:02 | [#剑指 Offer 03 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof) | ★ | 1 | 1 |
| 2020-02-11 23:09 | [#96 不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees) | ★★ | 2 | 2 |
| 2020-02-11 16:04 | [#136 只出现一次的数字](https://leetcode-cn.com/problems/single-number) | ★ | 2 | 2 |
| 2020-02-11 15:15 | [#3 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters) | ★★ | 6 | 2 |
| 2020-02-11 14:54 | [#79 单词搜索](https://leetcode-cn.com/problems/word-search) | ★★ | 2 | 2 |
| 2020-02-11 13:13 | [#617 合并二叉树](https://leetcode-cn.com/problems/merge-two-binary-trees) | ★ | 3 | **3** |
| 2020-02-11 00:50 | [#538 把二叉搜索树转换为累加树](https://leetcode-cn.com/problems/convert-bst-to-greater-tree) | ★★ | 5 | **3** |
| 2020-01-20 16:38 | [#148 排序链表](https://leetcode-cn.com/problems/sort-list) | ★★ | 3 | 2 |
| 2020-01-20 15:44 | [#56 合并区间](https://leetcode-cn.com/problems/merge-intervals) | ★★ | 4 | 2 |
| 2020-01-20 15:04 | [#406 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height) | ★★ | 1 | 1 |
| 2020-01-17 14:45 | [#114 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list) | ★★ | 5 | 2 |
| 2020-01-16 18:38 | [#226 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree) | ★ | 2 | 2 |
| 2020-01-16 16:44 | [#297 二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree) | ★★★ | 4 | **3** |
| 2020-01-14 15:14 | [#543 二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree) | ★ | 10 | 2 |
| 2020-01-03 23:07 | [#647 回文子串](https://leetcode-cn.com/problems/palindromic-substrings) | ★★ | 3 | 1 |
| 2020-01-03 14:15 | [#621 任务调度器](https://leetcode-cn.com/problems/task-scheduler) | ★★ | 1 | 1 |
| 2019-12-24 15:29 | [#347 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements) | ★★ | 2 | 1 |
| 2019-12-19 23:51 | [#309 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) | ★★ | 1 | 1 |
| 2019-12-16 17:58 | [#287 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number) | ★★ | 1 | 1 |
| 2019-12-15 18:09 | [#5 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring) | ★★ | 8 | 2 |
| 2019-12-13 15:50 | [#238 除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self) | ★★ | 1 | 1 |
| 2019-12-12 23:46 | [#234 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list) | ★ | 1 | 1 |
| 2019-12-09 18:18 | [#152 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray) | ★★ | 2 | 1 |
| 2019-12-06 17:45 | [#142 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii) | ★★ | 1 | 1 |
| 2019-12-05 22:40 | [#128 最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence) | ★★ | 1 | 1 |
| 2019-12-01 14:09 | [#105 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) | ★★ | 1 | 1 |
| 2019-11-27 17:56 | [#84 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram) | ★★★ | 1 | 1 |
| 2019-11-26 22:20 | [#43 字符串相乘](https://leetcode-cn.com/problems/multiply-strings) | ★★ | 1 | 1 |
| 2019-11-25 14:48 | [#76 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring) | ★★★ | 1 | 1 |
| 2019-11-24 12:27 | [#75 颜色分类](https://leetcode-cn.com/problems/sort-colors) | ★★ | 2 | 1 |
| 2019-11-20 21:30 | [#55 跳跃游戏](https://leetcode-cn.com/problems/jump-game) | ★★ | 1 | 1 |
| 2019-11-20 16:18 | [#49 字母异位词分组](https://leetcode-cn.com/problems/group-anagrams) | ★★ | 9 | 1 |
| 2019-11-19 21:45 | [#48 旋转图像](https://leetcode-cn.com/problems/rotate-image) | ★★ | 2 | 1 |
| 2019-11-12 14:46 | [#32 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses) | ★★★ | 4 | 1 |
| 2019-11-12 13:46 | [#31 下一个排列](https://leetcode-cn.com/problems/next-permutation) | ★★ | 1 | 1 |
| 2019-11-08 17:25 | [#21 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | ★ | 2 | 1 |
| 2019-11-08 15:08 | [#19 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list) | ★★ | 4 | 1 |
| 2019-11-06 16:14 | [#15 三数之和](https://leetcode-cn.com/problems/3sum) | ★★ | 4 | 1 |
| 2019-11-05 15:02 | [#4 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays) | ★★★ | 3 | 1 |
| 2019-11-04 18:16 | [#2 两数相加](https://leetcode-cn.com/problems/add-two-numbers) | ★★ | 3 | 1 |
