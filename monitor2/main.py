import subprocess
import time
import pygetwindow as gw


def launch_application(app_path):
    try:
        subprocess.Popen([app_path])
        print("アプリケーション を起動しました。")
    except Exception as e:
        print(f"アプリケーション の起動に失敗しました。エラー: {e}")


if __name__ == "__main__":
    ezstation_path = r"C:\Path\To\EZStation3.0.exe"  # 実際のパスに置き換える
    launch_application(ezstation_path)
    time.sleep(5)  # アプリケーションが起動するまで待機
