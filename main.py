import random
import pdf

# 足し算に関する問題を生成 & 解答用にデータ格納を行う関数
# 戻り値 : 問題内容
def addition():
    formerNumber = random.randint(2, 1000)
    latterNumber = random.randint(2, 100)

    # 解答用にデータ格納
    answers['addition']['formerNumbers'].append(formerNumber)
    answers['addition']['latterNumbers'].append(latterNumber)
    answers['addition']['sumNumbers'].append(formerNumber + latterNumber)

    return f"{formerNumber} + {latterNumber} ="

# 引き算に関する問題を生成 & 解答用にデータ格納を行う関数
# 戻り値 : 問題内容
def substraction():
    while True:
        formerNumber = random.randint(1, 1000)
        latterNumber = random.randint(1, 100)

        # マイナスになる問題を生成しない。
        if formerNumber > latterNumber:
            # 解答用にデータ格納
            answers['substraction']['formerNumbers'].append(formerNumber)
            answers['substraction']['latterNumbers'].append(latterNumber)
            answers['substraction']['sumNumbers'].append(formerNumber - latterNumber)
            break

    return f"{formerNumber} - {latterNumber} ="

# 掛け算に関する問題を生成 & 解答用にデータ格納を行う関数
# 戻り値 : 問題内容
def multiplication():
    formerNumber = random.randint(1, 100)
    latterNumber = random.randint(1, 10)

    # 解答用にデータ格納
    answers['multiplication']['formerNumbers'].append(formerNumber)
    answers['multiplication']['latterNumbers'].append(latterNumber)
    answers['multiplication']['sumNumbers'].append(formerNumber * latterNumber)

    return f"{formerNumber} × {latterNumber} ="

# 割り算に関する問題を生成 & 解答用にデータ格納を行う関数
# 戻り値 : 問題内容
def division():
    while True:
        formerNumber = random.randint(1, 1000)
        latterNumber = random.randint(2, 100)

        # 割り切れない問題を生成しない。
        if formerNumber % latterNumber == 0:
            # 解答用にデータ格納
            answers['division']['formerNumbers'].append(formerNumber)
            answers['division']['latterNumbers'].append(latterNumber)
            answers['division']['sumNumbers'].append(
                round(formerNumber / latterNumber))
            break

    return f"{formerNumber} ÷ {latterNumber} ="

# 問題、解答の生成を行う関数
# num : 現在index(位置)の問題、解答の番号
def calculateMaker(num):
    # PDFヘ書き込む際の情報一覧
    # setX : PDFヘ書き込む際のx座標
    # setY : PDFヘ書き込む際のy座標
    # functionName : PDFヘ書き込む際に実行する関数
    # symbol : functionNameを記号で表した1文字
    infoList = [
        {
            'setX': 10,
            'setY': (10 + 260 * num),
            'functionName': 'addition',
            'symbol': '+',
        },
        {
            'setX': 65,
            'setY': 10,
            'functionName': 'substraction',
            'symbol': '-',
        },
        {
            'setX': 110,
            'setY': 10,
            'functionName': 'multiplication',
            'symbol': 'x',
        },
        {
            'setX': 160,
            'setY': 10,
            'functionName': 'division',
            'symbol': '÷',
        }
    ]

    # 解答に関する情報を格納する。
    # ページ単位で更新されるため、global変数を用いる。
    global answers
    answers = {
        'addition': {
            'formerNumbers': [],
            'latterNumbers': [],
            'sumNumbers': [],
        },
        'substraction': {
            'formerNumbers': [],
            'latterNumbers': [],
            'sumNumbers': [],
        },
        'multiplication': {
            'formerNumbers': [],
            'latterNumbers': [],
            'sumNumbers': [],
        },
        'division': {
            'formerNumbers': [],
            'latterNumbers': [],
            'sumNumbers': [],
        }
    }

    for info in infoList:
        # postionの設定
        pdfIns.setXY(info['setX'], info['setY'])
        for i in range(Number_OF_PROBLEMS_PER_SYMBOL):
            # postionのx座標設定
            pdfIns.setX(info['setX'])
            # 関数の呼び方参考 : https://qiita.com/Chanmoro/items/9b0105e4c18bb76ed4e9
            # 問題を書き込む。
            pdfIns.setCell(WRITE_X_POINT, WRITE_Y_POINT, globals()[info['functionName']]())

    # @todo 何か良い方法があれば修正したい。
    # 解答を書き込む前に1ページ座標を進めておく。
    infoList[0]['setY'] = (10 + 260 * (num + 1))

    # 解答を生成する。
    for info in infoList:
        # postionの設定
        pdfIns.setXY(info['setX'], info['setY'])
        for n in range(Number_OF_PROBLEMS_PER_SYMBOL):
            # postionのx座標設定
            pdfIns.setX(info['setX'])
            # 解答を書き込む。
            pdfIns.setCell(WRITE_X_POINT, WRITE_Y_POINT, f"{answers[info['functionName']]['formerNumbers'][n]} {info['symbol']} {answers[info['functionName']]['latterNumbers'][n]} = {answers[info['functionName']]['sumNumbers'][n]}")

# 問題枚数を定数化
Number_OF_PROBLEMS = 2
# 足し算、引き算、掛け算、割り算それぞれの問題数を定数化
Number_OF_PROBLEMS_PER_SYMBOL = 25
# データを書き込む際のx座標
WRITE_X_POINT = 50
# データを書き込む際のy座標
WRITE_Y_POINT = 10

# PDFに関するinstanceを生成する。
pdfIns = pdf.Pdf()

# 問題、解答の生成
for num in range(Number_OF_PROBLEMS):
    calculateMaker(num)

# PDF生成
pdfIns.createPdf("output.pdf")
