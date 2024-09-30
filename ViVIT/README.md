# [ViViT: A Video Vision Transformer](https://arxiv.org/abs/2103.15691)

![vivit](https://github.com/user-attachments/assets/bbd9ab3a-6b65-4929-a509-8a67d38901de)



## Abstract:
We present pure-transformer based models for video classification, drawing upon the recent success of such models in image classification. Our model extracts spatio-temporal tokens from the input video, which are then encoded by a series of transformer layers. In order to handle the long sequences of tokens encountered in video, we propose several, efficient variants of our model which factorise the spatial- and temporal-dimensions of the input. Although transformer-based models are known to only be effective when large training datasets are available, we show how we can effectively regularise the model during training and leverage pretrained image models to be able to train on comparatively small datasets. We conduct thorough ablation studies, and achieve state-of-the-art results on multiple video classification benchmarks including Kinetics 400 and 600, Epic Kitchens, Something-Something v2 and Moments in Time, outperforming prior methods based on deep 3D convolutional networks. To facilitate further research, we release code at [github.com/google-research/scenic/tree/main/scenic/projects/vivit](https://github.com/google-research/scenic/tree/main/scenic/projects/vivit)

## Original Repo
[ViViT: A Video Vision Transformer](https://github.com/google-research/scenic/tree/main/scenic/projects/vivit)

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
