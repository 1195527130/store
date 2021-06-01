Friuts = {
	'苹果':12.3,  # 水果和单价
	'草莓':4.5,
    '香蕉':6.3,
    '葡萄':5.8,
    '橘子':6.4,
    '樱桃':15.8
}
info = {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},
        'money': 0
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
        'money': 0
    }
}
for name in info :
    for i in info[name]['fruits'] :
        if i in Friuts :
            info[name]['money'] = info.get(name).get('money') + info.get(name).get('fruits').get(i) * Friuts.get(i)
for i in info :
    print(i,"的账单为",info[i].values())