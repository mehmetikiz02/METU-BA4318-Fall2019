import pandas as pd

def get_brazil():
    return pd.read_csv("sudeste.csv",skipinitialspace=True,usecols=["temp","date"])
     
def get_madrid():
    return pd.read_csv("weather_madrid_LEMD_1997_2015.csv",skipinitialspace=True,usecols=["Mean TemperatureC","CET"])

def brazil_group_by(brazil):
    return brazil.groupby("date",as_index=False).mean()

def merge_madrid_brazil(madrid,brazil):
    return madrid.merge(brazil,how='inner',on=["date"])
def transform(brazil,madrid):
    madrid.rename(columns={"CET":"date","Mean TemperatureC":"temp-madrid"},inplace=True)
    brazil = brazil_group_by(brazil)
    final = merge_madrid_brazil(madrid,brazil)
    final.rename(columns = {"temp":"temp-brazil"})
    return final
def correlate(final):
    return final.corr(method='pearson')
def print_final(final):
    final = correlate(final)
    print("Correlation")
    print(final)

final = transform(get_brazil(),get_madrid())
print_final(final)

#Interpretations of the Results#
#Correlation coefficient is -0.030652. Correlation coefficients whose
#magnitude are less than 0.3 have little if any (linear)
#correlation. Since this is negative more than -0,3, there is a
#little negative correlation between Madrid and Brazil. 
#Since it is weak correlated, when tempraature of madric increases,
#there would be a little decrease in the Temprature of
#Brazil.Although, we can see that when Madrid's tempature increases,
#there is no tendency for the Brazil's tempature to
#change in a specific way. That is the result of weak negative
#linear relationship which is almost zero.
#ba4318-test1-part2#
#Mehmet IKIZ#
#2258978#
