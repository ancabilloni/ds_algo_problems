//https://app.codesignal.com/interview-practice/task/izLStwkDr5sMS9CEm/description
// Time O(n). Space O(n)

std::vector<int> findLongestSubarrayBySum(int s, std::vector<int> arr) {
    unsigned int sum = 0;
    unordered_map<int, int> sum_map;
    std::vector<int> ans(2,0);

    int max_sum_size = -1;

    for (int j=0; j < arr.size(); j++)
    {
        sum += arr[j];

        if (sum_map.find(sum) == sum_map.end()) // sum not found, put left most index of respective sum to map
        {
            sum_map[sum] = j;
        }

        if (sum == s) // guarantee max size up to this loop
        {
            ans = {0, j};
            max_sum_size = j;
        }
        else if (sum_map.find(sum - s) != sum_map.end()) // found (sum - s) in map
        {
            if (j - sum_map[sum - s] - 1 > max_sum_size) // check for bigger max size
            {
                max_sum_size = j - sum_map[sum - s] - 1;
                ans = {sum_map[sum - s] + 1, j};
            }
        }
    }

    if (max_sum_size < 0) // not finding any subarray
    {
        return {-1};
    }

    return {ans[0]+1, ans[1]+1};
}
