# PopGen_UNET

First attempt to predict introgression tracts using a UNET architecture. All the files needed are already available and you can skip right to running the code in the ipynb file.  However to recreate first run slim using:

`cd small_sims`
`./make.demo.sims.slim.sh`

This makes 8 files, four ms style with seg sites and four log files introgression tracts for each line. All these files are pop1->pop2 introgression, and I set the migration parameter in Dan's slim code to runif(0.1, 1). So a fair degree of varition in the intensity of introgression. 

Next combine these four sims together, chop everything down to 48x128 and make a npz file to use in training.  This is run as follows:

`gzip *ms *log`
`python3 prep.sims.for.training.UNET.py`

This produces 2 files, one called `training.data.npz` and one called `introg_reg.json`. The latter is needed for this work.

Finally open the `train.small.predict.introg.intensity.ipynb` and run on a GPU.  

Three things about the UNET model in that notebook. First it's a copy from here: https://github.com/zhixuhao/unet/blob/master/model.py. Second I think it may be overkill.  I suspect we could cut down depth and num. of neurons used in diff layers, but haven't experimented. And third, as you can see in my last run, it's unstable. The model seems to often lose it's way and the loss goes in the wrong direction.  That's not encouraging, but could be due to overly large and complex architecture for what we are trying to do. 
