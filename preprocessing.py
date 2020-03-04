def preprocess():
	gdp_data = pd.read_csv("../input/gdp-economics/economics.csv")
	pop_data = pd.read_csv("../input/population2/population.csv") #People per sq.km land area
	inf_data = pd.read_csv("../input/inflation-new/inflation.csv")
	u_pop_data = pd.read_excel("../input/population-urban/urb_pop.xls")
	hiv_data = pd.read_excel("../input/hiv-of-population-1549/hiv.xls")# Total % of population aged 15-49
	age_dep_data = pd.read_excel("../input/age-dependency-ratio-of-workingage-population/working_pop.xls") #%of working age population
	senior_data = pd.read_excel("../input/population-ages-65-and-above-total/pop_senior.xls")
	ch_mort_data = pd.read_csv("../input/child-mortality/child_mortality.csv") #Mortality rate, under-5 (per 1,000 live births)
	ru_pop = pd.read_csv("../input/rural-population/rural_pop.csv") #Rural population (% of total population)
	adol_fertility_data = pd.read_csv("../input/adolescent-fertility/adol_fertility.csv")#Adolescent fertility rate (births per 1,000 women ages 15-19)
	gdp_countries = gdp_data.iloc[:,0]
	pop_countries = pop_data.iloc[:,0]
	inf_countries = inf_data.iloc[:,0]
	urban_countries = u_pop_data.iloc[:,0]
	hiv_countries = hiv_data.iloc[:,0]
	working_age_countries = age_dep_data.iloc[:,0]
	senior_countries = senior_data.iloc[:,0]
	ch_mort_countries = ch_mort_data.iloc[:,0]
	ru_pop_countries = ru_pop.iloc[:,0]
	adol_fert_countries = adol_fertility_data.iloc[:,0]
	years = np.arange(1960,2018)
	eco_data = np.asarray(gdp_data)
	#eco_countries = np.asarray(countries)
	years = np.asarray(years)
	gdp = np.zeros((121,58))
	for i in range(0,121):
    	for x in range(2,60):
        	gdp[i,x-2] = eco_data[i,x] 
    countries = []
	rem=[]
	x = 0
	countries = list( set(pop_countries) & set(gdp_countries) & set(inf_countries) & set(urban_countries)  & set(hiv_countries) & set(working_age_countries) & set(senior_countries)  & set(ru_pop_countries) & set(adol_fert_countries)  & set(ch_mort_countries))  #Contains common countries 
	countries_np = np.asarray(countries)
	print(countries_np.shape)
	#print(adol_fert_countries)
	print(countries_np)