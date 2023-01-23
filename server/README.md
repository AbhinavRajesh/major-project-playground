# PYTHON SERVER

Server for streaming application

## Inital Setup

1. Download the zip file: [ffmeg-github-release](https://github.com/GyanD/codexffmpeg/releases/download/2022-06-06-git-73302aa193/ffmpeg-2022-06-06-git-73302aa193-essentials_build.zip)
2. Unzip the file and copy the 3 files `ffprobe`, `ffplay` and `ffmpeg` from the `bin` folder
3. Paste the copied files in the same location of your `python.exe` file. <br />
   (In windows, it's at `C:\Users\username\AppData\Local\Programs\Python\Python310`.

## Create Python Virtual Environment

### Windows

```powershell
py -m venv env
```

### Linux

```sh
python3 -m venv env
```

## Activate Python Virtual Environment and run server

### Windows

```sh
source env/Scripts/activate
py server.py
```

### Linux

```sh
source env/bin/activate
python3 server.py
```
