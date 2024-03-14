#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


### Define time array.
Tsam = 0.1              #.. sampling interval
Tmax = 12.0             #.. end time of series 
Nt = int(Tmax/Tsam)+1   #.. nominal length

### Construct time array t with three gaps.
Nt12 = int(Nt/12)
t = np.array([])
for k in [0,4,8]:
    igap = np.random.randint((k+1)*Nt12,(k+3)*Nt12)
    print('Constructed gap time : {:.1f}'.format(Tsam*igap))
    t = np.concatenate([t,np.arange(k*Nt12,igap),np.arange(igap+1,(k+4)*Nt12)])
t = t*Tsam
print()
### Compute the array of differences dt.
dt = t[1:] - t[:-1]
### Create a boolean mask igaps with indices where dt is at least 50% larger than Tsam.
igaps = dt > 1.5*Tsam
### Create the array t_before_gaps listing the times immediately before the gaps.
t_before_gaps = np.array([0.0,0.0,0.0])
i = 0
for k in range(len(igaps)):
    if igaps[k] == True:
        t_before_gaps[i] = t[k]
        i += 1
### Add Tsam to t_before_gaps to obtain the array t_gaps with the proper gap times.
t_gaps = t_before_gaps + Tsam
### Print the detected gap times in the same format as the constructed gap times.
for k in range(3):
    print('Detected gap time : {:.1f}'.format(t_gaps[k]))

