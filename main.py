def to_binary(n: int) -> int:
    """
    Convert a non-negative integer n into binary format.
    :param n:
    :return:
    """
    val = []
    while n >= 1:
        half = n / 2
        mod = n % 2
        val.append(mod)
        n = half

    val = int(''.join([str(int(i)) for i in val][::-1]))
    return val
