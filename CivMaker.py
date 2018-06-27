import sys
import re
import random
from typing import Dict, List


def error(string_err):
    print(string_err)
    exit()


UnitsTable: Dict[str, str] = {}
UnitsTable['CybranT1Land'] = 'URB0101'
UnitsTable['AeonQGate'] = 'UAB0304'
UnitsTable['AeonT1pgen'] = 'UAB1101'
UnitsTable['AeonEStorage'] = 'UAB1105'
UnitsTable['AeonT2pgen'] = 'UAB1201'
UnitsTable['AeonT3pgen'] = 'UAB1301'
UnitsTable['AeonT3Massfab'] = 'UAB1303'
UnitsTable['UEFT1pd'] = 'UEB2101'
UnitsTable['UEFTML'] = 'UEB2108'
UnitsTable['Triad'] = 'UEB2301'
UnitsTable['UEFT2Arty'] = 'UEF2303'
UnitsTable['Ravager'] = 'XEB2306'
UnitsTable['AeonTML'] = 'UAB2108'
UnitsTable['Oblivion'] = 'UAB2301'
UnitsTable['AeonT2Arty'] = 'UAB2303'
UnitsTable['CybranTML'] = 'URB2108'
UnitsTable['Cerberus'] = 'URB2301'
UnitsTable['CybranT2Arty'] = 'URB2303'
UnitsTable['CybranNuke'] = 'URB2305'
UnitsTable['SeraTML'] = 'XSB2108'
UnitsTable['SeraT2pd'] = 'XSB2301'
UnitsTable['SeraT2Arty'] = 'XSB2303'
UnitsTable['AeonT1AA'] = 'UAB2104'
UnitsTable['UEFT1AA'] = 'UEB2104'
UnitsTable['UEFT1TorpTower'] = '2109'
UnitsTable['UEFFlak'] = 'UEB2204'
UnitsTable['UEFTMD'] = 'UEB4201'
UnitsTable['UEFT2Shield'] = 'UEB4202'
UnitsTable['UEFSAM'] = 'UEB2304'
UnitsTable['UEFT3Shield'] = 'UEB4301'
UnitsTable['AeonTMD'] = 'UAB4201'
UnitsTable['AeonT2Shield'] = 'UAB4202'
UnitsTable['AeonSAM'] = 'UAB2304'
UnitsTable['AeonT3Shield'] = 'UAB4301'
UnitsTable['HARMS'] = 'XRB2308'
UnitsTable['AeonT1Radar'] = 'UAB3101'
UnitsTable['UEFT1Radar'] = 'UEB3101'
UnitsTable['UEFT2Radar'] = 'UEB3201'
UnitsTable['UEFOmni'] = 'UEB3104'
UnitsTable['UEFT2Transport'] = 'UEA0104'
UnitsTable['UEFT3Transport'] = 'XEA0306'
UnitsTable['CZAR'] = 'UAA0310'
UnitsTable['SoulRipper'] = 'URA0401'
UnitsTable['Ahwassa'] = 'XSA0402'
UnitsTable['UEFMechMarine'] = 'UEL0106'
UnitsTable['Striker'] = 'UEL0201'  # UEF t1 tank
UnitsTable['Aurora'] = 'UAL0201'
UnitsTable['Mantis'] = 'URL0107'
UnitsTable['Thaam'] = 'XSL0201'
UnitsTable['Pillar'] = 'UEL0202'
UnitsTable['Obsidian'] = 'UAL0202'
UnitsTable['Rhino'] = 'URL0202'
UnitsTable['Ilsha'] = 'XSL0202'
UnitsTable['Titan'] = 'UEL0303'
UnitsTable['Percival'] = 'XEL0305'
UnitsTable['Percy'] = 'XEL0305'
UnitsTable['Fatboy'] = 'UEL0401'
UnitsTable['Harb'] = 'UAL0303'
UnitsTable['GC'] = 'UAL0401'
UnitsTable['Loyalist'] = 'URL0303'
UnitsTable['Brick'] = 'XRL0305'
UnitsTable['ML'] = 'URL0402'
UnitsTable['Mega'] = 'XRL0403'
UnitsTable['Othuum'] = 'XSL0303'
UnitsTable['Slipper'] = 'XSL0303'
UnitsTable['Chicken'] = 'XSL0401'
UnitsTable['Salem'] = 'URS0201'
UnitsTable['Neptune'] = 'XES0307'
UnitsTable['Atlantis'] = 'UES0401'
UnitsTable['UEFStaging'] = 'UEB5202'
UnitsTable['CivBuilding'] = 'uec1101'
UnitsTable['Wall'] = 'UEB5101'
UnitsTable[''] = ''


