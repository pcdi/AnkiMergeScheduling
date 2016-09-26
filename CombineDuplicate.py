# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

def CombineDuplicateDefinitionCards():
    # get the number of cards in the current collection, which is stored in
    # the main window
    duplicateResult = mw.col.findDupes("Definition")

    if not duplicateResult:
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
