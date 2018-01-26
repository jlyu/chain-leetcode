/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321


Example 2:

Input: -123
Output: -321


Example 3:

Input: 120
Output: 21


Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. 
*/

var reverse = function(x) {
    var s = x + '';
    if (s.length < 1) { return 0; }

    var slen = s.length;
    var result = '';
    for (var i = slen - 1; i > 0; i--) {
        result += s[i];
    }
    if (s[0] === '-') {
        result = s[0] + result;
    } else {
        result += s[0]
    }

    if ( parseInt(result) > 2**31 ) { return 0; }
    if ( parseInt(result) < -(2**31) ) { return 0; }
    
    return parseInt(result);

}; 

// Tests
console.log( reverse(123) === 321 );
console.log( reverse(-123) === -321 );
console.log( reverse(120) === 21 );

 

// Notes: 一遍过
// 观察： 比较简单的数字纯逆序
// 边界值：[-2^31, 2^31]   
// 思路： 倒序遍历数字字符串，O(n) 在0位的地方再判断一下是否带符号


