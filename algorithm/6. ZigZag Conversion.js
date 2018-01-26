/*
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
*/

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {

    if (Math.min(numRows, s.length) <= 1) { return s; }
 
    var lines = {};
    var bSeq = true;
    var counter = 0;
    var zigzag = "";

    s.split('').map(function(v, i) {
      
        if (! lines[counter]) { lines[counter] = ""; }
        lines[counter] += v;

        if (bSeq) {
            
            if (counter === numRows - 1) { bSeq = false; counter--; if(counter === 0) {bSeq=true;}  }
            else { counter++; }
        } else {
             
            if (counter === 1) { bSeq = true; counter--; }
            else { counter--; }
        }
    });

    for (var i = 0; i < Math.min(numRows, s.length); i++) {
      zigzag += lines[i];
    }
    return zigzag;
};

// Tests
console.log( convert("123456", 2) );
console.log( convert("ABC", 4) );
console.log( convert("", 1) );
console.log( convert("A", 3) );

var testStr = "PAYPALISHIRING";
for (var i = 0; i <= testStr.length; i++) {
    console.log( convert(testStr, i) );
}


// Notes:
// 观察：什么叫 ZigZag Pattern？  类似 ↓↗↓↗...↗↓ 规则
// 边界值： numRows = 1 or 2 的情况， 以及 s 长度比 numRows 更短的情况
// 思路：遍历一遍字符串O(1), 顺序就是 [0, numRows-1] 形成垂直的线，然后逆序从[numRows-1, 1]形成斜上的线。 声明一个对象存放以行号为map的字符串，最后结果就是把各行子字符串相加得到


