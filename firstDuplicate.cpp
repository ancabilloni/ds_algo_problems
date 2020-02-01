int firstDuplicate(std::vector<int> a) {
    for (auto x: a)
    {
        a[abs(x) - 1] *= -1;
        if (a[abs(x) - 1] > 0)
        {
            return abs(x);
        }
    }
    return -1;
}
