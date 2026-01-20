# Waves and Optics Polarization Group 06
The file structure will be explained in this README.

* analysis: This folder contains all of the scripts that were used for data analysis.
  * analysis_internal_birefringence.py: Used to calculate the internal birefringence of the PMMA block.
  * analysis_one_block.py: Used to calculate the stress-induced birefringence for the case of one weight placed on the PMMA block.
  * analysis_two_blocks.py: Used to calculate the stress-induced birefringence for the case of two weights placed on the PMMA block.

* data: This folder contains all of the data collected in the project.
  * Lab1: As the name implies, contains all of the data collected in Lab1. Largely useless since better data was collected in future labs.
  * Lab2: Data collected in Lab 2. This data was majorly used in our draft report, and will be used in the final report as well.
  * Lab3: Data collected in Lab 3. This data uses the new technique mentioned in the methods section of our report, specifically continously placing and removing blocks to gather a lot of data in a shorter period of time. (Cycle method: 0 -> 1 -> 2 weights inducing stress on the PMMA block).
  * Tweaking: Something (we, the experimenters would like to thank ... yk the rest) Robert Grumeza, Astronomy BSc might need to rename. Contains edited versions of all of the data, patches "holes" in the csvs (i.e makes it so that spots where "" occurs to "0"), to make data analysis easier.

* simulations: This folder contains all of the simulation scripts used in the Discussion section of the report.
  * interferometer_simulation.py: Used to validate theories on systematic sinusoidal "drift" found in data by looking into interferometer issues.
  * compression_simulator.py: Used to validate theories on systematic sinusoidal "drift" found in data by looking into PMMA block compression, caused due to the additon of the weights.
  * polarizer_simulation.py: Used to check whether problems potentially caused by imperfect polarizers could lead to issues consistent with systemic errors seen in the data collected.
  * rotation_effects.ipynb: Used to understand if rotation due to placing weights on the PMMA / other reasons could lead to issues consistent with systemic errors seen in the data collected. Plot found in this file was used in the final report.
