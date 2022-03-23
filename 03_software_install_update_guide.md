
### STEP1. Download code về Pi khi chưa có Code


Download Code về Pi theo cách sau:
1.1. Truy cập vào Git
Trên console của Pi, sử dụng lệnh sau
Quay về thư mục gốc
```sh
cd ~
```
Sau đó

```sh
git clone -b main --single-branch https://github.com/phanmemkhoinghiep/vietbot_online.git
```
Chờ cho đến khi kết thúc

### STEP2.  Download code về khi đã có Code, cần cập nhật lại

2.1. Truy cập vào thư mục vietbot_online

Quay về thư mục gốc
```sh
cd ~
```
Sau đó
```sh
cd /home/pi/vietbot_online
```
Check xem có file gì mới không

```sh
git fetch
```
Download các File mới về

```sh
git pull
```
