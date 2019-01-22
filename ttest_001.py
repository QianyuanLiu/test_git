#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
for line in sys.stdin:
    a, b, c = line.split()
    # print(int(a[0]) + int(a[1]))
    # print(a, b, c)
    a,b,c = list(map(int, line.split()))
    num = 0
    a_flag = b_flag = c_flag = num_falg = 0
    for i_a in range(a+1):
        for i_b in range(b+1):
            for i_c in range(c+1):
                # a_flag = b_flag = c_flag = num_falg = 0
                if 1<=i_a<=a:
                    a_flag = 1
                if 1<=i_b<=b:
                    b_flag = 1
                if 1<=i_c<=c:
                    c_flag = 1
                if (i_a + i_b < i_c) or (i_a + i_c < i_b) or (i_c + i_b < i_a):
                    num_falg = 1
                if a_flag and b_flag and c_flag and num_falg :
                    num = num + 1
                    a_flag = b_flag = c_flag = num_falg = 0
    print(num%1000000007)
