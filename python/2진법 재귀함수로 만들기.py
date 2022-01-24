def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if n >= 2 :
        a = n%2
        b = n//2
        return dec_to_bin(b) + str(a)
    else :
        return str(n)

print(dec_to_bin(10))
# 1010
print(dec_to_bin(5))
# 101
print(dec_to_bin(50))
# 110010