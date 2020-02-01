/* Store a hash map of letter frequencies
loop through string to return first string with frequency 1 or less than 2
O(n) time, O(n) space since there is only 26 lower-case character to store in map
*/

char firstNotRepeatingCharacter(std::string s) {
    unordered_map<char, int> r;
    for (char c : s)
    {
        r[c] ++;
    }
    
    for (char c: s)
    {
        if (r[c] < 2)
        {
            return c;
        }
    }
    return '_';
}
