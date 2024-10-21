# Panorama Vision Agent

## Dependencies

```toml
python = ">=3.11,<3.14"
pyqt6 = "^6.7.1"
opencv-python = "^4.10.0.84"
pyinstaller = "^6.11.0"
```

## 📌Install Library

```PowerShell
# pip
pip install PyQt6 opencv-python pyinstaller
```
```PowerShell
# poetry
poetry add PyQt6 opencv-python pyinstaller
```

## How To Use This Application?

* PowerShell
```PowerShell
python <Your_App_Path>
```

* If you want to make exe file...
```PowerShell
pyinstaller <Your_App_Path>
```

### 1. Initial Screen


This is intial screen. `show`, `stitch`, `save` buttons are deactivated

![initial_page](img/{F93290E1-C4DF-477D-AF69-26564B4B85E4}.png)

### 2. Push `collect`

Check your Webcam

![collect_button](img/{E53CD804-674D-4518-99F0-01CFECF878E6}.png)

**On your keyboard, push...**
* C Button: Capture Video
* Q Button: Quit Video

If you capture Video (by pushing 'C') and quit your Webcam (by pushing 'Q'), `show`, `stitch`, `save` buttons will be activated.

### 3. Push `show`

Captured images will be displayed

![image_collection](img/{CA47A6D3-4C7C-4E6A-86FE-DF1A77030F6D}.png)


### 4. Push `stitch`

Panorama image will be displayed

![image_stitched_panorama](img/{1B8FC8F1-8F0E-4782-993C-21DE6E5FB6B6}.png)


### 5. Push `save`

Save your image.