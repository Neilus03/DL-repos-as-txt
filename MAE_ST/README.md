# [Masked Autoencoders As Spatiotemporal Learners](https://arxiv.org/abs/2205.09113)



![teaser](https://github.com/user-attachments/assets/1a755f73-9e39-429e-90fa-2486e35e1f10)


## Abstract:
This paper studies a conceptually simple extension of Masked Autoencoders (MAE) to spatiotemporal representation learning from videos. We randomly mask out spacetime patches in videos and learn an autoencoder to reconstruct them in pixels. Interestingly, we show that our MAE method can learn strong representations with almost no inductive bias on spacetime (only except for patch and positional embeddings), and spacetime-agnostic random masking performs the best. We observe that the optimal masking ratio is as high as 90% (vs. 75% on images), supporting the hypothesis that this ratio is related to information redundancy of the data. A high masking ratio leads to a large speedup, e.g., > 4x in wall-clock time or even more. We report competitive results on several challenging video datasets using vanilla Vision Transformers. We observe that MAE can outperform supervised pre-training by large margins. We further report encouraging results of training on real-world, uncurated Instagram data. Our study suggests that the general framework of masked autoencoding (BERT, MAE, etc.) can be a unified methodology for representation learning with minimal domain knowledge.
## Original Repo
[MultiMAE: Multi-modal Multi-task Masked Autoencoders](https://github.com/EPFL-VILAB/MultiMAE)

## Authors
Christoph Feichtenhofer, Haoqi Fan, Yanghao Li, Kaiming He

## Citation
```bash
@misc{feichtenhofer2022maskedautoencodersspatiotemporallearners,
      title={Masked Autoencoders As Spatiotemporal Learners}, 
      author={Christoph Feichtenhofer and Haoqi Fan and Yanghao Li and Kaiming He},
      year={2022},
      eprint={2205.09113},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2205.09113}, 
}
```
