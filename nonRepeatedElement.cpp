// Exclusive OR (XOR) all elements. Repeated elements will cancel each other out. Only the non repeated element is left.
// Complexity O(n), space O(1)

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = nums[0];
        for(int i=1; i < nums.size(); i++)
        {
            result ^= nums[i];
        }
        return result;
    }
};

// Other solution is to use hash table.
// Complexity O(n), space O(n)
