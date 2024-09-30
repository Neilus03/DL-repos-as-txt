# [VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](https://arxiv.org/abs/2203.12602)

![videomae](https://github.com/user-attachments/assets/855387be-93d4-4511-9482-a911bd2afe8c)


## Abstract:
We propose a pre-training strategy called Multi-modal Multi-task Masked Autoencoders (MultiMAE). It differs from standard Masked Autoencoding in two key aspects: I) it can optionally accept additional modalities of information in the input besides the RGB image (hence "multi-modal"), and II) its training objective accordingly includes predicting multiple outputs besides the RGB image (hence "multi-task").
We make use of masking (across image patches and input modalities) to make training MultiMAE tractable as well as to ensure cross-modality predictive coding is indeed learned by the network. We show this pre-training strategy leads to a flexible, simple, and efficient framework with improved transfer results to downstream tasks. In particular, the same exact pre-trained network can be flexibly used when additional information besides RGB images is available or when no information other than RGB is available - in all configurations yielding competitive to or significantly better results than the baselines. To avoid needing training datasets with multiple modalities and tasks, we train MultiMAE entirely using pseudo labeling, which makes the framework widely applicable to any RGB dataset.
The experiments are performed on multiple transfer tasks (image classification, semantic segmentation, depth estimation) and datasets (ImageNet, ADE20K, Taskonomy, Hypersim, NYUv2). The results show an intriguingly impressive capability by the model in cross-modal/task predictive coding and transfer.
Pre-training video transformers on extra large-scale datasets is generally required to achieve premier performance on relatively small datasets. In this paper, we show that video masked autoencoders (VideoMAE) are data-efficient learners for self-supervised video pre-training (SSVP). We are inspired by the recent ImageMAE and propose customized video tube masking with an extremely high ratio. This simple design makes video reconstruction a more challenging self-supervision task, thus encouraging extracting more effective video representations during this pre-training process. We obtain three important findings on SSVP: (1) An extremely high proportion of masking ratio (i.e., 90% to 95%) still yields favorable performance of VideoMAE. The temporally redundant video content enables a higher masking ratio than that of images. (2) VideoMAE achieves impressive results on very small datasets (i.e., around 3k-4k videos) without using any extra data. (3) VideoMAE shows that data quality is more important than data quantity for SSVP. Domain shift between pre-training and target datasets is an important issue. Notably, our VideoMAE with the vanilla ViT can achieve 87.4% on Kinetics-400, 75.4% on Something-Something V2, 91.3% on UCF101, and 62.6% on HMDB51, without using any extra data. Code is available at [https://github.com/MCG-NJU/VideoMAE](https://github.com/MCG-NJU/VideoMAE)
## Original Repo
[MultiMAE: Multi-modal Multi-task Masked Autoencoders](https://github.com/EPFL-VILAB/MultiMAE)

## Authors
Roman Bachmann, David Mizrahi, Andrei Atanov, Amir Zamir

## Citation
```bash
@misc{bachmann2022multimaemultimodalmultitaskmasked,
      title={MultiMAE: Multi-modal Multi-task Masked Autoencoders}, 
      author={Roman Bachmann and David Mizrahi and Andrei Atanov and Amir Zamir},
      year={2022},
      eprint={2204.01678},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2204.01678}, 
}
```
