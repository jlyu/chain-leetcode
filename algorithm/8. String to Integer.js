/*
Implement atoi to convert a string to an integer.

Hint: 
Carefully consider all possible input cases. 
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes:  
It is intended for this problem to be specified vaguely (ie, no given input specs). 
You are responsible to gather all the input requirements up front.

Notes: 
观察：  
边界值：数字类型的数值上下限  
思路：  input 必须严格 string 型， 理论上可以通过正则匹配来实现
       str第0位可能出现"-"符号
       碰到比如货币型数字呢： 123,456.78  123.789.000,99 都是可能的


*/



var myAtoi = function(str) {
    if (Object.prototype.toString.call(str) !== "[object String]" ) { throw "input must be string type."; }
    
    str = str.replace(/(^\s*)|(\s*$)/g, "");
    if (str.length === 0) { return 0; }
    var iStr = parseInt(str);
    if ( isNaN(iStr) ) { return 0; }
    if (iStr >= Math.pow(2, 31)) { return Math.pow(2, 31) - 1; }
    if (iStr <= Math.pow(-2, 31)) { return Math.pow(-2, 31); }

    return iStr;

};


// Tests
console.log( myAtoi("    +012a44.88f"));
console.log( myAtoi("    010"));
console.log( myAtoi(""));
console.log( myAtoi("123"));
console.log( myAtoi("-123") === -123 );
console.log( myAtoi("+111"));
console.log( myAtoi("-"));
console.log( myAtoi("???"));
console.log( myAtoi("+-1"));
console.log( myAtoi("12.34"));
console.log( myAtoi("2147483648") === 2147483647 );

 




