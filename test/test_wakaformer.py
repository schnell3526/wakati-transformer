from wakaformer import WakaFormer

wf = WakaFormer()

def test_wakati_01():
    text = "雨が降ってきたので傘を買いに近くのコンビニへ立ち寄った。"
    output = wf.wakati(text)
    assert output == "雨 が 降って きた ので 傘 を 買い に 近く の コンビニ へ 立ち寄った 。"

def test_wakati_02():
    text = "価格が引き上げられるのは、牛めしや定食の一部メニューで、来月2日午後2時から全国の店舗で実施される。"
    output = wf.wakati(text)
    assert output == "価格 が 引き上げ られる の は 、 牛 めし や 定食 の 一部 メニュー で 、 来月 2 日 午後 2 時 から 全国 の 店舗 で 実施 さ れる 。"

def test_wakati_03():
    text = "外国人参政権"
    output = wf.wakati(text)
    assert output == "外国 人 参政 権"