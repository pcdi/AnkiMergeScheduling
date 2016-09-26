# Anki Addon 
This addon is used to combine duplicate cards.  
**Note:** backup anki before try this addon!

# Description
This addon will find out the cards which have the same definition, then combine these cards' "Reference" field and copy the combined "Reference" field to one card, this card will be marked as "needVerify", other duplicate cards are marked as "needRemove".

# Install
1. Copy CombineDuplicate.py under folder /Users/$LOGNAME/Documents/Anki/addons/.  
2. Run anki, click Tools->Combine Duplicate Cards.  
3. The duplicated cards will have tag "needRemove", the combined cards will have tag "needVerify".  
4. Make sure the cards combined correctly, then you can remove the cards with "needRemove" tag.
5. Remove "needVerify" tag.



