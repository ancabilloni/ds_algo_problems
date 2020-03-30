// https://app.codesignal.com/interview-practice/task/sjRBSjPSPDAJgFX64

int insertBits(int n, int a, int b, int k) {
    // Create a->b mask with a left shifts
    int t = ((( 1 << (b-a)) ^ ( (1 << (b-a)) - 1)) << a);

    // Turn off all bits from a to b in n
    n = n & ~t;

    // left shift k to a
    n = n | (k << a);
    return n;
}
