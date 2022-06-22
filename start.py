##################################################################################
### IMPORT STATEMENTS
##################################################################################
import numpy as np
from matplotlib import pyplot as plt
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.io import fits
from astroquery.sdss import SDSS



##################################################################################
### TEST OBJECT
##################################################################################

#a completely random star I selected
ra =  1087604
dec = 0.71262


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

    #Catch TypeErrors for objects that do not exist in SDSS
    try:
        sp = SDSS.get_spectra(coordinates = crd, radius=2*u.arcsec)[0][1]

        sp_data = sp.data

        sp_flux = sp_data.flux
        sp_lambda = 10**sp_data.loglam #lambda is returned in log space

        return(sp_lambda, sp_flux)

    except(ValueError, RuntimeError, TypeError):
        return(-99, -99)




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
    plt.show()



##################################################################################
### FUNCTION: TEST THE FUNCTIONS
##################################################################################

wave, flux = get_spectrum(test_crd)
plot_spectrum(wave, flux)



