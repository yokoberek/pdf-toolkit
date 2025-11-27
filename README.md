# PDF Toolkit

A comprehensive tool for PDF file manipulation with Python. This program combines page deletion and PDF merging features in one easy-to-use file.

## 📋 Features

- **Remove Pages**: Delete specific pages from a PDF
- **Append**: Add PDF pages at the end of another document
- **Prepend**: Add PDF pages at the beginning of another document
- **Insert**: Insert PDF pages at a specific position
- **Merge Multiple**: Combine multiple PDF files into one
- **PDF Info**: View PDF file information (page count, metadata)

## 🚀 Installation

### 1. Install uv (Package Manager)

**Linux & macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or install via pip:
```bash
pip install uv
```

### 2. Clone Repository

```bash
git clone https://github.com/yokoberek/pdf-toolkit.git
cd pdf-toolkit
```

### 3. Install Dependencies with uv

```bash
uv sync
```

Or install dependencies directly:
```bash
uv add PyPDF2
```

## 📖 Usage

### General Syntax

```bash
uv run main.py <command> [arguments]
```

---

## 🔧 Commands

### 1. Remove - Delete Pages

Delete specific pages from a PDF.

**Syntax:**
```bash
uv run main.py remove <input.pdf> <output.pdf> <pages>
```

**Examples:**
```bash
# Delete pages 1, 3, and 5
uv run main.py remove document.pdf cleaned.pdf 1,3,5

# Delete page 2 only
uv run main.py remove document.pdf cleaned.pdf 2
```

**Parameters:**
- `input.pdf`: Original PDF file
- `output.pdf`: Output PDF file (without deleted pages)
- `pages`: Page numbers to delete (comma-separated, no spaces)

---

### 2. Append - Add at End

Add PDF pages at the end of another document.

**Syntax:**
```bash
uv run main.py append <base.pdf> <add.pdf> <output.pdf>
```

**Example:**
```bash
uv run main.py append document1.pdf document2.pdf merged.pdf
```

**Parameters:**
- `base.pdf`: Base PDF file
- `add.pdf`: PDF file to be added at the end
- `output.pdf`: Merged PDF output file

---

### 3. Prepend - Add at Beginning

Add PDF pages at the beginning of another document.

**Syntax:**
```bash
uv run main.py prepend <base.pdf> <add.pdf> <output.pdf>
```

**Example:**
```bash
uv run main.py prepend document1.pdf cover.pdf with_cover.pdf
```

**Parameters:**
- The `add.pdf` file will be placed at the beginning before `base.pdf`

---

### 4. Insert - Insert at Specific Position

Insert PDF pages at a specific position.

**Syntax:**
```bash
uv run main.py insert <base.pdf> <add.pdf> <output.pdf> <position>
```

**Example:**
```bash
# Insert at page 3
uv run main.py insert document.pdf insert.pdf result.pdf 3
```

**Parameters:**
- `position`: Page number where the file will be inserted (starting from 1)
- The `add.pdf` file will be inserted before that page

---

### 5. Multiple - Merge Multiple Files

Combine multiple PDF files into one.

**Syntax:**
```bash
uv run main.py multiple <output.pdf> <file1.pdf> <file2.pdf> <file3.pdf> ...
```

**Example:**
```bash
uv run main.py multiple final.pdf doc1.pdf doc2.pdf doc3.pdf doc4.pdf
```

**Parameters:**
- Files will be merged in the order provided
- Can merge 2 or more files

---

### 6. Info - View PDF Information

Display information about a PDF file.

**Syntax:**
```bash
uv run main.py info <input.pdf>
```

**Example:**
```bash
uv run main.py info document.pdf
```

**Output:**
```
PDF Information
==================================================
Filename: document.pdf
Pages: 25

Metadata:
  /Title: My Document
  /Author: John Doe
  /CreationDate: D:20240101120000
```

---

### 7. Help - Get Help

Display help and list of commands.

**Syntax:**
```bash
uv run main.py help
```

---

## 💡 Complete Usage Examples

### Scenario 1: Cleaning a Document
```bash
# Remove blank pages (pages 5, 8, 12)
uv run main.py remove report.pdf clean_report.pdf 5,8,12
```

### Scenario 2: Creating a Complete Report
```bash
# 1. Add cover at the beginning
uv run main.py prepend report_content.pdf cover.pdf temp1.pdf

# 2. Add appendix at the end
uv run main.py append temp1.pdf appendix.pdf temp2.pdf

# 3. Insert table of contents at position 2
uv run main.py insert temp2.pdf table_of_contents.pdf final_report.pdf 2
```

