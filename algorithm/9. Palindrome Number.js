/*
Determine whether an integer is a palindrome. 
Do this without extra space.

 

Notes: Easy
观察：  输入已经明确是 Int 型，要求不使用额外空间，O(n/2)
边界值： 负数是否全部为 false，只有正整数才开始判断？  
思路：   1先判断是否是 Int 型
        2再判断正负，负数返回 false，0 返回 true， 正数转为字符串
        3判断字符串长度？ 从index=0开始遍历直到中间位置


*/

var isPalindrome = function(x) {
    // if(!Number.isInteger(x)) { return false; }  // (Math.floor(x) === x)
    // if ( x < 0 ) { return false; }
    // var s = x + ''; //extra space!
    // var sl = s.length;
    // var mid = Math.floor(sl / 2); 
    // for (var i = 0; i < mid; i++) {
    //     if (s[i] !== s[sl - 1 - i]) { 
    //         return false;
    //     }
    // }
    // return true;

    if(! Number.isInteger(x)) { return false; }
    if ( x<0 || (x % 10===0 && x !== 0) ) { return false; }
    var revertedNumber = 0;
    while (x > revertedNumber) {
        revertedNumber = revertedNumber * 10 + x % 10;
        x = Math.floor( x / 10 );
        //console.log("... " + revertedNumber + ", " + x);
    }

    return x === revertedNumber || x === Math.floor( revertedNumber / 10 );
};

 


// Tests
console.log( isPalindrome("121") );
console.log( isPalindrome({}) );
console.log( isPalindrome(-1) );
console.log( isPalindrome(122) );
console.log( isPalindrome(121) );
console.log( isPalindrome(1221) );
console.log( isPalindrome(123454321) );




