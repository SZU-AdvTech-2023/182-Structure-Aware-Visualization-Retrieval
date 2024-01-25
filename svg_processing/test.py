import os
import shutil
import subprocess
import cairosvg
from PIL import Image
script_dir = os.path.dirname(os.path.abspath(__file__))

# 删除目录
def remove_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)

# 创建目录
def create_directory(directory):
    os.makedirs(directory, exist_ok=True)

# 切换工作目录到脚本所在目录
os.chdir(script_dir)
for i in ['train', 'test']:
    os.makedirs(f'../full_VizML+/{i}_graph', exist_ok=True)
    os.makedirs(f'../full_VizML+/{i}_json', exist_ok=True)

    for j in ['line', 'bar', 'scatter', 'box', 'histogram']:
        print(i, j)
        os.makedirs(f'../full_VizML+/{i}_graph/{j}', exist_ok=True)
        os.makedirs(f'../full_VizML+/{i}_json/{j}', exist_ok=True)
        subprocess.run(['node', 'parse.js', i ,j])

