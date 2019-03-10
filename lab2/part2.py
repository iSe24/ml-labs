#%%
import numpy as np
import pandas as pd
import pandasql as ps
from timeit import default_timer as timer
#%%
fd = pd.read_csv('C:/jupWork2/data/user_device.csv')
sd = pd.read_csv('C:/jupWork2/data/user_usage.csv')

#%%
fd.head()

#%%
sd.head()

#%%
def example1_pandasql(fd,sd):

    simple_query = '''
        SELECT *
        FROM fd JOIN sd
        WHERE fd.use_id==sd.use_id     
        '''
    return ps.sqldf(simple_query, locals())
#%%
example1_pandasql(fd,sd)
#%%
t1 = timer()
example1_pandasql(fd,sd)
elapsed1 = timer() - t1
t2 = timer()
fsd = fd.merge(sd)
elapsed2 = timer() - t2
print("PandasSQL: {a} \nPandas: {b} ".format(a=elapsed1,b=elapsed2))  

#%%
def example2_pandasql(sd):
    aggr_query = '''
        SELECT distinct
            device, avg(monthly_mb) as avg_mb
        FROM sd 
        GROUP BY device
        '''
    return ps.sqldf(aggr_query, locals())
#%%
example2_pandasql(fsd)
#%%
t1 = timer()
example2_pandasql(fsd)
elapsed1 = timer() - t1
t2 = timer()
fsd.groupby('device').monthly_mb.mean()
elapsed2 = timer() - t2
print("PandasSQL: {a} \nPandas: {b} ".format(a=elapsed1,b=elapsed2))  