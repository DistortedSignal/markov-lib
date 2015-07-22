# -*- coding: utf-8 -*-
import markov_tool as mt

ins = mt.InstanceList()

if ins._get_native_types() != (0, {}):
    print "There was a problem instantiating the InstanceList."
    print ins._get_native_types()

ins['a'] = 1
if ins['a'] != 1 or ins._get_native_types() != (1, {'a': 1}):
    print "There was a problem setting/getting an item."
    print ins._get_native_types()

ins['a'] += 1
if ins['a'] != 2 or ins._get_native_types() != (2, {'a': 2}):
    print "There was a problem setting/getting an item."
    print ins._get_native_types()

ins['b'] = 2

result = ins._InstanceList__get_next_token(lambda x, y: 0)
if result != 'a':
    print "There was a problem getting the next token (value: 0). Actual value: " + \
    str(result)
    print ins._get_native_types()

result = ins._InstanceList__get_next_token(lambda x, y: 1)
if result != 'a':
    print "There was a problem getting the next token (value: 1). Actual value: " + \
    str(result)
    print ins._get_native_types()

result = ins._InstanceList__get_next_token(lambda x, y: 2)
if result != 'b':
    print "There was a problem getting the next token (value: 2). Actual value: " + \
    str(result)
    print ins._get_native_types()

result = ins._InstanceList__get_next_token(lambda x, y: 3)
if result != 'b':
    print "There was a problem getting the next token (value: 3). Actual value: " + \
    str(result)
    print ins._get_native_types()

try:
    result = ins._InstanceList__get_next_token(lambda x, y: 4)
except IndexError as e:
    print "Caught Index error"
else:
    print "We didn't catch any errors, and that's a problem."

instance = mt.InstanceMatrix()

instance.load('this')

a = instance.generate()
if a != "this":
    print "There was a problem generating from the instance matrix."
    print "Result: " + a

print "Tests finished."

pantheon = ["Abholos", "Alala", "Ammutseba", "Amon-Gorloth", "Aphoom-Zhah", "Apocolothoth", \
"Arwassa", "Atlach-Nacha", "Ayi'ig", "Aylith", "Baoht Z'uqqa-Mogg", "Basatan", "B’gnu-Thun", \
"Bokrug", "Bugg-Shash", "Byatis", "Chaugnar Faugn", "Caug-Narfagn", "Coatlicue", "Coinchenn", \
"Crom Cruach", "Cthaat", "Cthaat Aquadingen", "Cthaeghya", "Cthugha", "Cthulhu", "Cthylla", \
"Ctoggha", "Cyäegha", "Cynothoglys", "Dhumin", "Dygra", "Dythalla", "Dzéwà", "Eihort", "Ei'lor", \
"Etepsed Egnis", "Ghadamon", "Ghatanothoa", "Ghisguth", "Glaaki", "Gleeth", "Gloon", "Gobogeg", \
"Gog-Hoor", "Gol-goroth", "Golothess", "Groth-Golka", "Gtuhanai", "Gurathnaka", "Gur'la-ya", \
"Gzxtyos", "Han", "Hastalÿk", "Hastur", "H’chtelegoth", "Hnarqu", "Hziulquoigmnzhah", "Idh-yaa", \
"Inpesca", "Iod", "Istasha", "Ithaqua", "Janai'ngo", "Juk-Shabb", "Kaalut", "Kag'Naru", \
"Kassogtha", "Kaunuzoth", "Khal'kru", "Klosmiebhyx", "K'nar'st", "Krang", "Kurpannga", "Lam", \
"Lythalia", "Mappo no Ryujin", "M’basui Gwandu", "M'Nagalah", "Mnomquah", "Mordiggian", "Mormo", \
"Mortllgh", "Mynoghra", "Nctosa & Nctolhu", "Ngirrth’lu", "Northot", "Nssu-Ghahnb", "Nug and Yeb", \
"Nyaghoggua", "Nycrama", "Nyogtha", "Ob'mbu", "Oorn", "Othuum", "Othuyeg", "Pharol", "Poseidon", \
"Psuchawrl", "Ptar-Axtlan", "Quachil Uttaus", "Quyagen", "Q'yth-az", "Raandaii-B'nk", "Ragnalla", \
"Raphanasuan", "Rhan-Tegoth", "Rhogog", "Rh'Thulla", "Rokon", "Ruhtra Dyoll", "Saa'itii", "Scathach", \
"Sebek", "Sedmelluq", "Sfatlicllp", "Shaklatal", "Shathak", "Shaurash-Ho", "Sheb-Teth", "Shlithneth", \
"Sho-Gath", "Shterot", "Shudde M'ell", "Shuy-Nihl", "Sthanee", "S'tya-Yg'Nalle", "Summanus", "Swarog", \
"Thanaroa", "Tharapithia", "Thog", "Th'rygh", "Tsathoggua", "Tulushuggua", "Turua", "Uitzilcapac", \
"Ut'Ulls-Hr'Her", "Vhuzompha", "Vibur", "Vile-Oct", "Volgna-Gath", "Voltiyig", "Vthyarilops", \
"Vulthoom", "Gsarthotegga", "Xalafu", "Xcthol", "Xinlurgash", "Xirdneth", "Xotli", "Xoxiigghua", \
"Yegg-Ha", "Y'golonac", "Yhagni", "Yhashtur", "Yig", "Y'lla", "'Ymnar", "Yog-Sapha", "Yorith", \
"Ysbaddaden", "Ythogtha", "Yug-Siturath", "Zathog", "Zhar and Lloigor", "Zindarak", "Zoth-Ommog", \
"Zstylzhemghi", "Zystulzhemgni", "Zushakon", "Zuchequon", "Z'toggua", "Zvilpogghua"]

gen = mt.InstanceMatrix()
for g in pantheon:
    gen.load(g)

a = gen._get_native_types()
print repr(a)
