# -*- coding: utf-8 -*-
#
# Prepare python environment
# 1. Download souce code of PyYAML 5.4.1
#    https://pypi.org/project/PyYAML/5.4.1/#files
#    (Target file: PyYAML-5.4.1.tar.gz)
# 2. Open the downloaded file by 7zip
# 3. Extract folder "PyYAML-5.4.1\lib\yaml" into the lib folder of notepad++
#    (For example: D:\notepad++\plugins\PythonScript\lib\yaml)

from Npp import editor, notepad
import yaml
import json

# -------------------------
#  Sort json or yaml
# -------------------------
def sort(a_str):
    a_type = 0
    try:
        a_fnm = notepad.getCurrentFilename()
        a_pos = a_fnm.rindex(".") + 1
        a_fext = a_fnm[a_pos:].lower()
        if a_fext == "json":
            a_type = 1
        elif a_fext == "yaml":
            a_type = 2
    except:
        pass

    if a_type == 0:
        if a_str[0:1] == "{":
            a_type = 1
        else:
            a_type = 2

    a_obj = None
    try:
        if a_type == 1:
            a_obj = json.loads(a_str)
        else:
            a_obj = yaml.safe_load(a_str)
    except:
        pass

    if a_obj is None:
        return None
    elif a_type == 1:
        return json.dumps(a_obj, sort_keys=True, indent=2)
    else:
        return yaml.safe_dump(a_obj, allow_unicode=True, sort_keys=True, indent=2)

# Main
isSel = True
txt = editor.getSelText()
if len(txt) == 0:
    txt = editor.getText()
    isSel = False
txt = sort(txt)
if not txt is None:
    if isSel:
        st = editor.getSelectionStart()
        editor.replaceSel(txt)
        ed = editor.getCurrentPos()
        editor.setSelectionStart(st)
        editor.setSelectionEnd(ed)
    else:
        editor.setText(txt)
