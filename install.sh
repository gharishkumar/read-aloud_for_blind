sudo apt update
sudo apt install -y python3-opencv tesseract-ocr
sudo pip3 install "picamera[array]" pytesseract
sudo apt-get -y install festival
amixer cset numid=3 1
wget https://github.com/guadalinex-archive/hispavoces/raw/master/packages/festvox-palpc16k_1.0-1_all.deb
sudo dpkg -i festvox-palpc16k_1.0-1_all.deb
