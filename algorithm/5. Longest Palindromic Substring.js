 
/* Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
// Example:
// Input: "babad"
// Output: "bab"

// Note: "aba" is also a valid answer.
// Example:
// Input: "cbbd"
// Output: "bb"  
*/  



// var isPalindrome = function(s) {
//     const strlen = s.length;
//     for (var i = 0; i < parseInt(strlen / 2); i++) {
//         if (s[i] !== s[strlen - 1 - i]) {
//             return false;
//         }
//     }
//     return true;
// };

// Plan A
// var longestPalindrome = function(s) {

//     const slen = s.length;

//     let smap = {};
//     let sdis = {};

//     let result;
//     let resultLen = 0;
    

//     for (let i = 0; i < slen ; i++) {
//         if (! smap[ s[i] ]) {
//             smap[ s[i] ] = [];
//         }
//         smap[ s[i] ].push(i);
//         if (smap[ s[i] ].length > 1) {
//             sdis[ s[i] ] = smap[ s[i] ][smap[ s[i] ].length - 1] - smap[ s[i] ][0];
//         }
//     }

//     for (let key in sdis) {
//         if (resultLen < sdis[key]) {
//             let head = smap[key][0];
//             let substring = s.slice(head, head + 1 + sdis[key])

//             if (isPalindrome(substring)) {
//                 resultLen = substring.length;
//                 result = substring;
//             }
//         }
//     }

//     return result;
// };


// Plan B
// var longestPalindrome = function(s) {
//   if (s.length <= 1) { return s; }
//   if (s.length > 1000) { throw "without range"; }
  
//   var isPalindrome = function(s) {
//     const strlen = s.length;
//     for (var i = 0; i < parseInt(strlen / 2); i++) {
//       if (s[i] !== s[strlen - 1 - i]) {
//         return false;
//       }
//     }
//     return true;
// };

//     var result = s[0];
//     var resultLength = 1;

//     for (var tail = s.length - 1; tail >= 0; tail--) {
//         for(var head = 0; head <= tail; head++) {

//             if (s[head] === s[tail]) {
//                 if ( resultLength <= (tail - head + 1)) {
//                     var subString = s.slice(head, tail + 1);
//                     if (isPalindrome(subString)) {
//                         result = subString;
//                         resultLength = subString.length;
//                     }
//                 }
//             }
//         }
//     }
//     return result;
// };




var longestPalindrome = function(s) {
    if (s.length <= 1) { return s; }
    if (s.length > 1000) { throw "without range"; }

    var longest = s[0];
    var stringExpand = function(str, start, end) {
        while (start >= 0 && end < s.length && s[start] === s[end]) {
            start--;
            end++;
        }
        return s.slice(start+1, end);
    };

    const slen = s.length;
    for (var i = 0; i < slen; i++) {
        tempStr = stringExpand(s, i, i);
        if (tempStr.length > longest.length) {
            longest = tempStr;
        }
        tempStr = stringExpand(s, i, i + 1);
        if (tempStr.length > longest.length) {
            longest = tempStr;
        }
    }
    return longest;
};

console.log(longestPalindrome(""));
console.log(longestPalindrome("a"));
console.log(longestPalindrome("aa"));
console.log(longestPalindrome("aaa"));

console.log(longestPalindrome("abcdea"));
console.log(longestPalindrome("babad"));
console.log(longestPalindrome("cbbd"));
console.log(longestPalindrome("cbbdfkeiznjfgusajasssjkfjfjdabcdefedcbajskfkriqwawpeoqiretirwuerkfjgksjfhgsjgyrd"));

console.log(longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"));
