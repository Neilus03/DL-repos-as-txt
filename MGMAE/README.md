# [MGMAE: Motion Guided Masking for Video Masked Autoencoding](https://arxiv.org/abs/2308.10794)



![image](https://github.com/user-attachments/assets/1f14bc14-e4ac-473c-b995-925ddb6b97af)

## Abstract:
Masked autoencoding has shown excellent performance on self-supervised video representation learning. Temporal redundancy has led to a high masking ratio and customized masking strategy in VideoMAE. In this paper, we aim to further improve the performance of video masked autoencoding by introducing a motion guided masking strategy. Our key insight is that motion is a general and unique prior in video, which should be taken into account during masked pre-training. Our motion guided masking explicitly incorporates motion information to build temporal consistent masking volume. Based on this masking volume, we can track the unmasked tokens in time and sample a set of temporal consistent cubes from videos. These temporal aligned unmasked tokens will further relieve the information leakage issue in time and encourage the MGMAE to learn more useful structure information. We implement our MGMAE with an online efficient optical flow estimator and backward masking map warping strategy. We perform experiments on the datasets of Something-Something V2 and Kinetics-400, demonstrating the superior performance of our MGMAE to the original VideoMAE. In addition, we provide the visualization analysis to illustrate that our MGMAE can sample temporal consistent cubes in a motion-adaptive manner for more effective video pre-training.

## Original Repo
[[ICCV 2023] Official Implementation of MGMAE](https://github.com/MCG-NJU/MGMAE)

## Authors
Bingkun Huang, Zhiyu Zhao, Guozhen Zhang, Yu Qiao, Limin Wang

## Citation
```bash
@misc{huang2023mgmaemotionguidedmasking,
      title={MGMAE: Motion Guided Masking for Video Masked Autoencoding}, 
      author={Bingkun Huang and Zhiyu Zhao and Guozhen Zhang and Yu Qiao and Limin Wang},
      year={2023},
      eprint={2308.10794},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2308.10794}, 
}
```