### Scenario 3: Merging Multiple Chapters
```bash
uv run main.py multiple complete_book.pdf \
    cover.pdf \
    preface.pdf \
    chapter1.pdf \
    chapter2.pdf \
    chapter3.pdf \
    conclusion.pdf
```

### Scenario 4: Complex Workflow
```bash
# 1. Check original file info
uv run main.py info original_document.pdf

# 2. Remove unnecessary pages
uv run main.py remove original_document.pdf edited_document.pdf 1,5,10

# 3. Add new pages
uv run main.py append edited_document.pdf new_pages.pdf final_document.pdf
```

---

## 🐍 Usage as Python Module

You can also use this script as a module in your Python code:

```python
from main import PDFToolkit

# Initialize toolkit
toolkit = PDFToolkit()

# Remove pages
toolkit.remove_pages('input.pdf', 'output.pdf', [1, 3, 5])

# Merge PDFs (append)
toolkit.merge_pdfs('doc1.pdf', 'doc2.pdf', 'merged.pdf', position='append')

# Insert PDF
toolkit.merge_pdfs('base.pdf', 'insert.pdf', 'result.pdf', 
                   position='insert', page_number=3)

# Merge multiple files
toolkit.merge_multiple(['file1.pdf', 'file2.pdf', 'file3.pdf'], 'output.pdf')

# View PDF info
info = toolkit.get_pdf_info('document.pdf')
print(f"Total pages: {info['pages']}")
```

---

## 🎯 Tips & Tricks

### 1. Page Numbering
- Pages start from **1** (not 0)
- Page 1 is the first page in the PDF

### 2. Page Number Format for Remove
```bash
# Correct ✓
python main.py remove doc.pdf out.pdf 1,3,5,7

# Wrong ✗
python main.py remove doc.pdf out.pdf 1, 3, 5, 7  # Has spaces
```

### 3. Backup Original Files
Always backup the original PDF file before manipulation:
```bash
cp original_document.pdf original_document_backup.pdf
```

### 4. Check Output Files
Use the `info` command to verify results:
```bash
python main.py info output.pdf
```

### 5. Batch Processing
To process multiple files, create a bash script:
```bash
#!/bin/bash
for file in *.pdf; do
    python main.py remove "$file" "cleaned_$file" 1
done
```

### 6. Using uv run
For an isolated environment, use `uv run`:
```bash
uv run main.py remove document.pdf cleaned.pdf 1,3,5
```

---

## ⚠️ Troubleshooting

### Error: "ModuleNotFoundError: No module named 'PyPDF2'"
**Solution:**
```bash
# With uv
uv add PyPDF2

# Or with regular pip
pip install PyPDF2
```

### Error: "uv: command not found"
**Solution:**
Install uv first:
```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# or via pip
pip install uv
```

### Error: "File not found"
**Solution:**
- Make sure the filename and path are correct
- Use the full path if the file is in another folder
```bash
uv run main.py remove /home/user/docs/file.pdf output.pdf 1
```

### Error: "Permission denied"
**Solution:**
- Make sure the file is not open in another application
- Check file permissions with `ls -l`

### Empty or Error Output PDF
**Possible Causes:**
1. Input PDF is protected/encrypted
2. Page number exceeds total pages
3. PDF is corrupt or damaged

### Error: "git: command not found"
**Solution:**
Install Git first:
```bash
# Ubuntu/Debian
sudo apt install git

# macOS
brew install git

# Windows
# Download from https://git-scm.com/
```

---

## 📝 Important Notes

1. **Encryption**: This script cannot process encrypted/password-protected PDFs
2. **File Size**: For very large PDF files (>100MB), processing may take time
3. **Metadata**: Metadata from the original PDF will be preserved after processing
4. **Format**: The script supports all standard PDF types (v1.3 - v1.7)

---

## 🤝 Contributing

If you find a bug or have suggestions for new features:

1. Fork this repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

---

## 📄 License

This script is based on the [MIT License](./LICENSE) so it's free to use for personal or commercial purposes.

---

## 👨‍💻 Developer

Created to simplify PDF file manipulation in daily workflows.

**Repository:** [https://github.com/yokoberek/pdf-toolkit](https://github.com/yokoberek/pdf-toolkit)

**Requirements:**
- Python 3.8+
- uv (Package Manager)
- PyPDF2

**Version:** 1.0.0

---

## 📚 References

- [uv Documentation](https://docs.astral.sh/uv/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [PDF Specification](https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/PDF32000_2008.pdf)

---

## 🔄 Update Log

### Version 1.0.0 (2024)
- ✅ Remove pages feature
- ✅ Merge feature (append, prepend, insert)
- ✅ Merge multiple files feature
- ✅ PDF info feature
- ✅ Command-line interface
- ✅ Python module support

---

**Happy PDF Processing! 📄✨**