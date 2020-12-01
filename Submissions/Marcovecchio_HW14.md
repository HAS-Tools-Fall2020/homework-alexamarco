Alexa Marcovecchio

November 30, 2020

Assignment #14

<<<<<<< Updated upstream
## Grade
3/3 - nice work.

=======
>>>>>>> Stashed changes
#### 1. What is the paper or project you picked? Include a title, a link the the paper and a 1-2 sentence summary of what its about.

Hilton, T., Whelan, M., Zumkehr, A. et al. Peak growing season gross uptake of carbon in North America is largest in the Midwest USA. Nature Clim Change 7, 450–454 (2017). https://doi.org/10.1038/nclimate3272

This paper uses measurements of carbonyl sulfide to estimate the first order uncertainty in climate predictions (GPP). They attempt this on a regional level by limiting their study to the Midwestern United States.

#### 2. What codes and/or data are associated with this paper? Provide any link to the codes and datasets and a 1-2 sentence summary of what was included with the paper (i.e. was it a github repo? A python package? A database? Where was it stored and how.

This article links to five different GitHub repos containing the code and data used to produce this paper.  Looking through these repos was more than a little overwhelming.  The repos contain dozens of python scripts as well as some R and FORTRAN code.  I was not able to find instructions to create an environment included in these repos, but four of the five repos were solely for supplemental functions that were used in multiple projects.  The data files used in this project were not included in any of the repos.

#### 3. Summarize your experience trying to understand the repo: Was their readme helpful? How was their organization? What about documentation within the code itself?

The readme was not helpful in any of the repos. The readme only provides a one sentence explanation of what the repo is for, and possibly a few citations. This left me unsure about what each script's exact purpose was. Some of the scripts were organized into subfolders, but most of them are just unorganized in the main repo.  Documentation within the code is inconsistent between scripts.  Some scripts are very well commented with good docstrings for each function, whereas other scripts contain little if any description.

#### 4. Summarize your experience trying to work with their repo: What happened? Where you successful? Why or why not?

I was not successful with these repos, partially because I was unsure of where to start. There was no information on how to build an environment that would allow me to run these scripts.  Therefore, each time I ran a new script I would have to install several new packages and run into new conflicts.  Also, there was no information about the order in which to run the scripts and very little information within each script regarding its main purpose.

#### 5. Summarize your experience working with the data associated with this research. Could you access the data? Where was it? Did it have a DOI? What format was it in?

The data for this project was not found within the GitHub repo.  However, they do provide links within the paper to the place the data was downloaded.  The paper also notes that you can reach out to the authors to get copies of the data files.  the paper does not provide the DOI for the data, but does reference the scientific paper that describes each dataset. Based on the scripts in the COS_Spatial_Analyses repo, the data is contained in ".cpickle", ".nc", and ".txt" formats.

#### 6. Did this experience teach you anything about your own repo or projects? Things you might start or stop doing?

The main thing I took away from this repo is the importance of documentation.  If I were to upload a repo for paper like this, I now know that I should include in my readme what each file is and a preferred order for running the scripts.  It also reminded me that its important to consistently provide comments and descriptions within my scripts, so an outside viewer could ascertain the purpose of each script fairly easily.
