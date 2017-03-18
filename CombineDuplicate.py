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
            for f in  model["flds"]:
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

def CombineDuplicateDefinitionCards(self):
    """ Combine cards have the same field """
    field_name = ""
    fields = get_fields_name()
    fields_id = chooseField("Choose the field contain the duplicated content", fields)
    if fields_id != -1:
        field_name = fields[fields_id]
    else:
        return

    duplicateResult = mw.col.findDupes(field_name)

    if not duplicateResult:
        showInfo("No duplicate found")
        return

    tagRemovedCards = 0
    for s, nidlist in duplicateResult:
        firstNoteId = nidlist[0]
        removedNids = nidlist[1:]
        tagRemovedCards += len(removedNids)
        mw.col.tags.bulkAdd([firstNoteId], "needVerify")
        mw.col.tags.bulkAdd(removedNids, "needRemove")

        firstCardId = mw.col.findCards("nid:%d" % firstNoteId)[0]
        firstCard = mw.col.getCard(firstCardId)
        firstNote = firstCard.note() # Get first note
        for removedId in removedNids:
            removedCardId = mw.col.findCards("nid:%d" % removedId)[0]
            removedCard = mw.col.getCard(removedCardId)
            # Append the duplicate reference to first note
            firstNote["Reference"] = firstNote["Reference"] + "<br><br>" + removedCard.note()["Reference"]
            firstNote.flush()

    showInfo("Done")

# create a new menu item, "test"
action = QAction("Combine duplicate cards", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(CombineDuplicateDefinitionCards)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
