import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.io import fits
from astroquery.sdss import SDSS
from astroquery.gaia import Gaia
def func1():
    f = open('../query.txt','r')
    query = f.read()
    print(query)
    res   = SDSS.query_sql(query)

def func2():
    gaia_query="SELECT dr2.source_id, dr2.phot_g_mean_mag, dr3.* \
    FROM gaiadr2.gaia_source AS dr2 \
    JOIN gaiadr3.dr2_neighbourhood AS dr3 ON \
    dr2.source_id = dr3.dr2_source_id \
    WHERE dr2.phot_g_mean_mag < 5 \
    ORDER BY dr2.source_id ASC"

    N=10000
    job = Gaia.launch_job_async("select top %s designation,ra,dec "
                                "from gaiadr2.gaia_source order by source_id"%N)
    res = job.get_results().to_pandas()
    #res.to_csv('gaia_stars.csv',index=False)

def func3():
    df=pd.read_csv('/Users/maryumsayeed/Downloads/MAST_Crossmatch_TIC.csv',delimiter=',',skiprows=4)
    df=df[df['ALLWISE']==df['ALLWISE']] 
    df=df[df['SDSS']==df['SDSS']] 

    df=df[df['ALLWISE']==df['ALLWISE']] 
    df1=df[['DESIGNATION','ra','dec','SDSS','GAIA','MatchID','ALLWISE']]
    df2=df[['ra','dec']]
    df1.to_csv('gaia_sdss_tic.csv',index=False)
    df2.to_csv('sample.csv',index=False)
    
def func4():
    df=pd.read_csv('/Users/maryumsayeed/Downloads/asu.tsv',skiprows=29)
    df.to_csv('ksample.txt',index=False)
    print(df)
func4()