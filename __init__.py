# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from aqt.utils import chooseList
import json


def get_fields_name():
    fields_name = set()
    for row in mw.col.db.execute("select models from col"):
        models = json.loads(row[0])
        for model in models.values():
            for f in model["flds"]:
                fields_name.add(f['name'])
    return list(fields_name)


def chooseField(prompt, choices):
    parent = mw.app.activeWindow()
    d = QDialog(parent)
    d.setWindowModality(Qt.WindowModal)
    l = QVBoxLayout()
    d.setLayout(l)
    t = QLabel(prompt)
    l.addWidget(t)
    c = QListWidget()
    c.addItems(choices)
    c.setCurrentRow(-1)
    l.addWidget(c)
    bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    bb.accepted.connect(d.accept)
    bb.rejected.connect(d.reject)
    l.addWidget(bb)
    if d.exec_():
        return c.currentRow()
    else:
        return -1


def CopyScheduling(self):
    """ Copy scheduling info of duplicate cards."""
    field_name = ""
    fields = get_fields_name()
    fields_id = chooseField(
        "Select the field that contains the duplicate content.", fields)
    if fields_id != -1:
        field_name = fields[fields_id]
    else:
        return

    duplicateResult = mw.col.findDupes(field_name)

    if not duplicateResult:
        showInfo("No duplicates found.")
        return

    for s, nidlist in duplicateResult:
        oldNoteId = nidlist[0]
        newNoteId = nidlist[1]
        oldCardId = mw.col.getNote(oldNoteId).cards()[0].id
        newCardId = mw.col.getNote(newNoteId).cards()[0].id
        oldCard = mw.col.getCard(oldCardId)
        newCard = mw.col.getCard(newCardId)
        newCard.due = oldCard.due
        newCard.factor = oldCard.factor
        newCard.ivl = oldCard.ivl
        newCard.lapses = oldCard.lapses
        newCard.left = oldCard.left
        newCard.queue = oldCard.queue
        newCard.reps = oldCard.reps
        newCard.type = oldCard.type
        newCard.flushSched()
        mw.col.tags.bulkAdd([newNoteId], "needsVerify")
        mw.col.tags.bulkAdd([oldNoteId], "needsRemove")

    showInfo("Done.")


# create a new menu item
action = QAction("Copy scheduling info", mw)
# set it to call the function when it's clicked
action.triggered.connect(CopyScheduling)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
