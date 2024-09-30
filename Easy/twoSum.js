//two sum
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const number_map = new Map();
    for(let i = 0; i < nums.length; i++){
        diff = target - nums[i];
        if(number_map.has(diff)){
            return [i,number_map.get(diff)];
        }
    
        number_map.set(nums[i],i);
    }
};