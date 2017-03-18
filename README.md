# Anki Addon
This addon is used to combine duplicate cards.
**Note:** backup anki before try this addon!

# Description
This addon will find out the cards which have the same field, then try to combine the "Reference" field of these cards. The combined card will has a tag "needVerify", the duplicate cards are tagged as "needRemove".

# Install
1. Copy CombineDuplicate.py under addons folder(Tools->Add-ons->Open Add-ons Folder...).
2. Run anki, click Tools->Combine Duplicate Cards.
3. Click "Browse" tag, on the left side, there are two new tags:"needRemove" and "needVerity". The duplicated cards have tag "needRemove", the combined cards have tag "needVerify".
4. Make sure the cards combined correctly, then you can remove the cards with "needRemove" tag.
5. Remove "needVerify" tag.



