var lengthOfLongestSubstring = function(s) {
    var container = [];
    var substr = "";
    var counter = 0;
    var result = "";
    s.split("").map(function(v){
        if ( substr.includes(v) ) {
            if (counter > result.length) {
                result = substr;
            }
            counter = 1;
            substr = v;
        } else {
            counter++;
            substr += v;
        }
    });
    return result;
};

alert(lengthOfLongestSubstring("abcabcbb"));

// var tests = [
//     // {in:"abcabcbb", out:"abc"},
//     // {in:"bbbbb", out:"b"},   
//     // {in:"pwwkew", out:"wke"},
//     // {in:"", out:""},
//     // {in:"aabbccddeeffabcdeff", out:"fabcde"},
//     {in:"abcabcbb", out:"abc"}
// ]

// tests.map( function(obj){
//     console.log(lengthOfLongestSubstring(obj.in) === obj.out);
// });
    


