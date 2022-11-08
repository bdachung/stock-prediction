import vnquant.data as dt
list_companies = ['VCB','AGR']

for company in list_companies:
    loader = dt.DataLoader(company, '2004-01-01','2022-11-01')
    data = loader.download()
    data.to_csv(company+'.csv')