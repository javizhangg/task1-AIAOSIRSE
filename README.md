# Project: Scientific Articles Analysis with Grobid

## Description
This project analyzes 10 open-access articles related to Bitcoin using Grobid. It extracts key information and visualizes it in different formats (CSV, PNG). 

The main objectives of this project are:
- **Extract keywords and generate a word cloud** from abstracts.
- **Visualize the number of figures** in each article.
- **List all the links found in each paper.**

## Requirements
To run the project, install the following dependencies:

### Docker
- Install Docker from [Docker official website](https://www.docker.com/)
- Import Grobid into Docker using the command:
```bash
  docker pull grobid/grobid:0.8.1
```
- Once the image is downloaded, you are ready to proceed.

### Conda
- Install Anaconda from [Anaconda official website](https://www.anaconda.com/download)
- Create a new environment using the `environment.yml` file:
```bash
  cd (project-directory)
  conda <environment_name> create -f environment.yml
  ```

### Python
- Install Python from [Python official website](https://www.python.org/downloads/)

Once these dependencies are installed, you are ready to start the project.

## Installation Instructions
1. Clone the repository:
```bash
   git clone https://github.com/javizhangg/task1-AIAOSIRSE.git
   cd task1-AIAOSIRSE
   ```

2. Start Grobid using Docker:
```bash
   docker run --rm --init -p 8070:8070 -p 8071:8071 grobid/grobid:0.8.1
   ```

3. Activate the Conda environment:
```bash
   conda init 
   conda activate <environment_name>
   ```

## Execution Instructions
Run the main script to process the articles:
```bash
python main.py
```

## Automated Testing and CI/CD
This project uses **GitHub Actions** for continuous integration. To manually trigger tests:
```bash
git push origin main
```
CI/CD workflows validate the installation and execution of tests.

## Preferred Citation
If you use this work, please cite it as:
```bibtex
@misc{ScientificArticlesAnalysis,
    title = {Scientific Articles Analysis with Grobid},
    howpublished = {\url{https://github.com/javizhangg/task1-AIAOSIRSE}},
    autor = {Zhiwei Zhang},
    publisher = {GitHub},
    year = {2025},
}
```
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14905817.svg)](https://doi.org/10.5281/zenodo.14905817)

## License
This project is licensed under the [Apache License 2.0](LICENSE).

## Where to Get Help
For questions or issues, please use the forum or contact:
- **Author:** Zhiwei Zhang
- **Email:** Zhiwei.zha@alumnos.upm.es
- **GitHub:** [https://github.com/user](https://github.com/javizhangg)

## Acknowledgments
This project follows the best practices taught in the Open Science and AI course by Daniel Garijo, including reproducibility, metadata structuring, and documentation standards【43 source】【44 source】.

## 📄 Structured Metadata
This project includes metadata in [CodeMeta](https://codemeta.github.io/) format for easier discovery and reuse.

📌 The `codemeta.json` file can be found in the repository root:
🔗 [codemeta.json](https://github.com/javizhangg/task1-AIAOSIRSE/blob/main/codemeta.json)


