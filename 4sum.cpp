/* https://leetcode.com/problems/4sum-ii/ 
O(n) solution
a + b + c + d = 0 <=> a + b = -(c+d)
Store frequencies of sum of a+b and c+d in 2 dictionaries
*/

class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        int N = A.size();
        unordered_map<int, int> SumAB, SumCD;
        
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                SumAB[A[i] + B[j]] ++;
                SumCD[C[i] + D[j]] ++;
            }
        }
        
        int count = 0;
        for (auto x : SumAB)
        {
            auto it = SumCD.find(x.first*-1);
            if (it != SumCD.end())
            {
                count += x.second * it->second;
            }
        }
        
        return count;
    }
};
