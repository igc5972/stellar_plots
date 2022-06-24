.. _installation:

Using Stellar Plots
====================


Two pieces of input:
First is the path to a  comma separated value (.csv) file with two columns, no header and one row for each object. 
The first column corresponds to the object's right ascension (RA; degrees).
The second column corresponds to the object's declination (DEC; degrees).

The second input is the path to a PDF file (that does not exist yet) where the output should be saved.


The first input should look like: ```'/path/to/list/of/coordinates.csv'```
The second input should look like: ```'/path/to/output/pdftosave.pdf'```


## Running the code from Python:


.. code-block:: python

	from stellar_plots.driver import output_figures as main
	main('/path/to/list/of/coordinates.csv', '/path/to/output/pdftosave.pdf')
	
	

## Running the code from Terminal (bash):

.. code-block:: bash
	
	$ python -m stellar_plots.driver '/path/to/list/of/coordinates.csv' '/path/to/output/pdftosave.pdf'
