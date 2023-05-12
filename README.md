## Alternative dark matter models for GravSphere

To run the alternative dark matter models discussed, you first need to download **GravSphere** and follow its documentation (see https://github.com/justinread/gravsphere).

**!** If you use GravSphere, don't forget to cite the papers mentioned in its repository.

If you use any of the models described here, please additionally cite the following papers:
+ Code implementation -- Constraining SFDM with Antlia B (link)
+ Cold Dark Matter (CDM) -- https://ui.adsabs.harvard.edu/abs/1996ApJ...462..563N/abstract
+ Scalar Field Dark Matter (SFDM) -- https://ui.adsabs.harvard.edu/abs/2021MNRAS.506.2418D/abstract

What you find here only substitutes the dark matter model implemented in GravSphere (coreNFWt), so **you will first need to run ```binulator.py```  in order to run the alternative models implemented here.** See [:: Setting up your own model ::](https://github.com/justinread/gravsphere) section for an explanation of how it works.


## Files

In order to run the alternative models, some changes need to be implemented in the file that contains the priors for the galaxy under analysis:
```
gravsphere_initialise_<name>.py
```
As an example, you can check our file ```gravsphere_initialise_AntliaB.py``` .
( **!** Don't forget to change ```<name>``` to whatever name you are using for your object.)

### Cold Dark Matter

To run the CDM model, the priors that you need are the virial mass $M_{200}$ and the concentration parameter $c_{200}$. The other parameters of the CDM profile are derived from these.
These priors are already defined on the default model, but you can change them according to your galaxy:
```
# M200 in solar masses
logM200low = 7.5
logM200high = 11.5

clow = 1.0
chigh = 50.0
```
After changing your priors, you will need to call your file in the main code,  ```gravsphere_nfw.py```, just like in the original script.

### Scalar Field Dark Matter

To run the SFDM model, the priors that you need are the virial mass $M_{200}$, the concentration parameter $c_{200}$, and the the characteristic length scale of the repulsive self-interaction $R_{\text{TF}}$.
Since the first and second ones are already defined on the default model, you only will need to add the following priors to your file:
```
#rTF in kpc
logrTFlow = np.log10(rTFlow)
logrTFhigh = np.log10(rTFhigh)
```
And you can change the lower (```rTFlow```)  and upper (```rTFhigh```) limit on the $R_\mathrm{TF}$ prior. In this case, we used ```rTFlow = 0.001```  and  ```rTFhigh = 5```. You can see the justification for the choice of each one of these priors on the paper, and choose yours accordingly.

After adding your priors, you will need to call your file in the main code,  ```gravsphere_sfdm.py```, just like in the original script.



## Run the models

You can now run ```python gravsphere_nfw.py``` or ```python gravsphere_sfdm.py```, in both running and plotting mode.

**!** Don't forget to create the folders required by [GravSphere](https://github.com/justinread/gravsphere) to storage the output.

### Note

**!** Even though the code is updated to the most recent version of GravSphere (version 1.5), the results of the paper in question were obtained using version 1.0.

#### Final remarks
If you find any bugs or have any questions, please [contact me](mailto:mpouseirojulio@aip.de).

Mariana P. Júlio
10/05/2023
