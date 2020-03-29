// Helper algo: https://www.youtube.com/watch?v=vB-81TB6GUc
// Time O(n). Space O(n)
int productExceptSelf(std::vector<int> nums, int m) {
    unsigned int ans = 0;
    // std::vector<int> mul(nums.size(), 1);
    int mul[nums.size()] = {1};

    int temp = 1;
    // Left transverse
    for (int i = 1; i < nums.size(); i++)
    {
        temp = (temp * nums[i-1]%m) % m;
        mul[i] = temp;
    }

    // Right transverse
    temp = 1;
    ans = mul[nums.size() - 1] % m;

    for (int i=nums.size() - 2; i >= 0; i--)
    {
        temp = (temp * nums[i+1]%m) % m;
        mul[i] = (temp*mul[i]) % m;
        ans = (ans + mul[i]) % m;
    }

    return ans;

}
