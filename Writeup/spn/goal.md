    目标：做完MetaTrust 2023和Openzeppelin CTF 2023
（metatrust 中有道zkp的题印象深刻，希望能与大佬们多多交流讨论🥹🥹）

metatrustctf byteVault
时隔n天后重新看ctf题（之前还一直是remix做题，现在换成foundry跟坐轮椅一样(♿️bushi♿️)

一眼withdraw函数问题
满足条件: 1.代码长度为奇数
        2.含有deadbeef字符串;
        3.立即执行
注：合约里面会用transfer调用sender，所以正常交互需要fallback/receive，这里本地测试的话就用了constructor跳过了（x