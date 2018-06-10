# CivMaker
For Supreme Commander FA. Allows civilians placement via blank markers on a map.

It requires python 3.x to work. https://www.python.org/

This script was made to be able to place civilians using ozonex's editor for FAF.

## IN EDITOR

In the editor, place a blank marker and name it using this template:

Civ[UnitName][GroupName]r id

Where UnitName is a name of a unit/building from the table at the beggining of the script (open script via test editor).
GroupName should be either WRECKAGE (for dead units) or INTIAL (for live units) if you're not planning to use adaptive script for current map. If you're using adaptive, this GroupName allows you to use different groups for dynamic civilians spawns. 'id' is a number, doesnt affect outcome. 'r' at the end is optional: it will make unit to be rotated randomly (use it for units wrecks mostly)

If you can't find needed unit inthe table, you use it's 'type' instead, like 'uel0202' for pillar (can be looked up in UnitsDB in FAF)
Current list of avaliable UnitName values:

**EXAMPLE:** Civ[AeonT2pgen][WRECKAGE]r 1
It will place an Aeon t2 power generator on this marker and rotate it randomly.

```
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
UnitsTable['Slipper'] = 'XSL0303' # Sera t3 tank
UnitsTable['Chicken'] = 'XSL0401'
UnitsTable['Salem'] = 'URS0201'
UnitsTable['Neptune'] = 'XES0307'
UnitsTable['Atlantis'] = 'UES0401'
UnitsTable['UEFStaging'] = 'UEB5202'
UnitsTable['CivBuilding'] = 'uec1101'
UnitsTable['Wall'] = 'UEB5101'
```
## HOW TO EXECUTE
For win use run.bat or this cmd command: 
```python CivMaker.py mapname_save.lua TABS > result.txt```
Where TABS is number of tablations you want to be in front of resulting code.
For linux: if you use linux, you can write batch file yourself.

## FINAL
Put resulting code into **mapname_save.lua** ARMY_id brackets, which civilians assigned to (usaully ARMY_17 for 16 players map)
```
['ARMY_17'] = 
        {
            personality = '',
            plans = '',
            color = 0,
            faction = 0,
            Economy = {
                mass = 0,
                energy = 0,
            },
            Alliances = {
            },
            ['Units'] = GROUP {
                orders = '',
                platoon = '',
                Units = {
                    ['INITIAL'] = GROUP {
                        orders = '',
                        platoon = '',
                        Units = {
                        },
                    },
                    **PUT THE RESULT HERE**
                },
            },
            PlatoonBuilders = {
                next_platoon_builder_id = '1',
                Builders = {
                },
            },
        },
```
Use appropriate TABS value to keep formatting good (5 for file generated by ozonex editor)
