
# Rationale for Scientific Articles Analysis with Grobid

## Introduction
This document provides the rationale behind the choices made in the **Scientific Articles Analysis with Grobid** project. It explains the methodology used, validation of results, and justifications for the tools and techniques employed.

## Methodology
### 1. **Data Collection**
- 10 open-access Bitcoin-related articles were selected for analysis.
- Articles were processed using **Grobid**, which extracts structured data from PDFs.

### 2. **Keyword Extraction & Word Cloud Generation**
- **Technique:** Extracted abstracts were tokenized and preprocessed.
- **Tools Used:** `NLTK` and `wordcloud` Python libraries.
- **Validation:** Common Bitcoin-related terms were checked for frequency to ensure meaningful results.
- **Output:** A word cloud image (`wordcloud.png`) visualizing extracted keywords.

### 3. **Figures Count Per Article**
- **Technique:** Figures were identified using Grobid’s full-text extraction.
- **Tools Used:** Grobid's XML parsing with `lxml`.
- **Validation:** Cross-referenced with manual counts from PDFs.
- **Output:** A CSV file (`figures.csv`) listing the number of figures per article.

### 4. **Extracting Links from Articles**
- **Technique:** Extracted hyperlinks from the full text using regular expressions.
- **Tools Used:** `re` module in Python for pattern recognition.
- **Validation:** Checked the validity of extracted URLs using HTTP response codes.
- **Output:** A CSV file (`all_links.csv`) containing extracted links.

## Reproducibility
- **Environment Management:** The use of **Conda** and **Docker** ensures reproducibility.
- **Automation:** CI/CD with GitHub Actions validates dependencies and execution.
- **Documentation:** `README.md` and `ReadTheDocs` provide clear setup and execution steps.
- **Outputs Generated:** The processed results are stored in the `outputs/` directory, including keyword abstracts (`abstracts.txt`), extracted links (`all_links.csv`), figure counts (`figures.csv`), and the generated word cloud (`wordcloud.png`).

## Limitations & Improvements
- **Limitations:**
  - Accuracy of figure extraction depends on Grobid's OCR.
  - Some articles may contain incomplete metadata.
- **Future Enhancements:**
  - Integration with Named Entity Recognition (NER) for better keyword extraction.
  - More robust validation for figure detection using computer vision techniques.
  - Improved filtering for extracted links to remove duplicates and broken URLs.

## Conclusion
This rationale explains the choices behind methodology, validation, and reproducibility. The project adheres to best practices in Open Science, ensuring transparency and usability for future research.
