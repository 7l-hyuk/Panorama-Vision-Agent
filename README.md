# Panorama Vision Agent

## Dependencies

이 프로젝트는 windows11 운영체제에서 제작됐습니다.

```toml
python = ">=3.11,<3.14"
pyqt6 = "^6.7.1"
opencv-python = "^4.10.0.84"
pyinstaller = "^6.11.0"
opencv-contrib-python = "^4.10.0.84"
```

## 📌Install Library

```PowerShell
poetry install
```

## How To Use This Application?

* PowerShell
```PowerShell
python <Your_App_Path>
```

* exe file
  
[panorama_vision_agent.exe](./installation)

### 1. 처음 화면

![alt text](img\initial_screen.png)

처음에는 collect 버튼만 활성화 돼 있습니다. collect 버튼을 눌러 웹캠을 활성화 합니다.

![webcam](img\webcam.png)

웹캠이 활성화 되면 c 버튼을 눌러 화면 캡쳐가 가능하고, q 버튼을 눌러 웹캠을 종료할 수 있습니다.

### 2. 웹캠 종료 후

![activated_button](img\button_activated.png)

웹캠이 종료되면 show, stitch, save 버튼이 활성화 됩니다. 

* `show`: 캡처된 이미지를 볼 수 있습니다.
* `stitch`: 캡처된 이미지로 파노라마 사진을 제작합니다.
* `save`: 만들어진 파노라마 이미지를 저장합니다.

### 3. 추가 기능: 파노라마 사진 저장 후

![activated_button](img\button_activated2.png)

파노라마 사진이 저장되면 해당 사진에 특수 효과를 적용할 수 있는 버튼이 활성화 됩니다. 특정 특수 효과를 지정하고 그 사진을 저장할 수 있습니다.