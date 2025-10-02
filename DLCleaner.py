import os, shutil

DOWNLOAD = r"C:\Users\k.nunokawa\Downloads"

for f in os.listdir(DOWNLOAD):
    path = os.path.join(DOWNLOAD, f)
    if os.path.isfile(path):
        # 拡張子を取得
        parts = f.rsplit('.', 1)
        if len(parts) == 2:  # 拡張子あり
            ext = parts[1]
        else:  # 拡張子なし
            ext = "NoExt"

        folder = os.path.join(DOWNLOAD, ext.upper())
        os.makedirs(folder, exist_ok=True)
        shutil.move(path, os.path.join(folder, f))
