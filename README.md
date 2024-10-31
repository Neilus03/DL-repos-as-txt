# DL-repos-as-txt

**Deep Learning Repositories in Text Format** is a collection of full GitHub repositories for deep learning papers, specifically in areas such as computer vision, 3D vision, video processing, and other related topics. The repositories are stored in plain `.txt` format for easy integration with large language models (LLMs). This setup allows you to query and adapt the code directly, ensuring a smooth experience for extracting information and repurposing the implementations without navigating through messy or complex codebases.

### Why This Repository Exists 

In the world of deep learning research, having access to the implementation code for state-of-the-art models is essential. However, repositories are often cluttered with extraneous files and complex structures, making it difficult to interact directly with the code, especially when using LLMs for assistance. This repository solves that by offering full repositories as clean text files.

LLMs can easily process this text format, allowing you to:
- Query specific code snippets or logic.
- Integrate code into your own projects seamlessly.
- Rapidly adapt repositories to suit new research directions or experiments.

### Structure
Each folder in this repo contains:
1. A **README** containing the abstract, main figure, authors and citation of the associated paper.
2. The **complete GitHub repository** in `.txt` format.


### Key Focus Areas:
- Deep Learning
- Computer Vision
- Self-Supervised Learning (SSL)
- 3D Vision
- Video Processing (e.g., VideoMAE, Masked Autoencoders)


## How to Generate `.txt` Repositories Using `repo_to_txt.py`

To convert any GitHub repository into a single `.txt` file that can be fed into LLMs for better context handling, you can use the `repo_to_txt.py` script. This script will traverse through the repository, combine all relevant text-based files, and output them into a single text file.

### Usage Instructions:

1. Clone the desired repository you want to convert into `.txt`.
2. Place the repository folder on your machine.
3. Modify the `repo_folder` path in the `repo_to_txt.py` script to point to the location of your cloned repository.
4. Run ```python repo_to_txt.py``` . It will output a single `.txt` file containing all code and documentation from the repository.

## Contributions
If you find a repository implementation that you'd like to add, feel free to submit a pull request. Please ensure you provide:

- A README with the required contents (see examples within each folder)
- The full GitHub repository in .txt format.
