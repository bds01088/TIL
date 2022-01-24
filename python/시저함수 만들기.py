def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 'i' == 105
    # 'y' == 121
    # 'a' == 97
    # y -> i까지 122 97 98 99 100 101 102 103 104 105
    #            122 123 124 125 126 127 128 129 130 131
    #122까지니까
    #131-122 = 9
    #97+9 = 106이니까 -1해주면 됌
    #A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z
    # for i in range(65,123) :
    #     print(chr(i), end = ' ')
    #소문자는 97부터 122까지 대문자는 65부터 90까지

    # asc = ''
    # for w in word :
    #     a = ord(w)
    #     #소문자일때
    #     if 97 <= a <= 122 :
    #         if a+n > 122 :
    #             b = a+n-122
    #             c = 97+b-1
    #         else :
    #             c = a+n
    #         asc += chr(c)
    #     #대문자일때
    #     elif 65 <= a <= 90 :
    #         if a+n > 90 :
    #             b = a+n-90
    #             c = 97+b-1
    #         else :
    #             c = a+n
    #         asc += chr(c)
    # return asc

    asc = ''
    for w in word :
        a = ord(w)
        #소문자일때
        if 97 <= a <= 122 :
            c = a+n%26
            if c > 122 :
                b = c-26
                c = b
            asc += chr(c)
        #대문자일때
        elif 65 <= a <= 90 :
            c = a+n%26
            if c > 90 :
                b = c-26
                c = b
            asc += chr(c)
    return asc

print(caesar('apple', 5))
# fuuqj
print(caesar('ssafy', 1))
# ttbgz
print(caesar('Python', 10))
# Zidryx