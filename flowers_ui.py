from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Thiết lập cửa sổ chính
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        
        # Widget trung tâm
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Nút tải lên
        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setGeometry(QtCore.QRect(410, 700, 180, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab Medium")
        self.uploadButton.setFont(font)
        self.uploadButton.setObjectName("uploadButton")
        
        # Nhãn cho tên ứng dụng
        self.label_nameApp = QtWidgets.QLabel(self.centralwidget)
        self.label_nameApp.setGeometry(QtCore.QRect(0, 30, 1000, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab Medium")
        font.setPointSize(24)
        self.label_nameApp.setFont(font)
        self.label_nameApp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nameApp.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_nameApp.setObjectName("label_nameApp")
        
        # Nhãn cho hình ảnh
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(55, 160, 500, 500))
        self.imageLabel.setMaximumSize(QtCore.QSize(900, 500))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab Medium")
        font.setPointSize(18)
        self.imageLabel.setFont(font)
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.imageLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageLabel.setLineWidth(5)
        self.imageLabel.setScaledContents(False)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        
        # Nhãn cho thông tin
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(610, 310, 340, 350))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(12)
        self.label_info.setFont(font)
        self.label_info.setFrameShape(QtWidgets.QFrame.Box)
        self.label_info.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_info.setLineWidth(1)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setWordWrap(True)
        self.label_info.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_info.setObjectName("label_info")
        
        # Nhãn cho các loài hoa
        self.label_flowers = QtWidgets.QLabel(self.centralwidget)
        self.label_flowers.setGeometry(QtCore.QRect(0, 85, 1000, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        self.label_flowers.setFont(font)
        self.label_flowers.setAlignment(QtCore.Qt.AlignCenter)
        self.label_flowers.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_flowers.setObjectName("label_flowers")
        
        # Nhãn cho dự đoán
        self.label_predict = QtWidgets.QLabel(self.centralwidget)
        self.label_predict.setGeometry(QtCore.QRect(610, 160, 340, 120))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab Medium")
        font.setPointSize(26)
        self.label_predict.setFont(font)
        self.label_predict.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_predict.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_predict.setLineWidth(3)
        self.label_predict.setMidLineWidth(0)
        self.label_predict.setAlignment(QtCore.Qt.AlignCenter)
        self.label_predict.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_predict.setObjectName("label_predict")
        
        # Thiết lập widget trung tâm
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Thanh menu
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # Thanh trạng thái
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Gán lại văn bản cho các phần tử giao diện khi chuyển đổi ngôn ngữ
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NHẬN DẠNG 5 LOÀI HOA"))
        self.uploadButton.setText(_translate("MainWindow", "UPLOAD"))
        self.label_nameApp.setText(_translate("MainWindow", "NHẬN DẠNG 5 LOÀI HOA"))
        self.imageLabel.setText(_translate("MainWindow", "Để đạt hiệu quả cao nhất,\n"
"hãy sử dụng hình ảnh tỉ lệ 1:1\n"
"và tập trung vào đối tượng."))
        self.label_info.setText(_translate("MainWindow", "THÔNG TIN"))
        self.label_flowers.setText(_translate("MainWindow", "[\'frangipani\', \'pinklotus\', \'purpleorchid\', \'redrose\', \'sunflower\']"))
        self.label_predict.setText(_translate("MainWindow", "DỰ ĐOÁN"))


# Nếu script được chạy trực tiếp
if __name__ == "__main__":
    # Import module sys để truy cập vào các tham số dòng lệnh
    import sys
    
    # Tạo một ứng dụng QApplication để quản lý các thành phần giao diện
    app = QtWidgets.QApplication(sys.argv)
    
    # Tạo một cửa sổ MainWindow để hiển thị giao diện
    MainWindow = QtWidgets.QMainWindow()
    
    # Tạo một đối tượng ui của lớp Ui_MainWindow để thiết lập giao diện cho cửa sổ MainWindow
    ui = Ui_MainWindow()
    
    # Gọi phương thức setupUi để thiết lập giao diện cho cửa sổ MainWindow
    ui.setupUi(MainWindow)
    
    # Hiển thị cửa sổ MainWindow lên màn hình
    MainWindow.show()
    
    # Chạy vòng lặp sự kiện của ứng dụng, đảm bảo ứng dụng luôn ở trạng thái chạy và sẵn sàng để nhận sự kiện từ người dùng
    sys.exit(app.exec_())
