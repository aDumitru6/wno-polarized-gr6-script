# Waves and Optics Polarization Group 06
The file structure will be explained in this README.

* analysis: This folder contains all of the scripts that were used for data analysis.
  * analysis_internal_birefringence.py: this script was used to calculate the internal birefringence of the PMMA block.
  * analysis_one_block.py: this script was used to calculate the stress-induced birefringence for the case of one weight placed on the PMMA block.
  * analysis_two_blocks.py: this script was used to calculate the stress-induced birefringence for the case of two weights placed on the PMMA block.

* data: This folder contains all of the data collected in the project.
  * Lab1: As the name implies, contains all of the data collected in Lab1. Largely useless since better data was collected in future labs.
  * Lab2: Data collected in Lab 2. This data was majorly used in our draft report, and will be used in the final report as well.
  * Lab3: Data collected in Lab 3. This data uses the new technique mentioned in the methods section of our report, specifically continously placing and removing blocks to gather a lot of data in a shorter period of time. (Cycle method: 0 -> 1 -> 2 weights inducing stress on the PMMA block).
  * Tweaking: Something (we, the experimenters would like to thank) Robert Grumeza, Astronomy BSc might need to rename. Contains edited versions of all of the data, patches "holes" in the csvs (i.e makes it so that spots where "" occurs to "0"), to make data analysis easier.
