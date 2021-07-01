<img src="Voicelab/favicon.ico">**VoiceLab**
======
**Automated Reproducible Acoustical Analysis**



## Contributors
David Feinberg, PhD  

Oliver Cook

## Version 
* Version 0.2.Beta.0

## Contact
#### feinberg@mcmaster.ca

Installation instructions:
We recommend setting up a new env in Anaconda or virtualenv with Python 3.8.  We have not tested this with 3.9 yet.
1. <code>conda create -n voicelab python=3.8 -y</code>
2. <code>conda activate voicelab</code>
3. <code>git clone git@github.com:Voice-Lab/VoiceLab.git</code>
4. <code>pip install .</code>
5. <code>python voicelab.py</code>
  
Colab install:
 
```
# Install conda and add channels to look for packages in
import sys
! wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
! chmod +x Anaconda3-2020.02-Linux-x86_64.sh
! bash ./Anaconda3-2020.02-Linux-x86_64.sh -b -f -p /usr/local
sys.path.append('/usr/local/lib/python3.7/site-packages/')
! conda update -n base -c defaults conda -y
! conda config --add channels bioconda
! conda config --add channels conda-forge
```
