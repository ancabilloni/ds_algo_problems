// Using set to check if the sum square repeats. Return False.
// Return True if arrive at value 1 (happy)

class Solution {
public:
    int squareSum(int n)
    {
        int result = 0;
        while (n > 0)
        {
            int m = n % 10;
            result += (n%10)*(n%10);
            n /= 10;
        }
        return result;
    }
    
    bool isHappy(int n) {
        set<int> st;
        while (true)
        {
            n = squareSum(n);
            if (n == 1)
            {
                return true;
            } else if (st.find(n) != st.end())
            {
                return false;
            }
            st.insert(n);
        }
    }
};
