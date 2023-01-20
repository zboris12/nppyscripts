# -*- coding: utf-8 -*-
#
# 全角半角変換用情報
#
from Npp import editor

HAN_ASC = list(u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
HAN_NUM = list(u"0123456789")
HAN_SIG = list(u"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ")
HAN_KANA = list(u"ｧｱｨｲｩｳｪｴｫｵｶｷｸｹｺｻｼｽｾｿﾀﾁｯﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓｬﾔｭﾕｮﾖﾗﾘﾙﾚﾛﾜｦﾝ｡｢｣､･ﾞﾟｰ")

ZEN_ASC = list(u"ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ")
ZEN_NUM = list(u"０１２３４５６７８９")
ZEN_SIG = list(u"！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿‘｛｜｝￣　")
ZEN_KANA = list(u"ァアィイゥウェエォオカキクケコサシスセソタチッツテトナニヌネノハヒフヘホマミムメモャヤュユョヨラリルレロワヲン。「」、・゛゜ー")
ZEN_HIRA = list(u"ぁあぃいぅうぇえぉおかきくけこさしすせそたちっつてとなにぬねのはひふへほまみむめもゃやゅゆょよらりるれろわをん。「」、・゛゜ー")

DAKU_HAN = [u"ｳﾞ", u"ｶﾞ", u"ｷﾞ", u"ｸﾞ", u"ｹﾞ", u"ｺﾞ", u"ｻﾞ", u"ｼﾞ", u"ｽﾞ", u"ｾﾞ", u"ｿﾞ", u"ﾀﾞ", u"ﾁﾞ", u"ﾂﾞ", u"ﾃﾞ", u"ﾄﾞ", u"ﾊﾞ", u"ﾊﾟ", u"ﾋﾞ", u"ﾋﾟ", u"ﾌﾞ", u"ﾌﾟ", u"ﾍﾞ", u"ﾍﾟ", u"ﾎﾞ", u"ﾎﾟ"]
DAKU_KANA = list(u"ヴガギグゲゴザジズゼゾダヂヅデドバパビピブプベペボポ")
DAKU_HIRA = list(u"ゔがぎぐげござじずぜぞだぢづでどばぱびぴぶぷべぺぼぽ")

# -----------
#  配列の検索
# -----------
def arrayFind(a_arr, a_val):
    try:
        a_pos = a_arr.index(a_val)
    except ValueError:
        a_pos = -1
    finally:
        return a_pos

# -------------------------
#  選択中の文字列の置き換え
# -------------------------
def replaceSelect(a_str):
    if editor.selectionIsRectangle():
        a_st = editor.getRectangularSelectionCaret()
        a_ed = editor.getRectangularSelectionAnchor()
        a_col = editor.getColumn(a_st)
        a_stln = editor.lineFromPosition(a_st)
        a_edln = editor.lineFromPosition(a_ed)

        a_txts = a_str.split("\n")
        editor.deleteBackNotLine()
        for a_ln in range(a_stln, a_edln + 1):
            a_lned = editor.getLineEndPosition(a_ln)
            a_pos = editor.positionFromLine(a_ln) + a_col
            a_txt = a_txts[a_ln - a_stln]
            if len(a_txt) > 0:
                editor.insertText(a_pos, a_txt)
                a_ed = a_pos + editor.getLineEndPosition(a_ln) - a_lned

        editor.setRectangularSelectionCaret(a_st)
        editor.setRectangularSelectionAnchor(a_ed)

    else:
        a_st = editor.getSelectionStart()
        editor.replaceSel(a_str)
        a_ed = editor.getCurrentPos()
        editor.setSelectionStart(a_st)
        editor.setSelectionEnd(a_ed)

# ---------
#  変換処理
# ---------
def convert(a_fromArr, a_toArr, a_str=None):
    a_noret = (a_str is None)
    if a_noret:
        a_dat = editor.getSelText()
    else:
        a_dat = a_str

    if not type(a_dat) is unicode:
        a_dat = a_dat.decode("utf-8")
    a_arr = list(a_dat)
    a_flg = False
    for a_c in range(0, len(a_arr)):
        for a_i in range(0, len(a_fromArr)):
            a_pos = arrayFind(a_fromArr[a_i], a_arr[a_c])
            if a_pos >= 0:
                a_arr[a_c] = a_toArr[a_i][a_pos]
                a_flg = True
                break

    if a_flg:
        a_ret = "".join(a_arr)
        if a_noret:
            replaceSelect(a_ret)
        else:
            return a_ret
    elif not a_noret:
        return a_dat

# -----------------
#  英数字半角⇒全角
# -----------------
def han2zenAns(a_str=None):
    return convert([HAN_NUM, HAN_ASC, HAN_SIG], [ZEN_NUM, ZEN_ASC, ZEN_SIG], a_str)

# -----------------
#  英数字全角⇒半角
# -----------------
def zen2hanAns(a_str=None):
    return convert([ZEN_NUM, ZEN_ASC, ZEN_SIG], [HAN_NUM, HAN_ASC, HAN_SIG], a_str)

# -----------------
#  カナ半角⇒全角
# -----------------
def han2zenKana(a_str=None):
    a_noret = (a_str is None)
    if a_noret:
        a_dat = editor.getSelText()
    else:
        a_dat = a_str

    if not type(a_dat) is unicode:
        a_dat = a_dat.decode("utf-8")
    a_arr = list(a_dat)
    a_flg = False
    a_daku = ""
    a_daku_w = ""
    for a_c in range(len(a_arr)-1, -1, -1):
        a_chr = a_arr[a_c]
        if a_daku != "":
            a_pos = arrayFind(DAKU_HAN, a_chr + a_daku)
            a_daku = ""
            if a_pos >= 0:
                a_arr[a_c] = DAKU_KANA[a_pos]
                a_arr[a_c + 1] = u""
                a_flg = True
                continue
            else:
                a_arr[a_c + 1] = a_daku_w
                a_flg = True

        if a_chr == u"ﾞ":
            a_daku = a_chr
            a_daku_w = u"゛"
            continue
        elif a_chr == u"ﾟ":
            a_daku = a_chr
            a_daku_w = u"゜"
            continue

        a_pos = arrayFind(HAN_KANA, a_chr)
        if a_pos >= 0:
            a_arr[a_c] = ZEN_KANA[a_pos]
            a_flg = True

    if a_daku != "":
        a_arr[0] = a_daku_w
        a_flg = True

    if a_flg:
        a_ret = "".join(a_arr)
        if a_noret:
            replaceSelect(a_ret)
        else:
            return a_ret
    elif not a_noret:
        return a_dat

# -----------------
#  カナ全角⇒半角
# -----------------
def zen2hanKana(a_str=None):
    return convert([DAKU_KANA, ZEN_KANA], [DAKU_HAN, HAN_KANA], a_str)

# -----------------
#  カナ⇒ひら
# -----------------
def kana2hira(a_str=None):
    return convert([DAKU_KANA, ZEN_KANA], [DAKU_HIRA, ZEN_HIRA], a_str)

# -----------------
#  ひら⇒カナ
# -----------------
def hira2kana(a_str=None):
    return convert([DAKU_HIRA, ZEN_HIRA], [DAKU_KANA, ZEN_KANA], a_str)

#test
#print(han2zenAns("%abCd(123)"))
#aa = han2zenAns(han2zenKana("ﾟstｱﾞriﾎﾟngｶﾞ"))
#print(aa)
#bb = kana2hira(aa)
#print(bb)
#cc = hira2kana(bb)
#print(cc)
#print(zen2hanAns(zen2hanKana(cc)))
#han2zenKana()
