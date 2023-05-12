import numpy as np
from constants import *
from functions_sfdm import * 
from functions_nfw import * 

# Number of CPU(s) that you have available (to run multiple processes at the same time)
nprocs = 12

#This file contains all the code options and choices for 
#running a given model. Throughout, -1 means auto-calculate.

#Data files and output base filename:
whichgal = 'AntliaB'
infile = output_base+whichgal+'/'+whichgal
outdirbase = output_base+whichgal+'/'

#Plot ranges and sample points [-1 means auto-calculate]:
rplot_inner = 1e-3
rplot_outer = 10.0
rplot_pnts = 100
y_sigLOSmax = 15
ymin_Sigstar = 1e-4
ymax_Sigstar = 100
yMlow = 1e4
yMhigh = 1e10
yrholow = 1e5
yrhohigh = 1e11
alp3sig = 0.0
sigmlow = 1e-3
sigmhigh = 5.0

#Code options:
propermotion = 'no'
virialshape = 'yes'

#Overplot true solution (for mock data). If 
#yes, then the true solutions should be passed
#in: ranal,betatrue(ranal),betatruestar(ranal),
#truemass(ranal),trueden(ranal),truedlnrhodlnr(ranal).
overtrue = 'no'

#Radial grid range for Jeans calculation:
rmin = -1.0
rmax = -1.0

#Galaxy properties. Assume here that the baryonic mass
#has the same radial profile as the tracer stars. If this
#is not the case, you should set Mstar_rad and Mstar_prof 
#here. The variables barrad_min, barrad_max and bar_pnts 
#set the radial range and sampling of the baryonic mass model.
Mstar = 8e5
Mstar_err = Mstar * 0.25
baryonmass_follows_tracer = 'yes'
barrad_min = 0.0
barrad_max = 10.0
bar_pnts = 250


###########################################################
#Priors

#For surface density fit tracertol = [0,1] sets the spread 
#around the best-fit value from the binulator.
tracertol = 0.1

#Velocity anisotropy priors:
betr0min = -0.9
betr0max = 0.0
betnmin = 1.0
betnmax = 3.0
bet0min = -1.0
bet0max = 1.0
betinfmin = -1.0
betinfmax = 1.0

# NFW + SFDM priors:
logM200low = 7.5
logM200high = 11.5
clow = 1.0
chigh = 50.0

# SFDM priors
rTFlow = 0.001
rTFhigh = 5.
logrTFlow = np.log10(rTFlow)
logrTFhigh = np.log10(rTFhigh)

#Priors on central dark mass [set logMcenlow/high very negative
#to switch this off. Mcen is the mass in Msun; acen is the
#scale length in kpc, usually assumed smaller than Rhalf
#to avoid degeneracies with the stellar mass]:
logMcenlow = -4
logMcenhigh = -3
acenlow = 1e-5
acenhigh = 1e-2

#Priors on rotation [Arot defined as:
#vphimean^2 / (2 sigr^2) = Arot(r/Rhalf) which yields linear
#rotation with radius. (Arot = 0.5 means an equal balance of
#rotation and pressure support at Rhalf.)]:
Arotlow = 0.0
Arothigh = 1.0e-12

#Priors on distance [True distance follows as:
#dgal_kpc * drange s.t. we usually want drangelow < 1.0 and
#drangehigh > 1.0]:
dgal_kpc = 1.35e3
drangelow = 0.99999
drangehigh = 1.00001

###########################################################
#Post processing options:

#For calculating D+J-factors:
calc_Jfac = 'no'
alpha_Jfac_deg = 0.5 
calc_Dfac = 'no'
alpha_Dfac_deg = 0.5
