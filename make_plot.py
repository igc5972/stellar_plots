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
### PLOTTING FUNCTION
##################################################################################
def plotting(wave, flux, teff, lum):
    '''
    Inputs:  wave = wavelengths from sdss spectrum
             flux = fluxes from sdss spectrum
             teff = temperature from sdss
             lum =  luminosity from sdss
    '''

    plt.figure(figsize = (10, 6))
    G = gridspec.GridSpec(5, 2)
    G.update(wspace=0.5, hspace=2.5) #include whitespace around plots

    ax1 = plt.subplot(G[3:,:]) #spectrum
    ax2 = plt.subplot(G[:3,0]) #HRD
    ax3 = plt.subplot(G[:3,1]) #to be determined

    ### Spectrum
    ax1.plot(wave, flux, lw = 2, color = 'k')
    ax1.set_xlabel(r'$\rm{Wavelength \ [\AA]}$', fontsize = 14)
    ax1.set_ylabel(r'$\mathrm{Flux \ [arbitrary units]}$', fontsize = 14)


    ### HR Diagram
    ax2.scatter(teff, lum, color = 'red', marker = 's')
    ax2.set_xlabel(r'$\rm{Label TBD}$', fontsize = 14)
    ax2.set_ylabel(r'$\rm{Label TBD}$', fontsize = 14)


    ### Image?
    ax3.set_xticks([])
    ax3.set_yticks([])



    ### to be determined



    plt.show()




##################################################################################
### TESTING
##################################################################################

#made up data for testing
wave = [1, 2, 3, 4, 5, 6, 7]
flux = [w+3 for w in wave]


plotting(wave, flux, 4, 5)


