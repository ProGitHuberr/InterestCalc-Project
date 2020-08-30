from PyQt5 import QtCore, QtGui, QtWidgets


def valid_input(number, wanted):

    try:
        if wanted == 'float':
            value = float(number)
        if wanted == 'int':
            value = int(number)

    except ValueError:
        return None

    else:
        if value <= 0:
            return None
        else:
            return value


def auto_format(int_number):

    number = str(int_number)
    scrambled_number = []
    formatted_list = []
    final_list = []
    final_number = ''

    for char in number:
        scrambled_number.insert(0, char)

    count = 1

    for scrambled in scrambled_number:
        formatted_list.append(scrambled)

        if count % 3 == 0:
            formatted_list.append(' ')

        count += 1

    for formatted in formatted_list:
        final_list.insert(0, formatted)

    if final_list[0] == ' ':
        del final_list[0]
    if final_list[-1] == ' ':
        del final_list[-1]

    for final in final_list:
        final_number += final

    return final_number


def save_tab(years, input_interest, monthly):

    months = years * 12
    months_left = months
    interest = input_interest / 100 + 1
    total = 0

    while months_left != 0:
        spec_month = monthly * (interest ** (months_left // 12))
        last_months = (spec_month * (interest - 1) / 12) * (months_left % 12)
        total += spec_month + last_months

        months_left -= 1

    total_string = auto_format(str(round(total)))
    total_savings = auto_format(str(round(months * monthly)))

    return f"Saved: {total_savings}kr\nReturned: {total_string}kr"


def earn_tab(savings, input_interest):
    interest = input_interest / 100
    per_month = round((savings * interest) / 12)
    return f"Earn: {auto_format(per_month)}kr"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(0, 0, 411, 541))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.tab_widget.setFont(font)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.years_line_edit = QtWidgets.QLineEdit(self.tab_1)
        self.years_line_edit.setGeometry(QtCore.QRect(220, 80, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.years_line_edit.setFont(font)
        self.years_line_edit.setObjectName("years_line_edit")
        self.interest_line_edit = QtWidgets.QLineEdit(self.tab_1)
        self.interest_line_edit.setGeometry(QtCore.QRect(220, 190, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.interest_line_edit.setFont(font)
        self.interest_line_edit.setObjectName("interest_line_edit")
        self.monthly_line_edit = QtWidgets.QLineEdit(self.tab_1)
        self.monthly_line_edit.setGeometry(QtCore.QRect(220, 300, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.monthly_line_edit.setFont(font)
        self.monthly_line_edit.setObjectName("monthly_line_edit")
        self.calc_button_1 = QtWidgets.QPushButton(self.tab_1)
        self.calc_button_1.setGeometry(QtCore.QRect(210, 410, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        self.calc_button_1.setFont(font)
        self.calc_button_1.setObjectName("calc_button_1")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(10, 70, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.tab_widget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.savings_line_edit = QtWidgets.QLineEdit(self.tab_2)
        self.savings_line_edit.setGeometry(QtCore.QRect(40, 70, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.savings_line_edit.setFont(font)
        self.savings_line_edit.setObjectName("savings_line_edit")
        self.interest_spin_box = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.interest_spin_box.setGeometry(QtCore.QRect(110, 200, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.interest_spin_box.setFont(font)
        self.interest_spin_box.setObjectName("interest_spin_box")
        self.calc_button_2 = QtWidgets.QPushButton(self.tab_2)
        self.calc_button_2.setGeometry(QtCore.QRect(80, 410, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.calc_button_2.setFont(font)
        self.calc_button_2.setObjectName("calc_button_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(90, 140, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(40, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.tab_widget.addTab(self.tab_2, "")
        self.list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget.setGeometry(QtCore.QRect(430, 40, 341, 501))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.list_widget.setFont(font)
        self.list_widget.setObjectName("list_widget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 540, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.calc_button_1.clicked.connect(self.save_tab_action)
        self.calc_button_2.clicked.connect(self.earn_tab_action)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "InterestCalc"))
        self.calc_button_1.setText(_translate("MainWindow", "Calculate"))
        self.label.setText(_translate("MainWindow", "Years"))
        self.label_2.setText(_translate("MainWindow", "Annual Interest %"))
        self.label_3.setText(_translate("MainWindow", "Monthly Savings"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(
            self.tab_1), _translate("MainWindow", "Save"))
        self.calc_button_2.setText(_translate("MainWindow", "Calculate"))
        self.label_4.setText(_translate("MainWindow", "Annual Interest %"))
        self.label_5.setText(_translate("MainWindow", "Savings"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(
            self.tab_2), _translate("MainWindow", "Earn"))
        self.label_6.setText(_translate(
            "MainWindow", "©  Aron H. Björkvald 2020"))

    def save_tab_action(self):

        years = valid_input(self.years_line_edit.text(), 'int')
        comma_value = self.interest_line_edit.text()

        if comma_value.find(',') != -1:
            dot_value = comma_value.replace(',', '.')
        else:
            dot_value = comma_value

        interest = valid_input(dot_value, 'float')
        monthly = valid_input(self.monthly_line_edit.text(), 'int')

        self.years_line_edit.clear()
        self.interest_line_edit.clear()
        self.monthly_line_edit.clear()

        if years == None or interest == None or monthly == None:
            item = 'Invalid Input'
        else:
            item = save_tab(years, interest, monthly)

        self.list_widget.addItem(item)

    def earn_tab_action(self):

        savings = valid_input(self.savings_line_edit.text(), 'int')
        comma_interest = self.interest_spin_box.text()
        interest = valid_input(comma_interest.replace(',', '.'), 'float')

        self.savings_line_edit.clear()
        self.interest_spin_box.clear()

        if savings == None or interest == None:
            item = 'Invalid Input'
        else:
            item = earn_tab(savings, interest)

        self.list_widget.addItem(item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
