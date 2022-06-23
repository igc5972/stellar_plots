##################################################################################
### PURPOSE: Main calling function
##################################################################################

##################################################################################
### PURPOSE: Import Statements
##################################################################################
from matplotlib.backends.backend_pdf import PdfPages
from make_plot.py import plotting
from utils.py import *



def output_figures(input_file, output_save_dir_plus_name):

    '''Main calling function

    Main function that calls other functions to find properties for the list of sources

    Args:
        input_file (str): Points to a list (.txt) with two columns (ra, dec) and 
            1 row per source with 1 header row
        output_save_dir_plus_name(str): The path and name for where the flipbook
            should be saved on user's computer

    Returns:
        None
    '''

    
    pp = PdfPages(save_dir_plus_name) #directory to save output flipbook to

    ras, decs = np.loadtxt(list, unpack = True, skiprows = 1)
    temp, gmag = {function call to Gaia}
    wave, flux = {function call to SDSS}
    ....

    for i in range(len(ras)):
        figure = plotting(args...)
        pp.savefig(figure)

    pp.close()
        
        
        
    
