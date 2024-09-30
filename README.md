# full-repos-in-txt

**Full Repositories in Text Format** is a collection of full GitHub repositories for deep learning papers, specifically in areas such as computer vision, 3D vision, video processing, and other related topics. The repositories are stored in plain `.txt` format for easy integration with large language models (LLMs). This setup allows you to query and adapt the code directly, ensuring a smooth experience for extracting information and repurposing the implementations without navigating through messy or complex codebases.

## Why This Repository Exists

In the world of deep learning research, having access to the implementation code for state-of-the-art models is essential. However, repositories are often cluttered with extraneous files and complex structures, making it difficult to interact directly with the code, especially when using LLMs for assistance. This repository solves that by offering full repositories as clean text files. 

LLMs can easily process this text format, allowing you to:
- Query specific code snippets or logic.
- Integrate code into your own projects seamlessly.
- Rapidly adapt repositories to suit new research directions or experiments.

Each repository is accompanied by:
1. A **brief summary** of the associated paper.
2. The **original paper** in PDF format.
3. The **complete GitHub repository** in `.txt` format.

## Example Structure

paper-1/
- summary.txt (a brief explanation of the paper)
- paper.pdf (the original research paper)
- repo.txt (the full GitHub repo as a .txt file)

paper-2/
- summary.txt
- paper.pdf
- repo.txt

### Key Focus Areas:
- Deep Learning
- Computer Vision
- Self Supervised Learning (SSL)
- 3D Vision
- Video Processing (e.g., VideoMAE, Masked Autoencoders)

## Papers and Repositories (example)

1. **[Masked Autoencoders as Spatiotemporal Learners](https://arxiv.org/abs/2205.09113)**  
   - **Summary**: This paper presents an extension of Masked Autoencoders (MAE) for learning spatiotemporal representations from videos. By randomly masking spacetime patches in videos, the autoencoder is trained to reconstruct the missing information. The method is efficient and achieves competitive results on various video datasets.  
   - **Paper**: [arXiv](https://arxiv.org/pdf/2205.09113)  
   - **Original Repository**: [mae_st](https://github.com/facebookresearch/mae_st) (available in repo.txt)


## How to Use

Each repository is provided in `.txt` format for easy parsing and integration. You can either:
- Download the entire folder containing the paper, summary, and repository.
- Directly copy relevant code segments from the `.txt` files for use in your own projects.

### Future Enhancements
- **Folder Segmentation**: Over time, as more repositories are added, they will be segmented by research topics (e.g., 3D vision, video processing).
- **Additional Annotations**: Future versions of this repo may include code annotations and example usage to help you better understand key functions.

## Contributions
If you find a repository implementation that you'd like to add, feel free to submit a pull request. Please ensure you provide:
1. A brief summary of the paper.
2. The original PDF of the paper (or a link to it).
3. The full GitHub repository in `.txt` format.

