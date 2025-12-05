import vobject

vcard = vobject.vCard()
fn = vcard.add("FN")
fn.value = "이영찬"
name = vcard.add("N")
name.value = vobject.vcard.Name(family="이",given="영찬")

tel_cell = vcard.add("TEL")
tel_cell.value="+82(10)8706-2516"
tel_cell.type_param="CELL"
tel_home=vcard.add("TEL")
tel_home.value = "+82(055)323-0912"
tel_home.type_param="home"
print(vcard.serialize())