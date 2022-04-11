import numpy as np


# グレゴリー級数
def gregory_progression(end=1000):
    phi = 0
    isTurnOver = True

    for i in range(1, end, 2):
        if isTurnOver:
            g = 4 * 1 / i
        else:
            g = -1 * 4 * 1 / i
        phi += g

        isTurnOver = not isTurnOver

        if i > end*0.99:             # 後ろの方だけ出力確認
            print(i, 'π=', phi)

    return phi


# モンテカルロ法
def montecarlo_method(count=100):
    bR = .5         # 半径
    sS = 0          # 四角のプロット数
    cS = 0          # 円のプロット数

    np.random.seed(0)   # 乱数を固定
    ps = np.random.uniform(-1*bR, bR, (count, 2))
    x = ps[:, 0]
    y = ps[:, 1]
    r0 = np.sqrt(x**2 + y**2)   # ランダムにプロットした点
    for r in r0:
        if bR > r:
            cS += 1   # 円の中
        sS += 1       # 四角形の中

    print('π=', 4. * cS / sS)

    return 4. * cS / sS
