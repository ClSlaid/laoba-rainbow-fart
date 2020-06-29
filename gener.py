# -*- coding: utf-8 -*

try:
    import ujson as json
except:
    import json

import sys
import os


def main():

    # Parsing parameters
    list = []

    update = False

    if len(sys.argv) == 1:
        list = os.listdir('./')
    elif len(sys.argv) == 2:
        list = os.listdir(sys.argv[1])
    elif len(sys.argv) == 3:
        list = os.listdir(sys.argv[1])
        if sys.argv[2] == '-u':
            update = True
    else:
        print('请将语音文件放至本脚本同目录执行本脚本\n或者\n命令行运行本脚本并带上语音文件目录参数')
        return
    try:
        list.remove(sys.argv[0])
    except:
        pass
    
    # Read manifest.json
    path = 'manifest.json'
    if update:
        path = os.path.join(sys.argv[1], path)

    if not os.path.exists(path):
        print('没找到 ' + path + ' 请确认')
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = json.loads(f.read())

    for c in content['contributes']:
        newVoices = []
        for v in list:
            suffix = v[v.rfind('.') + 1:]
            if detectionFormat(suffix):
                newVoices.append(v)
        c['voices'] = newVoices

    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(content))


'''
@description: Check if the file suffix is ​​legal
@param {type} 
@return: 
'''
def detectionFormat(suffix):
    supportSuffix = ['mp3', 'aac', 'wav', 'wma']
    for s in supportSuffix:
        if s == suffix:
            return True
    return False


if __name__ == "__main__":
    main()
