def GDP():
	l = gdp_data.iloc[0,2:]
	sub_value = []
	for i in range(len(l)-2):
    	sub = l[i+1] - l[i]
    	sub_value.append(sub)
	warner.insert(len(warner.columns), "GDP", sub_value, True)
	warner.head()