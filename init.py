import json

TOWER_NAME = 'wizard'

str100 = '''
|-
| style="background:#00BFFF" rowspan="2" | {} || style="width:20%" | {} || style="width:20%" | {} || style="width:20%" | ${} || style="width:20%" | {}XP
|-
| colspan="4" style="text-align:left;" | （自己填）'''

str5 = '''
|- style="background:#FFD700"
| style="background:#FFA500" rowspan="2" | {} || {} || {} || ${} || {}XP
|- style="background:#FFD700"
| colspan="4" style="text-align:left;" | （自己填）'''

strother = '''
|-
| style="background:#00BFFF" rowspan="2" | {} || {} || {} || ${} || {}XP
|-
| colspan="4" style="text-align:left;" | （自己填）'''

result = ''' class="wikitable mw-collapsible" style="text-align:center;width:100%;background:#90DDFF"
|+
|- style="font-weight:bold;background:#1E90FF"
| style="width:10%" | 等级 || colspan="4" | 等级效果
|-
| style="background:#00BFFF" rowspan=2 | 0<br>(基础) || ${} || 射程32 || 占地6 || 初始解锁
|-
| colspan="4" style="text-align:left;" | （自己填）'''

f = open('jsons/exp.json')
exp = json.load(f)
f.close()
f = open('jsons/price.json')
price = json.load(f)
f.close()
f = open('jsons/name_en.json')
name = json.load(f)
f.close()
f = open('jsons/name_zh.json', encoding='utf-8')
namezh = json.load(f)
f.close()

result = '{|'+result.format(price[TOWER_NAME][0])

for i in range(3):
    result += "\n|-\n| style=\"background:#00BFFF\" colspan=5 | '''路线{}'''".format(
        i+1)
    for j in range(5):
        xp = exp[TOWER_NAME][i][j]
        cost = price[TOWER_NAME][i+1][j]
        enname = name[TOWER_NAME][i][j]
        zhname = namezh[TOWER_NAME][i][j]
        if i == 0 and j == 0:
            result += str100.format(1, zhname, enname, cost, xp)
        elif j == 4:
            result += str5.format(5, zhname, enname, cost, xp)
        else:
            result += strother.format(j+1, zhname, enname, cost, xp)

result += '\n|-\n|}'

f = open('out/'+TOWER_NAME+'.txt', 'w', encoding='utf-8')
f.write(result)
f.close()
