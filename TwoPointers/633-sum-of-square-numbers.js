/**
 * @param {number} c
 * @return {boolean}
 */
 var judgeSquareSum = function(c) {

    const nums = [];
    for (let i = 0; i * i <= c; i++) {
        nums.push(i * i);
    }
    if (nums.length === 0) { return false; }
    let L = 0;
    let R = nums.length - 1;

    while(L <= R) {
        const n = nums[L] + nums[R];
        if (n === c) { return true; }
        else if (n < c) { L++; }
        else if (n > c) { R--; }
    }

    return false;
};

console.log(judgeSquareSum(2));