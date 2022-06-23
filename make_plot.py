##################################################################################
### PURPOSE: Plot the actual output for each source
##################################################################################



##################################################################################
### IMPORT STATEMENTS
##################################################################################
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec





##################################################################################
### CENTERING AXES
##################################################################################


##################################################################################
### PLOTTING FUNCTION
##################################################################################
def plotting(wave, flux, teff, lum, ra, dec, z):
    '''Plotting

    Make a figure with subplots for each of the data products pulled

    Args: 
        wave  (arr):   Numpy array. The wavelength values for the spectrum from SDSS.
        flux  (arr):   Numpy array. The flux values for the spectrum with SDSS.
        teff (float):  Float. The effective temperature from Gaia.
        lum  (float):  Float. The luminosity from Gaia. 
        ra   (float):  Float. Right Ascension of target.
        dec  (float):  Float. Declination of target.
        z    (float):  Float. Redshift of source.

    Returns:
        None. 
    '''

    plt.figure(figsize = (10, 8))
    G = gridspec.GridSpec(20, 4)
    G.update(wspace=0.5, hspace=2.5) #include whitespace around plots

    ax1 = plt.subplot(G[12:,:]) #spectrum
    ax2 = plt.subplot(G[:10,0:2]) #HRD
    ax3 = plt.subplot(G[:10,2:4]) #to be determined



    ### Spectrum
    ax1.set_xlabel(r'$\rm{Wavelength \ [\AA]}$', fontsize = 14)
    ax1.set_ylabel(r'$\mathrm{Flux \ [arbitrary units]}$', fontsize = 14)
    if not isinstance(wave, (np.ndarray, list, set,) ): #handle case of no available data
        ax1.set_ylim(0, 10)
        ax1.set_xlim(0, 100)
        ax1.annotate('No Spectrum Data Available', (25, 4), xytext = (25, 4), fontsize = 20)
    else:
        ax1.plot(wave, flux, lw = 2, color = 'k')



    ### HR Diagram 
    ax2.set_xlabel(r'$\rm{Effective Temperature}$', fontsize = 14)
    ax2.set_ylabel(r'$\rm{Luminosity}$', fontsize = 14)
    if not teff < 0 or lum < 0: #handle case of no available data
        ax2.set_ylim(0, 10)
        ax2.set_xlim(0, 100)
        ax2.annotate('No HR Data Available', (3, 5), xytext = (3, 5), fontsize = 20)
    else:
        ax2.scatter(teff, lum, color = 'red', marker = 's')
    


    ### Image?
    ax3.set_xticks([])
    ax3.set_yticks([])
    ax3.set_ylim(0, 100)
    ax3.set_xlim(0, 100)
    ax3.annotate("Ra:  " + str(ra), (2, 90), xytext = (2, 90), fontsize = 14, color = 'k')
    ax3.annotate("Dec: " + str(dec), (2, 80), xytext = (2, 80), fontsize = 14, color = 'k')
    ax3.annotate("z:     " + str(z), (2, 70), xytext = (2, 70), fontsize = 14, color = 'k')
    





    ### to be determined



    plt.show()




##################################################################################
### TESTING
##################################################################################

#made up data for testing
wave = -99
flux = -99
ra = 1.12312
dec = 123.32132

plotting(wave, flux, 4, 5, ra, dec, 1.3)

