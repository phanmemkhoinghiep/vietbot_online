### ĐÂY LÀ HƯỚNG DẪN CÀI ĐẶT PHẦN HỆ ĐIỀU HÀNH, THƯ VIỆN, DRIVER CHO PI ZERO WIRLESS, MODUN 2 MIC HAT, 4 MIC ARRAY HOẶC MIC USB TỪ IMAGE CÓ SẴN

### STEP1. Download bộ Image cho Raspberry Pi đã cài đặt sẵn

Download bộ Image cho Raspberry Pi đã cài đặt sẵn cho tất cả các loại Mic tại Link sau

[GOOGLE DRIVE FILE NÉN 1.4G](https://drive.google.com/file/d/1SZwM6F2k0eiubYJ0VcXg47Me68E9WReX/view?usp=sharing)

### STEP2. Ghi vào thẻ SD

2.1. Dùng Win32IMG để ghi vào thẻ nhớ SD

### STEP3. Khai báo WiFi
có thể tải file wpa_supplicant.conf mẫu chuẩn ở link này, rồi sửa lại ID wifi và pass wifi cho đúng. Hoặc làm file mới như hướng dẫn phía dưới
[GOOGLE DRIVE](https://drive.google.com/file/d/1D2iFC-sP2PUL-RijPmK9yKo3IsgEAvJ8/view?usp=sharing)

3.1. Sử dụng Notepad ++ để tạo file có tên là wpa_supplicant.conf trong thư mục boot của thẻ nhớ

3.2. Set định dạng File
Định dạng file Unix (Edit -> EOL converion -> UNIX/OSX Format là Unix (LF)), nội dung là các tham số tên SSID và mật khẩu tương ứng

3.3. Đặt nội dung
Chú ý, tham số country có thể đổi sang us hoặc vn tùy theo cài đặt tại bộ phát WiFi
```sh
country=vn
update_config=1
ctrl_interface=/var/run/wpa_supplicant
network={
    ssid="testing"
    psk="testingPassword"
}
```
3.4. Save lại nội dung File

3.5. Tạo một file rỗng có tên là SSH
có thể tải file SSH mẫu chuẩn ở link này
[GOOGLE DRIVE](https://drive.google.com/file/d/1QCAYZMTlXJ7Zx3ZW8iKjiXDVuGqZMqTc/view?usp=sharing)


### STEP4. Kết nối và điều chỉnh

4.1. Kết nối

4.1.1. Cắm thẻ nhớ vào Pi Zero 2 W/Pi 3B+/Pi4 và boot lên

4.1.2. Tìm địa chỉ IP của pi và sử dụng SSH để truy cập từ xa vào Console

4.1.3. Nhập Username và password đăng nhập (pi/vietbot)

4.2. Nâng dung lượng của OS cho Full thẻ

4.2.1. Chạy lệnh sau

```sh
sudo raspi-config
```
4.2.2. Chọn Advance

4.2.3. Chọn Expand File System

4.2.4. Chọn OK và chờ vài s

4.2.5. Chọn Yes để Reboot

### STEP5. Khai báo Mic

5.1. Khai báo Mic 2 Hat, Mic 4Hat

5.1.1. Tạo một file rỗng asound.conf tại thư mục /home/pi như sau

```sh
sudo nano /home/pi/.asoundrc
```
Gõ space bar sau đó gõ backspace
Bấm lần lượt Ctrl + X, sau đó Y rồi Enter

5.1.2. Copy file thiết lập cho mọi account (Nếu chỉ dùng Account Pi thì bỏ qua bước này)

Chạy lệnh sau
```sh
sudo cp /home/pi/.asoundrc /etc/asound.conf
```

5.2. Khai báo Mic USB (Mic USB thường và Mic Respeaker USB)

5.2.1. Thống kê ID của Mic USB và Loa 

Chạy lệnh sau để biết ID của Mic USB
```sh
arecord -l
```
sau đó chạy lệnh sau để biết ID của Loa

```sh
aplay -l
```
Lưu lại thông tin về card_id và device_id ở mỗi kết quả lệnh

5.2.2. Khai báo Default cho ALSA

Chạy lệnh sau 

```sh
sudo nano /usr/share/alsa/alsa.conf
```
Cửa sổ nano hiện lên, tìm tới 2 dòng sau
```sh
# defaults
defaults.ctl.card 0
defaults.pcm.card 0

```
Thay thế ký tự '0' bằng kết quả đã lưu cho <card_id>, ví dụ 1

tiếp tục tìm tới 2 dòng sau
```sh
# defaults
defaults.pcm.device 0
defaults.pcm.subdevice 0
```
Thay thế ký tự '0' bằng kết quả đã lưu cho <device_id>, ví dụ 1 (Nếu 0 thì ko phải thay)

5.2.3. Đưa Account đang dùng (Ví dụ pi) vào group root

Chạy lệnh sau
```sh
sudo usermod -aG root pi
```
5.2.4. fix lỗi bot không hoạt động sau 1 thời gian.
Chạy lệnh sau
```sh
sudo usermod -aG audio root
```
5.2.5. Reboot lại Pi
Chạy lệnh sau
```sh
sudo reboot
```

Tiếp đó chuyển qua 

![CÀI ĐẶT, CẬP NHẬT PHẦN MỀM](https://github.com/phanmemkhoinghiep/vietbot_online/blob/main/03_software_install_update_guide.md) 

