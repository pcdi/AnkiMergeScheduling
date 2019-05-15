# Description
Please [backup](https://apps.ankiweb.net/docs/manual.html#backups) your collection before you use this addon.
This addon will copy the scheduling information from one card to another.
It looks for duplicates and then copies the due date, ease factor, next interval, lapses, how many reviews left for the card to graduate, queue, repetitions, and the card type.
It adds a `needsVerify` tag to the card to which the information was copied and a `needsRemove` tag to the card from which the information was copied.

# Installation
1. You can access the top level add-ons folder by going to the Tools>Add-ons menu item in the main Anki window. Click on the View Files button, and a folder will pop up. The add-ons folder is named `addons21`, corresponding to Anki 2.1.
2. Move the `AnkiMergeScheduling` folder into `addons21`.
3. Run Anki, then select Tools>Copy scheduling info.

# Manual copying
1. Open Anki’s [Debug Console](https://apps.ankiweb.net/docs/manual.html#debug-console).
2. Copy [Lines 61--77](https://github.com/pcdi/AnkiMergeScheduling/blob/master/__init__.py#L61-L77) to the prompt.
3. In the [Card Info](https://apps.ankiweb.net/docs/manual.html#card-info) window, copy the corresponding Note IDs (not Card IDs).
4. In the debug console, replace `nidlist[0]` and `nidlist[1]` with these Note IDs.
