/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumXOR = function(nums) {
    let mask = 0, res = 0
    for(let i=31; i>=0; i--) {
        mask = mask | (1 << i)
        let m = {}
        for(let n of nums) {
            m[n&mask] = 1
        }
        let tmp = res | (1 << i)
        for(let k in m) {
            if(m[tmp^k] != undefined) {
               res = tmp 
               break
            }
        }
    }
    return res
};