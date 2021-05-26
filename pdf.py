# documentation : https://pyfpdf.readthedocs.io/en/latest/index.html
from fpdf import FPDF

# PDFに関するクラス
class Pdf:
    pdf = None
    # PDFの初期化
    def __init__(self):
        self.pdf = FPDF('P', 'mm', 'Letter')
        self.pdf.set_auto_page_break(auto=True, margin=10)
        self.pdf.add_page()
        self.pdf.set_font('helvetica', "", 16)

    # PDFのx座標を取得
    def getX(self):
        return self.pdf.get_x()

    # PDFのy座標を取得
    def getY(self):
        return self.pdf.get_y()

    # PDFのx座標を設定
    def setX(self, x):
        self.pdf.set_x(x)

    # PDFのx座標, y座標を設定
    def setXY(self, x, y):
        self.pdf.set_xy(x, y)

    # PDFにデータ書き込み
    def setCell(self, x, y, text):
        self.pdf.cell(x, y, text, ln=1)

    # PDF生成
    def createPdf(self, path):
        self.pdf.output(path)
