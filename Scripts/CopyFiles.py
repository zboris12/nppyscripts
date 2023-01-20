# -*- coding: utf-8 -*-
#

from Npp import editor, console
from datetime import datetime
import os
import shutil

LOG = True
SRCDIR = "C:/aaa/"
DESDIR = "C:/bbb/"

def consolog(msg):
    if not console.editor.getReadOnly():
        console.editor.addText(datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")[0:23])
        console.editor.addText(" " + msg + "\n")

def makedirs(tgtdir):
    if not os.path.exists(tgtdir):
        consolog("Create dir: " + tgtdir)
        os.makedirs(tgtdir)

def copyfile(srcdir, desdir, target):
    desfpath = os.path.join(desdir, target)
    makedirs(os.path.dirname(desfpath))
    shutil.copyfile(os.path.join(srcdir, target), desfpath)

def main():
    if LOG:
        console.editor.setReadOnly(False)
        console.show()
    consolog("From dir: " + SRCDIR)
    consolog("To dir  : " + DESDIR)
    consolog("Start copy")

    i = 0
    txt = editor.getText()
    for ln in txt.splitlines():
        ln = ln.lstrip()
        if len(ln) > 0 and ln[0] != "#":
            i += 1
            copyfile(SRCDIR, DESDIR, ln)

    consolog(str(i) + " files copied")

    if not console.editor.getReadOnly():
        console.editor.setReadOnly(True)

main()
