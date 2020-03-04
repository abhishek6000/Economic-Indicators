def inflation():
	l = inf_data.iloc[0,4:].values
	sub_value = []
	for i in range(len(l)-2):
    	sub = l[i+1] - l[i]
    	sub_value.append(sub)
	warner.insert(len(warner.columns), "inflation", sub_value, True)
	warner.head()