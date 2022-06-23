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
from astroquery.vizier import Vizier

'''
todo
- what if the input ra dec aren't in degrees
'''

def read_table(fname):
    '''
    Read in stars from a file if it exists with columns RA & Dec.
    
    Args:
        fname (str): name of file that contains stars to read in.

    Returns:
        ra (array): right ascension (ra) values of input stars.
        dec (array): declination (dec) values of input stars.
    '''

    df = pd.read_csv(fname, names=['ra','dec'])
    return df['ra'].to_numpy(), df['dec'].to_numpy()

def load_gaia(ra, dec, dr=2):
    '''
    Read in Gaia data from Gaia DR2, and returns stellar parameters & Gaia IDs.

    Args:
        ra (float): ra values of input stars.
        dec (float): dec values of input stars.
        dr (int): Gaia data release no. Default is 2.

    Returns:
        gaia_id (int): Gaia Source IDs for all stars.
        teff (float): stellar effective temperature in Kelvin.
        rad (float): stellar radius in solar units.
        lum (float): stellar luminosity in solar units.
    '''

    if dr == 2:
        GAIA_CATALOG='I/345/gaia2'
    elif dr == 3:
        GAIA_CATALOG='I/355/gaiadr3'
    else:
        print('This GAIA version does not exist. Please specify either 2 or 3.')
        sys.exit()

    coord = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
    try:
        cat=Vizier.query_region(coord, catalog=GAIA_CATALOG, radius=1*u.arcsecond)
        cat=cat[0].to_pandas()
        return cat['Source'], cat['Teff'], cat['Rad'], cat['Lum']
    except:
        print('Object with (RA,Dec)=(%s,%s) not found.'%(ra,dec))
        return np.nan, np.nan, np.nan, np.nan

def load_sdss(ra, dec):
    '''
    Read in Gaia data from Gaia DR2.

    Args:
        ra (float): ra of input stars.
        dec (float): dec of input stars.
    
    Returns:
        sdss_ids (array): SDSS ID of input star.
    '''

    SDSS_CATALOG='V/147/sdss12'

    coord = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
    try:
        cat=Vizier.query_region(coord, catalog=SDSS_CATALOG, radius=1*u.arcsecond)
        cat=cat[0].to_pandas().iloc[0]
        sdss_id= cat['SDSS12']
    except:
        print('Object with (RA,Dec)=(%s,%s) not found.'%(ra,dec))
        sdss_id = np.nan
    return sdss_id

##################################################################################
### TEST OBJECT
##################################################################################

#a completely random star I selected
ra  =  10.187604
dec = 0.21871262


#coordinates of star to use for testing
test_crd = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)

##################################################################################
### FUNCTION: OBTAIN SPECTRUM OF OBJECT FROM SDSS
##################################################################################
def get_spectrum(ra, dec):
    '''
    Returns the spectrum of input star from SDSS.

    Args:
        ra (float): ra of input stars.
        dec (float): dec of input stars.
    
    Returns:
        sp_lambda (array): wavelength in SDSS spectrum
        sp_flux (array): flux in SDSS spectrum
    '''

    coord = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)
    sp = SDSS.get_spectra(coordinates = coord, radius=1*u.arcsec)[0][1]

    sp_data = sp.data

    sp_flux = sp_data.flux
    sp_lambda = 10**sp_data.loglam #lambda is returned in log space

    return sp_lambda, sp_flux

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
exit()




