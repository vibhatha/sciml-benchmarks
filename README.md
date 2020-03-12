![sciml-benchmark-logo](img/logo.png "title-1")

Suite of scientific machine learning benchmarks. This repository contains a 
selection of reference implementations for machine learning problems in 
facilities science. The code in this repository also implements command line 
tools for easily configuring and running the benchmarks.

## Benchmarks


### EM Denoise
Electron microscopy (EM) images of graphene can be used to calculate the
lifetime of the structural defects and how they evolve. However, exposing them
to the EM beam will induce their decay and thus interfere with any conclusions
made. To prevent this samples can be imaged at lower doses, but as the image is
dominated by shot/Poisson noise, making the signal to noise ratio (SNR) lower to
the point where it becomes prohibitive to get any information out of the image.
We wish to reduce the noise present whilst preserving the underlying atomic
structure in the image. 

This benchmark takes simulated images of graphene sheets and adds a noise
distribution that is close to that of the experimental data. As we have
simulated data we have pairs of noisy & clean data which can be used as
input/output pairs for training.

The advantage of machine learning methods comes from the fact noise is poorly
characterised (dead pixels, spatially varying etc.) and traditional approaches
are often task specific (e.g. JPEQ deblocking or AWGN removal), whereas ML will
implicitly learn the noise in the training data without you needing to be able
to assign a value for how severe it is for each image (as you would for say
BM3D).

### DMS Classification

### SLSTR Cloud

## Installation

 - Clone the git repository
 - Install the python package:

```
pip install -e .
```

 - Run the `sciml-bench`:

```
sciml-bench --help
```

## Accessing Data

The `sciml-bench` command provides a method for downloading datasets from the 
remote data store. You can choose to download a single dataset or all of the 
datasets. For example, to download the EM denoise dataset we can run the following:

```
sciml-bench download em_denoise <scarf-user-name> ./data/ 
```

Replace `<scarf-user-name>` with you actual scarf username.

## Running Benchmarks