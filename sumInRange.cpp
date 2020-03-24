// CodeSignal problem: https://app.codesignal.com/interview-practice/task/4MoqQLaw22nrzXbgs
// Time O(n+m)
// Space O(n) to store pre_sum

int sumInRange(std::vector<int> nums, std::vector<std::vector<int>> queries) {
    int s = 0;
    const int m = pow(10,9) + 7;
    std::vector<int> pre_sum;
    pre_sum.push_back(nums[0]);

    // Helper algorithm: https://www.geeksforgeeks.org/range-sum-queries-without-updates/
    // Calculate a pre-sum vector O(n) with n = nums.size()
    for (int j=1; j < nums.size(); j++)
    {
        pre_sum.push_back(nums[j] + pre_sum[j-1]);
    }

    // Find sum of queries and modulo of sum O(m) with m = queries.size()
    for (int i = 0; i < queries.size(); i++)
    {
        s += pre_sum[queries[i][1]];
        if(queries[i][0] != 0)
        {
            s -= pre_sum[queries[i][0] -1];
        }
        s %= m; // if not doing this, the final output of very large sum is incorrect (maybe overflow/underflow?)
    }
    return (s + m) % m; // because the output wants positive modulo
}
