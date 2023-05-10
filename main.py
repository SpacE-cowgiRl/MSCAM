# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from MyDialog import Ui_Dialog  # 导入GUI文件
from MyFigure import *  # 嵌入了matplotlib的文件

from pathlib import Path
import nibabel as nib
import numpy as np

class MainDialogImgBW(QDialog, Ui_Dialog):
    def __init__(self):
        super(MainDialogImgBW, self).__init__()
        # 读取QSS文件中的内容
        with open('style.qss', 'r') as f:
            qss = f.read()
        self.setupUi(self)
        self.Myui()
        self.setWindowTitle(" ")
        #self.MainWindow.setStyleSheet(qss)
        self.setMinimumSize(0, 0)

        #设置背景
        bg = QBrush(QPixmap("bg.png"))
        palette = self.palette()
        palette.setBrush(QPalette.Background, bg)
        #palette.setColor(QPalette.Window, QColor(37, 37, 38))
        self.setPalette(palette)

        # 创建存放nii文件路径的属性
        self.nii_path = ''
        # 创建存放mask文件路径的属性
        self.mask_path = ''
        # 创建记录nii文件里面图片数量的属性
        self.shape = 1
        # 创建用于检查radio button选择标记的属性，选择'nii图像'，为0，现在‘mask图像’，为1
        self.check = 0
        # 创建用于记录是否选中画笔，选择画笔为1，未选中为0
        self.draw = 0

        # 定义MyFigure类的一个实例
        self.F = MyFigure(width=3, height=3, dpi=100)
        # 在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F, 0, 1)
        #here5
        # if self.mask_path != '':
        #     self.mask_data = nib.load(Path(self.mask_path)).get_fdata()
        #     # 获取mask图像的尺寸
        #     self.mask_shape = self.mask_data.shape
        #     #将图像与绘图方法连接起来
        #     self.mask_data.mousePressEvent = self.on_mousePressEvent

    #here9
    # def on_mousePressEvent(self, event: QMouseEvent):
    #     # 获取当前坐标
    #     pos = event.pos()
    #     x, y = pos.x(), pos.y()
    #     print(f"pos: {pos}")
    #     mask_value = self.mask_data[y, x, 1]
    #     print(mask_value)
    #     #test
    #     # for x in range(1,256):
    #     #     for y in range(1,256):
    #     #         if self.data[y, x, 1]==1:
    #     #             print(y,x)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    sys.exit(app.exec_())
