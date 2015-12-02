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
    print "Caught Index error, not a problem."
else:
    print "We didn't catch any errors, and that's a problem."

instance = mt.InstanceMatrix()

instance.load('this')

a = instance.generate()
if a != "this":
    print "There was a problem generating from the instance matrix."
    print "Result: " + a

print "Tests finished."

pantheon = [u"Abholos", u"Alala", u"Ammutseba", u"Amon-Gorloth", u"Aphoom-Zhah", u"Apocolothoth", \
u"Arwassa", u"Atlach-Nacha", u"Ayi'ig", u"Aylith", u"Baoht Z'uqqa-Mogg", u"Basatan", u"B'gnu-Thun", \
u"Bokrug", u"Bugg-Shash", u"Byatis", u"Chaugnar Faugn", u"Caug-Narfagn", u"Coatlicue", u"Coinchenn", \
u"Crom Cruach", u"Cthaat", u"Cthaat Aquadingen", u"Cthaeghya", u"Cthugha", u"Cthulhu", u"Cthylla", \
u"Ctoggha", u"Cyäegha", u"Cynothoglys", u"Dhumin", u"Dygra", u"Dythalla", u"Dzéwà", u"Eihort", u"Ei'lor", \
u"Etepsed Egnis", u"Ghadamon", u"Ghatanothoa", u"Ghisguth", u"Glaaki", u"Gleeth", u"Gloon", u"Gobogeg", \
u"Gog-Hoor", u"Gol-goroth", u"Golothess", u"Groth-Golka", u"Gtuhanai", u"Gurathnaka", u"Gur'la-ya", \
u"Gzxtyos", u"Han", u"Hastalÿk", u"Hastur", u"H'chtelegoth", u"Hnarqu", u"Hziulquoigmnzhah", u"Idh-yaa", \
u"Inpesca", u"Iod", u"Istasha", u"Ithaqua", u"Janai'ngo", u"Juk-Shabb", u"Kaalut", u"Kag'Naru", \
u"Kassogtha", u"Kaunuzoth", u"Khal'kru", u"Klosmiebhyx", u"K'nar'st", u"Krang", u"Kurpannga", u"Lam", \
u"Lythalia", u"Mappo no Ryujin", u"M'basui Gwandu", u"M'Nagalah", u"Mnomquah", u"Mordiggian", u"Mormo", \
u"Mortllgh", u"Mynoghra", u"Nctosa & Nctolhu", u"Ngirrth'lu", u"Northot", u"Nssu-Ghahnb", u"Nug and Yeb", \
u"Nyaghoggua", u"Nycrama", u"Nyogtha", u"Ob'mbu", u"Oorn", u"Othuum", u"Othuyeg", u"Pharol", u"Poseidon", \
u"Psuchawrl", u"Ptar-Axtlan", u"Quachil Uttaus", u"Quyagen", u"Q'yth-az", u"Raandaii-B'nk", u"Ragnalla", \
u"Raphanasuan", u"Rhan-Tegoth", u"Rhogog", u"Rh'Thulla", u"Rokon", u"Ruhtra Dyoll", u"Saa'itii", u"Scathach", \
u"Sebek", u"Sedmelluq", u"Sfatlicllp", u"Shaklatal", u"Shathak", u"Shaurash-Ho", u"Sheb-Teth", u"Shlithneth", \
u"Sho-Gath", u"Shterot", u"Shudde M'ell", u"Shuy-Nihl", u"Sthanee", u"S'tya-Yg'Nalle", u"Summanus", u"Swarog", \
u"Thanaroa", u"Tharapithia", u"Thog", u"Th'rygh", u"Tsathoggua", u"Tulushuggua", u"Turua", u"Uitzilcapac", \
u"Ut'Ulls-Hr'Her", u"Vhuzompha", u"Vibur", u"Vile-Oct", u"Volgna-Gath", u"Voltiyig", u"Vthyarilops", \
u"Vulthoom", u"Gsarthotegga", u"Xalafu", u"Xcthol", u"Xinlurgash", u"Xirdneth", u"Xotli", u"Xoxiigghua", \
u"Yegg-Ha", u"Y'golonac", u"Yhagni", u"Yhashtur", u"Yig", u"Y'lla", u"'Ymnar", u"Yog-Sapha", u"Yorith", \
u"Ysbaddaden", u"Ythogtha", u"Yug-Siturath", u"Zathog", u"Zhar and Lloigor", u"Zindarak", u"Zoth-Ommog", \
u"Zstylzhemghi", u"Zystulzhemgni", u"Zushakon", u"Zuchequon", u"Z'toggua", u"Zvilpogghua"]

gen = mt.InstanceMatrix()
for g in pantheon:
    gen.load(g)

print gen.generate()
print gen.generate()
print gen.generate()
print gen.generate()

# a = gen._get_native_types()
# print repr(a)
