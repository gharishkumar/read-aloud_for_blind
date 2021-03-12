# read-aloud_for_blind

Capture image using pi camear, use OCR image ➡️ text, use speech synthesis text ➡️ voice.
This helps blind to read text.

## Installation
 - [Install RaspberryPi OS](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit)
 - Make sure the internet is connected
 - Clone git repository
```bash
gh repo clone gharishkumar/read-aloud_for_blind
```
   **or**
 - Download the zip from the repository and unzip
```bash
wget https://github.com/gharishkumar/read-aloud_for_blind/archive/master.zip
unzip master.zip
cd read-aloud_for_blind-master
```
 - Install required packages by
```bash
 sudo sh install.sh
```

## Setup
 - Enable pi camera
```bash
 sudo raspi-config
```
![Enable camera](https://www.pyimagesearch.com/wp-content/uploads/2015/03/raspi_config-1024x768.jpg)
 - Connect the `circuit` as shown
![Circuit diagram](https://github.com/gharishkumar/read-aloud_for_blind/raw/main/read-aloud_for_blind_bb.png)

## Testing
 - Run `read-aloud_for_blind.py`
```bash
 python3 read-aloud_for_blind_final.py
```
 - Position the text infront of camera
 - Press the button
 - You should here the text read-aloud
## Run at startup
 - Add `read-aloud_for_blind.py` to [*startup*](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)


# Modules used
 - [tesseract-ocr](https://github.com/tesseract-ocr/tesseract)
 - [festvox](https://github.com/festvox/festvox) & [doc](http://www.festvox.org/flite/index.html)
# Reference
 - [capture image](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/)
 - [image ➡️ text](https://circuitdigest.com/microcontroller-projects/optical-character-recognition-ocr-using-tesseract-on-raspberry-pi)
 - [text ➡️ voice](https://www.bujarra.com/raspberry-pi-notificando-correos-electronicos-nuevos-y-citas-del-calendario/?lang=en)
 - [full-reader](https://hackaday.com/2018/03/02/diy-text-to-speech-with-raspberry-pi/)
 - [full-reader & book](https://hackaday.com/2014/05/10/brickpi-bookreader-1-and-2-read-tablets-or-books-aloud-you-choose/)
