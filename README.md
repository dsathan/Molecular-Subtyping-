# Molecular-Subtyping-
Classifying Breast Cancer Subtypes Using Deep Embedded Clustering and Hypergraph Partitioning Based on Multi-omics Data

This repository provides some codes for the paper.

The repository can be divided into three parts:
1. Codes for Deep Embedded CLustering.
2. Codes for  omics data integration using hypergraph Partitioning.
3.COdes to mapping obtained clusters to known PAM50 subytpes suing bipartite graphs

## Framework
We take breast cancer classification using multi-omics as example case.

The raw data of breast cancer multi-omics can be download from The Cancer Genome Atlas (TCGA). Here, we just use part of data as example. The workflow of this code is described as follows:

(1) Read corresponding omics data file.<br>
(2) Preprocess data  and feature selection. <br>
(3) Set the hyper-parameters of deep neural network.<br>
(4) Define and train deep neural network and test on test dataset.<br>
(5) Use hypergraph partitioning for ensemble of the multi-omics clusters.<br>
(6) Show the output.

In this study, all the codes in this section are implemented in Python 3.7.
