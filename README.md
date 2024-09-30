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
- Self-Supervised Learning (SSL)
- 3D Vision
- Video Processing (e.g., VideoMAE, Masked Autoencoders)

## Papers and Repositories (example)

1. **[Masked Autoencoders as Spatiotemporal Learners](https://arxiv.org/abs/2205.09113)**  
   - **Summary**: This paper presents an extension of Masked Autoencoders (MAE) for learning spatiotemporal representations from videos. By randomly masking spacetime patches in videos, the autoencoder is trained to reconstruct the missing information. The method is efficient and achieves competitive results on various video datasets.  
   - **Paper**: [arXiv](https://arxiv.org/pdf/2205.09113)  
   - **Original Repository**: [mae_st](https://github.com/facebookresearch/mae_st) (available in repo.txt)

## How to Generate `.txt` Repositories Using `repo_to_txt.py`

To convert any GitHub repository into a single `.txt` file that can be fed into LLMs for better context handling, you can use the `repo_to_txt.py` script. This script will traverse through the repository, combine all relevant text-based files, and output them into a single text file.

### Usage Instructions:

1. Clone the desired repository you want to convert into `.txt`.
2. Place the repository folder on your machine.
3. Modify the `repo_folder` path in the `repo_to_txt.py` script to point to the location of your cloned repository.
4. Run the `repo_to_txt.py` script. It will output a single `.txt` file containing all code and documentation from the repository.

### Example

```bash
python repo_to_txt.py
```
