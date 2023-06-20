ui = int(input())
dp = [3,7]

if ui>2:
    for i in range(ui-2):
        dp.append((2*dp[-1]+dp[-2])%9901)
    print(dp[-1])

else:
    print(dp[ui-1])

#modulo연산의 성질 : https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-addition-and-subtraction
