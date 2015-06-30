# coding: utf-8

"""
同階層にあるフォルダを zip 圧縮するスクリプト。
ただし、拡張子は、cbz とする。
フォルダ内のファイル名は 4 桁の連番となる。
フォルダ名が ( や - で始まる場合はスキップされる
"""

__author__  = 'mystblue'
__version__ = '0.0.1'
__date__    = '2013/11/12'

import os
import re
import Tkinter
import tkMessageBox
import zipfile

def show_message(num):
    """
    メッセージを出力する
    """
    root = Tkinter.Tk()
    root.withdraw()

    if num ==0:
        tkMessageBox.showinfo("終了", "フォルダが見つかりませんでした。")
    else:
        tkMessageBox.showinfo("終了", str(num) + "個のフォルダを圧縮しました。")

def compare(str1, str2):
    """
    ソートする。
    a, a1 -> -1
    a11, a1 -> 1
    """
    l1 = len(str1)
    l2 = len(str2)
    min = l2 if l1 >= l2 else l1
    isSymbol = lambda x: True if re.match(r"\.|\?|-|_|\[|\]|\(|\)|\+|\*|/|<|>|\!|\"|#|\$|%|\&|'|=|~|\^|@|\{|\}|:|;", x) else False
    for i in range(min):
        s1 = str1[i]
        s2 = str2[i]
        if s1 == s2 and not s1.isdigit() and not s2.isdigit():
            continue
        else:
            if s1.isdigit() and s2.isdigit():
                i1 = i + 1
                i2 = i + 1
                while i1 < l1:
                    if str1[i1].isdigit():
                        s1 += str1[i1]
                    else:
                        break
                    i1 += 1
                while i2 < l2:
                    if str2[i2].isdigit():
                        s2 += str2[i2]
                    else:
                        break
                    i2 += 1
                # 001 と 01 の場合は、01 の方が大きい
                if long(s1) == long(s2):
                    #print s1
                    #print s2
                    return cmp(str1, str2)
                else:
                    #print "s1 = " + s1
                    #print "s2 = " + s2
                    return -1 if long(s1) < long(s2) else 1
            if isSymbol(s1) and not isSymbol(s2):
                return -1
            if not isSymbol(s1) and isSymbol(s2):
                return 1
            if s1 == s2:
                return 0
            elif s1 > s2:
                return 1
            else:
                return -1
    return cmp(str1, str2)

def sort(array):
    """
    配列をソートする
    """
    array.sort(compare)
    return array

def is_img(ext):
    """
    画像ファイルかどうか
    """
    img_list = [".jpg", ".png", ".gif", ".bmp"]
    if ext.lower() in img_list:
        return True
    else:
        return False

def get_ext(filename):
    """
    指定したファイル名の拡張子を取得する
    """
    root, ext = os.path.splitext(filename)
    return ext

def get_filename(name, num):
    """
    連番のファイル名を取得する
    """
    return '%04d' % num + get_ext(name)

def zip_compress(path):
    """
    ZIP 圧縮を行う
    """
    zip = zipfile.ZipFile(path + ".cbz", 'w', zipfile.ZIP_DEFLATED)
    file_list = os.listdir(path)
    file_list = sort(file_list)
    counter = 1
    for file_name in file_list:
        if not is_img(get_ext(file_name)):
            continue
        zip.write(os.path.join(path, file_name),
                  get_filename(file_name, counter))
        counter = counter + 1
    zip.close()

def search_folder(rootDir):
    """
    rootDir 直下にフォルダがあれば、zip 圧縮する
    """
    count = 0
    file_list = os.listdir(rootDir)
    for file_name in file_list:
        path = os.path.join(rootDir, file_name)
        # ファイルは処理しない
        if not os.path.isdir(path):
            continue
        # ( や - で始まるフォルダも処理しない
        if file_name.startswith('(') or file_name.startswith('-'):
            continue
        #print file_name
        zip_compress(path)
        count = count + 1
    return count

if __name__ == "__main__":
    num = search_folder(".")
    show_message(num)
