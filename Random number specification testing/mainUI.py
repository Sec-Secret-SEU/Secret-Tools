import datetime
import os

import sys
import time

from PyQt6 import QtWidgets
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QFrame, QInputDialog
from PyQt6.QtGui import QColor

from UIClass import UiClass
import main
import Monobit_frequency
import Block_frequency_test
import Pocker_test
import Runs_test
import Autocorrelation_test
import Approximate_entropy_test
import Serial_test
import Longest_run_of_ones_in_a_block
import Binary_derivative_test


class Mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.not_clicked_color = QColor(255, 255, 255)
        self.clicked_color = QColor(255, 215, 0)
        self.ui = UiClass()
        self.ui.setupUi(self)

        # 按钮
        self.ui.pushButton.clicked.connect(self.test_click)  # 点击计算按钮
        self.ui.pushButton2.clicked.connect(self.select_from_file)  # 点击选择文件按钮
        self.ui.pushButton3.clicked.connect(self.random_click)  # 点击随机生成按钮
        self.ui.check_boxes[0].setProperty("event", Mywindow.checkbox1_event)
        self.ui.check_boxes[1].setProperty("event", Mywindow.checkbox2_event)
        self.ui.check_boxes[2].setProperty("event", Mywindow.checkbox3_event)
        self.ui.check_boxes[3].setProperty("event", Mywindow.checkbox4_event)
        self.ui.check_boxes[4].setProperty("event", Mywindow.checkbox5_event)
        self.ui.check_boxes[5].setProperty("event", Mywindow.checkbox6_event)
        self.ui.check_boxes[6].setProperty("event", Mywindow.checkbox7_event)
        self.ui.check_boxes[7].setProperty("event", Mywindow.checkbox8_event)
        self.ui.check_boxes[10].setProperty("event", Mywindow.checkbox11_event)
        # self.ui.check_boxes[1].setProperty("event", Mywindow.checkbox11_event)

        # 创建一个QFrame小部件作为分割线
        # line = QFrame(self)
        # line.setGeometry(335, 15, 2, 390)  # 设置分割线的位置和大小
        # line.setFrameShape(QFrame.Shape.VLine)  # 设置分割线的形状为垂直线
        # line.setStyleSheet("background-color: #DDDDDD;")  # 设置分割线的颜色为黑色

    # 单比特检测
    def checkbox1_event(self, bits):
        start_time = time.time()  # 记录开始时间
        is_success, P_value, Q_value = Monobit_frequency.for_UI(bits)
        end_time = time.time()  # 记录结束时间
        interval_time = end_time - start_time

        text = '未通过'
        if is_success:
            text = '通过'
        self.res += "单比特频数检测结果:  " + text + "  P_value:" + str(P_value) + "  Q_value:" + str(Q_value) + '  耗时:' + str(
            interval_time * 1000) + 'ms' + '\n'
        self.ui.textEdit_2.setText(self.res)

    # 块内频数检测
    def checkbox2_event(self, bits):
        start_time = time.time()  # 记录开始时间
        is_success, P_value, Q_value = Block_frequency_test.for_UI(bits)
        end_time = time.time()  # 记录结束时间
        interval_time = end_time - start_time

        text = '未通过'
        if is_success:
            text = '通过'
        self.res += "块内频数检测结果:  " + text + "  P_value:" + str(P_value) + "  Q_value:" + str(Q_value) + '  耗时:' + str(
            interval_time * 1000) + 'ms' + '\n'
        self.ui.textEdit_2.setText(self.res)

    # 扑克检测
    def checkbox3_event(self, bits):
        start_time = time.time()  # 记录开始时间
        is_success, P_value, Q_value = Pocker_test.for_UI(bits)
        end_time = time.time()  # 记录结束时间
        interval_time = end_time - start_time

        text = '未通过'
        if is_success:
            text = '通过'
        self.res += "扑克检测结果:  " + text + "  P_value:" + str(P_value) + "  Q_value:" + str(Q_value) + '  耗时:' + str(
            interval_time * 1000) + 'ms' + '\n'
        self.ui.textEdit_2.setText(self.res)

    # 重复子序列检测
    def checkbox4_event(self, bits):
        start_time = time.time()  # 记录开始时间
        is_success, P1_value, P2_value, Q1_value, Q2_value = Serial_test.for_UI(bits)
        end_time = time.time()  # 记录结束时间
        interval_time = end_time - start_time

        text = '未通过'
        if is_success:
            text = '通过'
        self.res += "重叠子序列检测结果:  " + text + "  P1_value:" + str(P1_value) + "  P2_value:" + str(
            P2_value) + '  耗时:' + str(
            interval_time * 1000) + 'ms' + '\n'
        self.ui.textEdit_2.setText(self.res)

    # 游程检测
    def checkbox5_event(self, bits):
        start_time = time.time()  # 记录开始时间
        is_success, P1_value, P2_value = Runs_test.for_UI(bits)
        end_time = time.time()  # 记录结束时间
        interval_time = end_time - start_time

        text = '未通过'
        if is_success:
            text = '通过'
        self.res += "游程检测结果:  " + text + "  P1_value:" + str(P1_value) + "  P2_value:" + str(
            P2_value) + '  耗时:' + str(interval_time * 1000) + 'ms' + '\n'
        self.ui.textEdit_2.setText(self.res)

    # 块内最大游程检测
    def checkbox6_event(self, bits):
        start_time = time.time()  # 记录开始时间
        is_success, P_value, Q_value = Longest_run_of_ones_in_a_block.for_UI(bits)
        end_time = time.time()  # 记录结束时间
        interval_time = end_time - start_time

        text = '未通过'
        if is_success:
            text = '通过'
        self.res += "块内最大游程检测结果:  " + text + "  P_value:" + str(P_value) + "  Q_value:" + str(Q_value) + '  耗时:' + str(
            interval_time * 1000) + 'ms' + '\n'
        self.ui.textEdit_2.setText(self.res)

    # 二元推导检测
    def checkbox7_event(self, bits):
        start_time = time.time()  # 记录开始时间
        is_success, P_value, Q_value = Binary_derivative_test.for_UI(bits)
        end_time = time.time()  # 记录结束时间
        interval_time = end_time - start_time

        text = '未通过'
        if is_success:
            text = '通过'
        self.res += "二元推导检测结果:  " + text + "  P_value:" + str(P_value) + "  Q_value:" + str(Q_value) + '  耗时:' + str(
            interval_time * 1000) + 'ms' + '\n'
        self.ui.textEdit_2.setText(self.res)

    # 自相关检测
    def checkbox8_event(self, bits):
        start_time = time.time()  # 记录开始时间
        is_success, P_value, Q_value = Autocorrelation_test.for_UI(bits)
        end_time = time.time()  # 记录结束时间
        interval_time = end_time - start_time

        text = '未通过'
        if is_success:
            text = '通过'
        self.res += "自相关检测结果:  " + text + "  P_value:" + str(P_value) + "  Q_value:" + str(Q_value) + '  耗时:' + str(
            interval_time * 1000) + 'ms' + '\n'
        self.ui.textEdit_2.setText(self.res)

    # 近似熵检测
    def checkbox11_event(self, bits):
        start_time = time.time()  # 记录开始时间
        is_success, P_value, Q_value = Approximate_entropy_test.for_UI(bits)
        end_time = time.time()  # 记录结束时间
        interval_time = end_time - start_time

        text = '未通过'
        if is_success:
            text = '通过'
        self.res += "近似熵检测结果:  " + text + "  P_value:" + str(P_value) + "  Q_value:" + str(Q_value) + '  耗时:' + str(
            interval_time * 1000) + 'ms' + '\n'
        self.ui.textEdit_2.setText(self.res)

    def checkbox15_event(self):
        print("执行选择按钮15的事件")

    # 点击计算
    def test_click(self):
        # 读取用户输入字符串
        text = self.ui.textEdit_1.toPlainText()
        if text != '':
            bits = list(self.ui.textEdit_1.toPlainText())
            if not self.is_binary_sequence(bits):
                # 如果包含了01外的其他字符，弹出提示框 提示用户
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Icon.Warning)
                msgBox.setWindowTitle("Warning")
                msgBox.setText("检测到序列含有01外其他字符！")
                msgBox.setStandardButtons(QMessageBox.StandardButton.Cancel)
                msgBox.exec()
                return -1
            selected_checkboxes = [checkbox for checkbox in self.ui.check_boxes if checkbox.isChecked()]
            # if len(selected_checkboxes) == 15:
            self.res = ''
            for checkbox in selected_checkboxes:
                checkbox_event = checkbox.property("event")
                if checkbox_event is not None:
                    checkbox_event(self, bits)
        else:
            # 弹出提示框 提示用户
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Warning")
            msgBox.setText("检测到序列为空！")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Cancel)
            msgBox.exec()

    # 点击选择文件
    def select_from_file(self):
        # 打开文件选择对话框
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setDirectory(r'../data/')  # 设置默认打开路径为data文件夹
        file_dialog.setNameFilter("TXT Files (*.txt)")

        file_path = ''
        if file_dialog.exec():
            # 获取所选文件路径
            file_path = file_dialog.selectedFiles()[0]
            # print(file_path)
        with open(file_path, 'r') as file:
            self.ui.textEdit_1.setPlainText(file.readline())

    # 点击随机生成并报错到文件中
    def random_click(self):
        # 弹出对话框，让用户输入序列位数
        number, ok = QInputDialog.getInt(self, "输入随机序列的位数", "请输入一个整数：")
        if ok:
            print("输入随机序列位数为:", number)

        random_list, random_str = main.generate_random_sequence(number)
        self.ui.textEdit_1.setPlainText(random_str)

        # 写入到文件中，以当前时间命名
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = current_time + ".txt"
        file_path = r'D:\cryptology\data\{}'.format(file_name)
        with open(file_path, 'w') as file:
            os.write(file.fileno(), random_str.encode())
            print("写入随机数据到", file_path, "成功")

    # 检查序列是否只有01
    def is_binary_sequence(self, blist):
        unique_elements = set(blist)
        return (len(unique_elements) == 2 or len(unique_elements) == 1) and all(
            element in {'0', '1'} for element in unique_elements)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    sys.exit(app.exec())
