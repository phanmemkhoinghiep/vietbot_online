### ĐÂY LÀ HƯỚNG DẪN CÀI ĐẶT PHẦN HỆ ĐIỀU HÀNH, THƯ VIỆN, DRIVER CHO PI ZERO WIRLESS, MODUN 2 MIC HAT, 4 MIC ARRAY HOẶC MIC USB TỪ IMAGE CÓ SẴN

### STEP1. Download bộ Image cho Raspberry Pi đã cài đặt sẵn

1.1. Download bộ Image cho Raspberry Pi đã cài đặt sẵn Drive cho Respeaker 2 Mic Hat, Respeaker USB Mic và Mic USB thường tại Link sau

![GOOGLE DRIVE](https://drive.google.com/file/d/1jY3hx7nrfd-ukf4AeMss5YgZkauzemWO/view?usp=sharing)

![FSHARE](https://www.fshare.vn/file/WUBPA38PI75U)


### STEP2. Ghi vào thẻ SD

2.1. Dùng Win32IMG để ghi vào thẻ nhớ SD

### STEP3. Khai báo WiFi

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


### STEP4. Sử dụng

4.1. Sử dụng

4.1.1. Cắm thẻ nhớ vào Pi Zero 2 W/Pi 3B+/Pi4 và boot lên

4.1.2. Sử dụng SSH để truy cập từ xa vào Console

4.1.3. Nhập Username và password đăng nhập (pi/vietbot)

4.2. Nâng dung lượng của OS cho Full thẻ

4.2.1. Chạy lệnh sau

```sh
sudo raspi-config
}

4.2.2. Chọn Advance

4.2.3. Chọn Expand File System

4.2.4. Chọn OK và chờ vài s

4.2.5. Chọn Yes để Reboot

Tiếp đó chuyển qua 

![CÀI ĐẶT, CẬP NHẬT PHẦN MỀM](https://github.com/phanmemkhoinghiep/vietbot_online/blob/main/03_software_install_update_guide.md)  
