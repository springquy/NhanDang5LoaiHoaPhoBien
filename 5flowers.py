import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from flowers_ui import Ui_MainWindow  # Import giao diện
from keras.saving import load_model
import numpy as np
from keras.preprocessing import image


class FlowerRecognitionApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()  # Gọi hàm khởi tạo của lớp cha
                
        self.setupUi(self)  # Thiết lập giao diện người dùng
        
        # Kết nối nút tải lên với hàm load_image
        self.uploadButton.clicked.connect(self.load_image)  
        
        # Các loài hoa
        self.flowers = ['Frangipani', 'Pink Lotus', 'Purple Orchid', 'Red Rose', 'Sunflower']
        
        # Thông tin về các loài hoa
        self.information = [
            'Frangipani (Plumeria), người Việt thường gọi là hoa sứ hoặc hoa đại. Đa dạng về màu sắc, nhưng hoa sứ trắng-vàng được ưa chuộng nhất. Đặc biệt là ở Hawaii, những vòng hoa sứ là biểu tượng của lòng \nhiếu khách và tình bạn.',
            'Pink Lotus là hoa sen hồng,\nquốc hoa của nước Việt Nam.\nSở dĩ, không chỉ vì vẻ đẹp \nthánh thiện mà còn vì khả năng sống mạnh mẽ, vươn lên giữa \nbùn đất và toả hương ngan ngát giữa trời đất, là biểu tượng của \nsức sống bất diệt.',
            'Purple Orchid là hoa lan tím,\nbiểu tượng của sự sang trọng, \nquý phái và sự huyền bí.\nNó thường được dùng làm \nquà tặng cao cấp trong các \nsự kiện quan trọng như \nđám cưới và hội nghị.',
            'Red Rose là hoa hồng đỏ,\nbiểu tượng toàn cầu về \ntình yêu và sự lãng mạn.\nNó thường được sử dụng để \nthể hiện tình cảm chân thành \nvà sâu đậm trong các dịp \nđặc biệt như lễ tình nhân, \nkỷ niệm, và ngày cưới.',
            'Sunflower là hoa hướng dương. Chúng là biểu tượng của sức sống mãnh liệt. Đặc biệt hơn hết,\nhoa hướng dương luôn dõi theo \nánh mặt trời, tượng trưng cho \ntinh thần kiên định và \nniềm tin vào tương lai.'            
        ]
        
        self.model = load_model('5flowers_model.h5')  # Load mô hình khi khởi động ứng dụng
        

    def load_image(self):
        options = QFileDialog.Options()     # Mở hộp thoại để người dùng chọn hình ảnh
        fileName, _ = QFileDialog.getOpenFileName(self, "Tải lên hình ảnh", "", "Image Files (*.png *.jpg)", options=options)
        if fileName:
            pixmap = QPixmap(fileName)      # Chuyển đổi file hình ảnh thành QPixmap để hiển thị
            self.display_image(pixmap)      # Hiển thị hình ảnh trên QLabel
            self.predict_flower(fileName)   # Dự đoán loài hoa sau khi đã tải ảnh lên
            
            
    def display_image(self, pixmap):
        # Lấy kích thước của QLabel
        label_width = self.imageLabel.width()
        label_height = self.imageLabel.height()

        # Thu/Phóng hình ảnh để vừa với QLabel mà vẫn giữ nguyên tỉ lệ
        scaled_pixmap = pixmap.scaled(label_width, label_height, Qt.KeepAspectRatio)
        
        # Đặt hình ảnh đã được thay đổi kích thước vào QLabel
        self.imageLabel.setPixmap(scaled_pixmap)    
        
        
    def predict_flower(self, file_path):
        # Đọc và tiền xử lý hình ảnh
        img = image.load_img(file_path, target_size=(224,224))  # Đọc hình ảnh và thay đổi kích thước
        img = image.img_to_array(img)                           # Chuyển đổi hình ảnh thành mảng số
        img = np.expand_dims(img, axis=0)                       # Thêm một chiều để phù hợp với đầu vào của mô hình
        img /= 255                                              # Chuẩn hóa giá trị pixel

        # Dự đoán
        prediction = self.model.predict(img)                # Dự đoán và lấy kết quả dưới dạng vector xác suất
        prediction_index = np.argmax(prediction)            # Lấy chỉ số của nhãn có xác suất dự đoán cao nhất
        prediction_flower = self.flowers[prediction_index]  # Lấy nhãn tương ứng với chỉ số dự đoán
        information = self.information[prediction_index]    # Lấy thông tin tương ứng

        # Hiển thị dự đoán
        self.label_predict.setText(f'{prediction_flower}')  # Hiển thị tên loài hoa dự đoán
        self.label_info.setText(f'{information}')           # Hiển thị thông tin về loài hoa dự đoán


if __name__ == "__main__":
    app = QApplication(sys.argv)            # Tạo ứng dụng PyQt5
    mainWindow = FlowerRecognitionApp()     # Tạo cửa sổ chính của ứng dụng
    mainWindow.show()                       # Hiển thị cửa sổ chính
    sys.exit(app.exec_())                   # Bắt đầu vòng lặp sự kiện chính của ứng dụng
