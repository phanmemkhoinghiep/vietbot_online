
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
git clone -b beta --single-branch https://github.com/phanmemkhoinghiep/vietbot_online.git
```
Chờ cho đến khi kết thúc

### STEP2.  Download code về khi đã có Code, cần cập nhật lại

2.1. Truy cập vào thư mục vietbot_online

Quay về thư mục gốc
```sh
cd ~
```
Sau đó kiểm tra chính xác xem có trong nhánh beta hay không

```sh
pi@vietbot:~/vietbot_online/src $ git branch -vv
* beta b7da00f [origin/beta] Update 03_software_install_guide.md
```

Sau đó
```sh
cd /home/pi/vietbot_online/src
```
Check xem có file gì mới không

```sh
git fetch
```
Download các File mới về

```sh
git pull
```
### STEP3. Cài đặt các gói Python

3.1. Nâng cấp PIP

Chạy lần lượt các lệnh sau
```sh
python3 -m pip install --upgrade pip

```
3.2. Cài đặt các gói Python 

```sh
python3 -m pip install -r requirements.txt

```
