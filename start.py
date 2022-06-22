##################################################################################
### IMPORT STATEMENTS
##################################################################################
import numpy as np
from matplotlib import pyplot as plt
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.io import fits
from astroquery.sdss import SDSS
from astroquery.gaia import Gaia
# Gaia.MAIN_GAIA_TABLE = "gaiadr2.gaia_source"  # Reselect Data Release 2, default
ra =  10.187604
dec = 0.21871262
test_crd = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)

query1 = """SELECT 
TOP 10
source_id, ra, dec, parallax 
FROM gaiadr2.gaia_source
"""
# radius = u.Quantity(1.0, u.deg)
# j = Gaia.cone_search_async(test_crd, radius)
# r = j.get_results()

job = Gaia.launch_job_async("select top 100 designation,ra,dec "
                            "from gaiadr2.gaia_source order by source_id")

GaiaDR2SourceID = str(4769316162914833408)

query = "SELECT TOP 1 source_id, ra, dec FROM gaiadr2.gaia_source WHERE ra = %s, dec = %s" % (ra,dec)
query = "SELECT TOP 1 source_id, ra, dec FROM gaiadr2.gaia_source WHERE source_id = " + str(5889388490662572288)#+ str(1635721458409799680)

print(query)
job = Gaia.launch_job(query)
results = job.get_results()

print(results)
exit()
'''
from astroquery.gaia import Gaia
>>>
job = Gaia.launch_job("select top 100 "
                      "solution_id,ref_epoch,ra_dec_corr,astrometric_n_obs_al, "
                      "matched_observations,duplicated_source,phot_variable_flag "
                      "from gaiadr2.gaia_source order by source_id")
r = job.get_results()
print(r['ra_dec_corr'])
 ra_dec_corr
 '''


''' 
grab spectrum from SDSS and plot
use SQL to get teff, radius of star and make HRDiagram
use SQL to get stellar parameters from Gaia
sample of 100 stars
error handling if source is not in Gaia, or not in SDSS


1. HR diagram
2. spectrum
3.


workflow :
- input N stars' ra/dec
- use SDSS to get their

'''

def get_params(N=1):
    f = open('query.txt','r')
    query = f.read()
    print(query)
    res   = SDSS.query_sql(query)
    print(res)
    exit()
    return res['teff'].data, res['logg'].data
    
##################################################################################
### TEST OBJECT
##################################################################################

#a completely random star I selected
ra =  10.187604
dec = 0.21871262


#coordinates of star to use for testing
test_crd = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)

##################################################################################
### FUNCTION: OBTAIN SPECTRUM OF OBJECT FROM SDSS
##################################################################################
def get_spectrum(crd):
    '''
    Input:    An astropy SkyCoord object for the desired target
    Returns:  The wavelength and flux of the SDSS spectrum
    '''

    sp = SDSS.get_spectra(coordinates = crd, radius=2*u.arcsec)[0][1]

    sp_data = sp.data

    sp_flux = sp_data.flux
    sp_lambda = 10**sp_data.loglam #lambda is returned in log space

    return(sp_lambda, sp_flux)




##################################################################################
### FUNCTION: PLOT THE SPECTRUM
##################################################################################

def plot_spectrum(wave, flux):
    '''
    Inputs:  Two lists, one for the wavelength and one for the fluxes in the spectrum
    Returns: Nothing, outputs a plot for visualization
    '''
    fig, ax = plt.subplots(figsize = (10, 5))
    ax.plot(wave, flux, lw = 2, color = 'k')
    ax.set_xlabel(r'$\rm{Wavelength \ [\AA]}$', fontsize = 14)
    ax.set_ylabel(r'$\mathrm{Flux \ [arbitrary units]}$', fontsize = 14)
    return ax

##################################################################################
### FUNCTION: PLOT HR DIAGRAM
##################################################################################

def plot_hrd(teff, logg):
    '''
    Inputs:  Two lists, one for the effective temperature and one for the radius
    Returns: Nothing, outputs a plot for visualization
    '''
    fig, ax = plt.subplots(figsize = (10, 5))
    logg = logg[teff>=0]
    teff = teff[teff>=0]
    ax.scatter(teff, logg, color = 'grey')
    plt.gca().invert_xaxis()
    ax.set_xlabel(r'$\rm{T_\mathrm{eff} \ [K]}$', fontsize = 14)
    ax.set_ylabel(r'$\mathrm{Log(g) \ [dex]}$', fontsize = 14)
    return ax

##################################################################################
### FUNCTION: TEST THE FUNCTIONS
##################################################################################

wave, flux = get_spectrum(test_crd)
teff, logg = get_params()
ax1 = plot_hrd(teff,logg)
plt.show()
ax2 = plot_spectrum(wave, flux)
query_object_catalogs('', 'Gaia DR1 TGA')
exit()