class Unit:
    current_id = 1
    id_ = -1
    type = 'uel0202'  # pillar by default, because pillars are awesome
    Position = ['', '', '']
    Orientation = ['', '', '']
    group = "WRECKAGE"

    def __init__(self, type_, pos, rotation_, group_, random1):
        self.id_ = Unit.current_id
        Unit.current_id += 1
        if type_ in UnitsTable:
            self.type = UnitsTable[type_]
        else:
            self.type = type_
        self.Position = pos
        self.Orientation = rotation_
        if random1:
            self.Orientation[1] = str(random.uniform(0, 6.28)) # Random rotation
        self.group = group_

    def toStringList(self, tabs):
        str1 = ["\t" * tabs + "[\'UNIT_" + str(self.id_) + "\'] = {\n"]
        str1 += '\t' * tabs + '\t' + "type = \'" + self.type + "\',\n"
        str1 += '\t' * tabs + '\t' + "orders = '',\n"
        str1 += '\t' * tabs + '\t' + "platoon = '',\n"
        str1 += '\t' * tabs + '\t' + "Position = { " + self.Position[0] + ", " + self.Position[1] + ", " + \
                self.Position[2] + " },\n"
        str1 += '\t' * tabs + '\t' + "Orientation = { " + self.Orientation[0] + ", " + self.Orientation[1] + ", " + \
                self.Orientation[2] + " },\n"
        str1 += '\t' * tabs + "},\n"
        return str1


# MAIN STARTS HERE
if len(sys.argv) < 2:
    error("Usage:" + sys.argv[0] + "<mapname_save.lua>")
if len(sys.argv) >= 3:
    Tabs = int(sys.argv[2])
else:
    Tabs = 0
f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()
MarkersFound = 0
UnitsList = []
for i in range(0, len(lines)):
    marker = re.search("\['Civ\[\w+\]\[\w+\]r? [0-9]*'\] = {", lines[i])  # searches for civ markers
    if marker is not None:
        MarkersFound += 1
        tmp = re.findall("Civ\[\w+\]", lines[i])[0]  # extracting unit type
        Type = tmp[4: len(tmp) - 1]  # extracting unit type
        tmp1 = re.findall("\]\[\w+\]", lines[i])[0] # extracting unit group
        group = tmp1[2: len(tmp1) - 1] # extracting unit group
        tmp2 = re.findall("\]\[\w+\]r?", lines[i])[0] # is rotation random?
        random_ = False
        if tmp2[len(tmp2)-1] is 'r':
            random_ = True
        position = re.findall("[0-9]+(?!\()\.?[0-9]*", lines[i + 5])
        rotation = re.findall("[0-9]+(?!\()\.?[0-9]*", lines[i + 4])
        UnitsList.append(Unit(Type, position, rotation, group, random_))

UnitGroups: Dict[str, List[Unit]] = {}  # grouping units by group names
for unit in UnitsList:
    if unit.group in UnitGroups:
        UnitGroups[unit.group].append(unit)
    else:
        UnitGroups[unit.group] = [unit]

for GroupName, ListOfUnits in UnitGroups.items():
    print('\t'*Tabs + "['" + GroupName + "'] = GROUP {")
    print('\t' * (Tabs+1) + "orders = '',")
    print('\t' * (Tabs+1) + "platoon = '',")
    print('\t' * (Tabs+1) + "Units = {")
    for unit in ListOfUnits:
        print(*unit.toStringList(Tabs+2), sep='')
    print('\t' * (Tabs+1) + "},")
    print('\t' * Tabs + "},")
