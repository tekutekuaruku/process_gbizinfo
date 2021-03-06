import pandas as pd
import os
import copy
import math

def item_checker():
    company_info = [["法人番号", "法人名", "法人名ふりがな", "法人名英語", "郵便番号", "本社所在地", "ステータス", "登記記録の閉鎖等年月日",
     "登記記録の閉鎖等の事由",	"法人代表者名", "法人代表者役職", "資本金", "従業員数", "企業規模詳細(男性)", "企業規模詳細(女性)", "営業品目リスト",
     "事業概要", "企業ホームページ", "設立年月日", "創業年", "最終更新日"]]
    index = 0
    #対象ファイルを選択してください
    target_file = "out.csv"
    info_list = pd.read_csv(target_file, encoding="utf_8_sig", na_filter=False, dtype=str).values.tolist()
    while index < len(info_list):
        #確かめたい項目の配列の位置を指定
        if info_list[index][2]:
            company_info.append(info_list[index])
        index += 1
    columns1 = company_info[0]
    company_info.pop(0)
    df = pd.DataFrame(data = company_info, columns = columns1)
    #出力するファイル名を指定してください
    df.to_csv('company_output/output_info_210302.csv', encoding="utf_8_sig")
    return

item_checker()