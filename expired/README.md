# chain-leetcode
:beginner:  楽しくグアルゴリズムを攻略しよう～ Submission Result: Accepted update: 2017-3-17

【贪婪】【分治】【动态】  

####链表(3)  
两链表相加：不要求位数对齐，但需要考虑进位。 https://leetcode.com/problems/add-two-numbers  
从链尾删除第N个结点： https://leetcode.com/problems/remove-nth-node-from-end-of-list  
合并2个已排序链表 O(m-n) https://leetcode.com/problems/merge-two-sorted-lists  

####栈(9)  
检测括号匹配 注意if stack == [] or stack.pop() != brackets[char] https://leetcode.com/problems/valid-parentheses  
最简路径 注意 /...hidden 的含义 https://leetcode.com/problems/simplify-path  
评估RPN 注意除法 int(float(lhs)/rhs) https://leetcode.com/problems/evaluate-reverse-polish-notation  
O(1)栈内最小值 push时把当前min记录下来 https://leetcode.com/problems/min-stack  
删除重复字母 需要按lexicographically顺序 【贪婪】https://leetcode.com/problems/remove-duplicate-letters  
压平嵌套列表 考察generator和yield用法 https://leetcode.com/problems/flatten-nested-list-iterator  
解密字符串 纯stack应用 https://leetcode.com/problems/decode-string  
删除k位字符串 【贪婪】 https://leetcode.com/problems/remove-k-digits  
加减法计算 需要注意负号的计算 https://leetcode.com/problems/basic-calculator  

####数组  
二数和 数组遍历/二分查找/哈希表 https://leetcode.com/problems/two-sum  
二数和-排序数组 https://leetcode.com/problems/two-sum-ii-input-array-is-sorted  
三数和 排序/存在重复元素/二数和升级 https://leetcode.com/problems/3sum  
两排序数组中值 【分治】  
数组包含重复值 set https://leetcode.com/problems/contains-duplicate  
数组包含重复值II Hash https://leetcode.com/problems/contains-duplicate-ii  
删除数组指定值 https://leetcode.com/problems/remove-element  
删除数组重复值 https://leetcode.com/problems/remove-duplicates-from-sorted-array  
数组数字+1 递归 https://leetcode.com/problems/plus-one  
合并2个排序数组 https://leetcode.com/problems/merge-sorted-array  
股票交易最大利润 【动态】https://leetcode.com/problems/best-time-to-buy-and-sell-stock  
股票交易最大利润II 只要盈利就交易，区间内找最小找最大【贪婪】 https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii  
股票交易最大利润III 限制交易2笔【动态】https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii  
寻找峰值 利用dict.keys https://leetcode.com/problems/find-peak-element  
寻找数组内不存在的值们 无序 要求O(n)  https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array  
寻找数组内不存在的值   有序 要求O(n)+S(n) 等差数列-和  https://leetcode.com/problems/missing-number  
寻找数组内唯一重复值 要求O(n^2),O(1) Floyd's cycle-finding algorithm https://leetcode.com/problems/find-the-duplicate-number   
主要元素 HashTable/【分治】 https://leetcode.com/problems/majority-element  
主要元素II Boyer-Moore Majority Vote Algorithm https://leetcode.com/problems/majority-element-ii  
数组元素乘积除本身 https://leetcode.com/problems/product-of-array-except-self  
移零到数组最后 双指针 https://leetcode.com/problems/move-zeroes  
数组内第3大元素 O(n) https://leetcode.com/problems/third-maximum-number/  


####自定义数据结构  
插入删除随机都O(1) https://leetcode.com/problems/insert-delete-getrandom-o1  
插入删除随机都O(1)可重复 collections.defaultdict(set) https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed  
