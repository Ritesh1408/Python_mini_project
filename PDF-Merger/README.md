
# PDF Merger

This Python script merges multiple PDF files into a single PDF file using PyPDF2 library.

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/pdf-merger.git
    ```

2. Install the required dependencies:

    ```bash
    pip install PyPDF2
    ```

## Usage

1. Place the PDF files you want to merge into the same directory as the script.

2. Modify the `pdf_files` list in the script to include the filenames of the PDF files you want to merge.

3. Run the script:

    ```bash
    python merge_pdfs.py
    ```

4. Once the script finishes execution, it will create a file named `merged.pdf` containing the merged PDFs.

## Example

Suppose you have three PDF files named `1.pdf`, `2.pdf`, and `item.pdf` that you want to merge. You would modify the `pdf_files` list in the script as follows:

```python
pdf_files = ['1.pdf', '2.pdf', 'item.pdf']
```

After running the script, a file named `merged.pdf` will be created containing the merged contents of `1.pdf`, `2.pdf`, and `item.pdf`.



