province = ["北京","上海","广东"]
province.append("石家庄")
province.append("太原")
province.append("呼和浩特")
province.append("沈阳")
province.append("长春")
province.append("哈尔滨")
province.append("南京")
province.append("杭州")
province.append("合肥")
province.append("福州")
province.append("南昌")
province.append("济南")
province.append("郑州")
province.append("武汉")
province.append("长沙")
province.append("广州")
province.append("南宁")
province.append("海口")
province.append("成都")
province.append("贵阳")
province.append("昆明")
province.append("拉萨")
province.append("西安")
province.append("兰州")
province.append("西宁")
province.append("银川")
province.append("乌鲁木齐")
province.append("台北")
a = province[1]
province[1] = province[2]
province[2] = a
print(province)

GDP = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
print("前八城市的GDP总和为：",round(sum(GDP),2))
print("前八城市的平均GDP为：",round(sum(GDP)/8,2))


