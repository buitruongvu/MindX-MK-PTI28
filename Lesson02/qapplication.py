import sys
# Nhập module sys, một module cơ bản của Python cung cấp các hàm và các biến được sử dụng để thao tác các phần khác nhau của môi trường chạy Python.
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
#Nhập 2 lớp QApplication và QWidget.
#QApplication là lớp chính để quản lý ứng dụng đồ họa, QWidget là lớp để tạo ra cửa sổ (màn hình) đồ họa trống.
app = QApplication(sys.argv)
# Dòng này tạo một đối tượng ứng dụng
# PyQt6 sử dụng lớp QApplication. Đối tượng này là một đại diện cho ứng dụng đồ họa và nó làm cho PyQt6 được kích hoạt và sẵn sàng để chạy.
window = QWidget()
# Tạo một đối tượng cửa sổ đồ họa sử dụng lớp QWidget. Đối tượng window này đại diện cho cửa sổ giao diện chính của ứng dụng của chúng ta.
button = QPushButton("Click Me", window)
button.setGeometry(100, 100, 100, 30)
window.show()
# Phương thức show() của lớp QWidget giúp hiển thị cửa sổ giao diện vì theo mặc định khi cửa sổ được tạo ra nó sẽ bị ẩn đi.
app.exec()
# Bắt đầu vòng lặp, nội dung được lập trình sau dòng 6 sẽ không được thực thi đến khi ứng dụng được đóng.







