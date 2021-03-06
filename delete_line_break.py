import re
import copy
import csv
import time

def delete_line_break():
    #不適な改行を削除する対象ファイル名を選択してください
    target_file = "gbizinfo.csv"
    #出力するファイル名を選択してください
    output_filename = "out.txt"
    one_line_before = ""
    fileobj = open(target_file, "r", encoding="utf_8")
    text_file = open(output_filename, "wt", encoding="utf_8")
    #一つのファイルの中の処理
    while True:
        line = fileobj.readline()
        if not line:
            text_file.write(one_line_before)
            fileobj.close()
            break
        if one_line_before:
            if not (line.startswith('\"')):
                one_line_before = copy.deepcopy(one_line_before.strip() + line)
                continue
            #新しいファイルに書き込んで行く
            text_file.write(one_line_before)
        one_line_before = copy.deepcopy(line)
    text_file.close()

delete_line_break()