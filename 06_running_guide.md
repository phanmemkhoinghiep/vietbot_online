
### STEP1. Chạy Manual

1.1. Truy nhập vào thư mục Bot
Sử dụng lệnh sau

```sh
cd vietbot_online/src
```
1.2. Edit config bằng lệnh 

```sh
sudo nano create_config.py
```
1.3. Tạo file config sau khi Edit xong bằng lệnh 

```sh
python3 create_config.py
```
1.4. Chạy boot bằng lệnh 

```sh
python3 start.py
```
1.4. Ra lệnh bằng từ khóa

Sau khi có kết quả thành công, ra lệnh bằng từ khóa đã có trong file confg.json sẽ có tiếng Ting và bắt đầu chờ để ra lệnh


### STEP2.  Chạy tự động khi khởi động Pi

2.1. Chạy bằng Supervisor 

2.1.1. Cài đặt supervisor (Nếu chưa cài)

```sh
sudo apt-get install supervisor -y
```
2.1.2. Tạo file vietbot.conf bằng lệnh

```sh
sudo nano /etc/supervisor/conf.d/vietbot.conf
```
Tại cửa sổ Nano, gõ dòng lệnh sau

```sh
[program:vietbot]
directory=/home/pi/vietbot_online/src
command=/bin/bash -c 'cd /home/pi/vietbot_online/src && python3 start.py'
numprocs=1
autostart=true
autorestart=true
startretries=0 
```
Bấm Ctrl + X, Y, Enter

2.1.3. Gõ lệnh sau

```sh
sudo supervisorctl update
```
Hệ thống sẽ hiện ra
```sh
vietbot: added process group
```
Hệ thống đã sẵn sàng tự động chạy vietbot

2.1.4. Gõ lệnh sau để chạy vietbot
```sh
sudo supervisorctl start vietbot
```
hoặc
```sh
sudo reboot
```
2.1.5. Gõ lệnh sau để xem log
```sh
sudo supervisorctl tail -f vietbot stdout
```
2.1.6. Gõ lệnh sau để remove chạy tự động

Gõ lện để stop

```sh
sudo supervisorctl stop vietbot
```

```sh
sudo rm -rf /etc/supervisor/conf.d/vietbot.conf
```
Sau đó gõ tiếp

```sh
sudo supervisorctl update
```
Hệ thống sẽ hiện ra
```sh
vietbot: removed process group
```
Hệ thống đã gỡ vietbot khỏi chạy tự động

2.2. Tự động bằng crontab

2.2.1. Tạo nơi lưu log

```sh
cd ~
mkdir logs
```
2.2.2. Khai báo crontab

```sh
crontab -e
```
Chọn 1 để edit bằng nano 
Tại cửa sổ nano, di chuyển xuống dòng cuối cùng rồi gõ

```sh
@reboot sh /home/pi/vietbot_online/src/start.sh >/home/pi/logs/cronlog 2>&1
```
Bấm Ctrl + X, Y, Enter

2.2.3. Khởi động lại Pi 

```sh
sudo reboot
```
Bot sẽ tự động chạy khi khởi động Pi (Chú ý thời gian chạy của bot có thể lâu sau khi khởi động)

2.2.4. Xem log khi chạy

```sh
cat /home/pi/logs/cronlog
```
2.2.5. Gỡ tự động chạy khi khởi động Pi (Nếu cần)

```sh
crontab -e
```
Chọn 1 để edit bằng nano 

Tại cửa sổ nano, di chuyển xuống dòng cuối cùng rồi xóa dòng sau

```sh
@reboot sh /home/pi/vietbot_online/src/start.sh >/home/pi/logs/cronlog 2>&1
```
Bấm Ctrl + X, Y, Enter

Khởi động lại Pi 

```sh
sudo reboot
```
Bot sẽ không tự động chạy khi khởi động Pi nữa
