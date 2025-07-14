#Solución Kenny Jesús Flores Huamán

class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT_32 = -2 ** 31        # -2147483648
        MAX_INT_32 = 2 ** 31 - 1     # 2147483647
        is_negative = -1 if x < 0 else 1
        num = abs(x)
        reverse=0
        while num > 0:
            reminded = num % 10
            reverse = (reverse*10) + reminded
            num //= 10

        reverse = reverse*is_negative

        if not (MIN_INT_32 <= reverse <= MAX_INT_32):
            return 0
        return reverse

