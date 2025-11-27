#!/usr/bin/env python3
"""
PDF Toolkit - Comprehensive tool for PDF manipulation
Includes features to remove pages and merge PDF files
"""

from PyPDF2 import PdfReader, PdfWriter
import sys
import os


class PDFToolkit:
    """Class for PDF manipulation operations"""

    @staticmethod
    def remove_pages(input_pdf, output_pdf, pages_to_remove):
        """
        Remove specific pages from a PDF file.

        Args:
            input_pdf (str): Path to the input PDF file
            output_pdf (str): Path to save the output PDF file
            pages_to_remove (list): List of page numbers to remove (1-indexed)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            reader = PdfReader(input_pdf)
            writer = PdfWriter()

            total_pages = len(reader.pages)
            print(f"Total pages in PDF: {total_pages}")
            print(f"Pages to remove: {pages_to_remove}")

            # Convert to 0-indexed and create a set for faster lookup
            pages_to_remove_set = set(page - 1 for page in pages_to_remove)

            # Add all pages except the ones to remove
            pages_kept = 0
            for page_num in range(total_pages):
                if page_num not in pages_to_remove_set:
                    writer.add_page(reader.pages[page_num])
                    pages_kept += 1

            # Write the output PDF
            with open(output_pdf, "wb") as output_file:
                writer.write(output_file)

            print(f"Successfully created {output_pdf}")
            print(f"Pages kept: {pages_kept}")
            print(f"Pages removed: {len(pages_to_remove_set)}")
            return True

        except FileNotFoundError:
            print(f"Error: File '{input_pdf}' not found.")
            return False
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

    @staticmethod
    def merge_pdfs(base_pdf, add_pdf, output_pdf, position="append", page_number=None):
        """
        Merge pages from one PDF to another.

        Args:
            base_pdf (str): Path to the base PDF file
            add_pdf (str): Path to the PDF file to add/merge
            output_pdf (str): Path to save the merged PDF file
            position (str): Where to add pages - 'append', 'prepend', or 'insert'
            page_number (int): Page number for 'insert' position (1-indexed)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            base_reader = PdfReader(base_pdf)
            add_reader = PdfReader(add_pdf)
            writer = PdfWriter()

            total_base_pages = len(base_reader.pages)
            total_add_pages = len(add_reader.pages)

            print(f"Base PDF: {base_pdf} ({total_base_pages} pages)")
            print(f"Add PDF: {add_pdf} ({total_add_pages} pages)")
            print(f"Merge position: {position}")

            if position == "append":
                # Add base pages first, then add pages
                for page in base_reader.pages:
                    writer.add_page(page)
                for page in add_reader.pages:
                    writer.add_page(page)
                print(f"Appended {total_add_pages} pages to end of base PDF")

            elif position == "prepend":
                # Add new pages first, then base pages
                for page in add_reader.pages:
                    writer.add_page(page)
                for page in base_reader.pages:
                    writer.add_page(page)
                print(f"Prepended {total_add_pages} pages to start of base PDF")

            elif position == "insert":
                if page_number is None:
                    raise ValueError("page_number required for 'insert' position")

                insert_pos = page_number - 1  # Convert to 0-indexed

                # Add base pages before insert position
                for i in range(insert_pos):
                    if i < total_base_pages:
                        writer.add_page(base_reader.pages[i])

                # Add new pages
                for page in add_reader.pages:
                    writer.add_page(page)

                # Add remaining base pages
                for i in range(insert_pos, total_base_pages):
                    writer.add_page(base_reader.pages[i])

                print(f"Inserted {total_add_pages} pages at position {page_number}")

            else:
                raise ValueError(
                    f"Invalid position: {position}. Use 'append', 'prepend', or 'insert'"
                )

            # Write the output PDF
            with open(output_pdf, "wb") as output_file:
                writer.write(output_file)

            print(f"\nSuccessfully created {output_pdf}")
            print(f"Total pages in merged PDF: {len(writer.pages)}")
            return True

        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
            return False
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

    @staticmethod
    def merge_multiple(pdf_list, output_pdf):
        """
        Merge multiple PDF files into one.

        Args:
            pdf_list (list): List of PDF file paths to merge
            output_pdf (str): Path to save the merged PDF file

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            writer = PdfWriter()
            total_pages = 0

            print("Merging multiple PDFs:")
            print("-" * 50)

            for pdf_file in pdf_list:
                if not os.path.exists(pdf_file):
                    print(f"Warning: File '{pdf_file}' not found. Skipping...")
                    continue

                reader = PdfReader(pdf_file)
                num_pages = len(reader.pages)

                print(f"Adding {pdf_file} ({num_pages} pages)")

                for page in reader.pages:
                    writer.add_page(page)

                total_pages += num_pages

            # Write the output PDF
            with open(output_pdf, "wb") as output_file:
                writer.write(output_file)

            print("-" * 50)
            print(f"Successfully created {output_pdf}")
            print(f"Total pages: {total_pages}")
            return True

        except Exception as e:
            print(f"Error: {str(e)}")
            return False

    @staticmethod
    def get_pdf_info(pdf_file):
        """
        Get information about a PDF file.

        Args:
            pdf_file (str): Path to the PDF file

        Returns:
            dict: PDF information
        """
        try:
            reader = PdfReader(pdf_file)
            info = {
                "filename": pdf_file,
                "pages": len(reader.pages),
                "metadata": reader.metadata,
            }
            return info
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return None


def print_help():
    """Print help information"""
    help_text = """
PDF Toolkit - Comprehensive PDF Manipulation Tool
================================================

USAGE:
    python pdf_toolkit.py <command> [arguments]

COMMANDS:

1. remove - Remove specific pages from a PDF
   Usage: python pdf_toolkit.py remove <input.pdf> <output.pdf> <pages>
   Example: python pdf_toolkit.py remove document.pdf cleaned.pdf 1,3,5
   
2. append - Add PDF pages to the end of another PDF
   Usage: python pdf_toolkit.py append <base.pdf> <add.pdf> <output.pdf>
   Example: python pdf_toolkit.py append doc1.pdf doc2.pdf merged.pdf
   
3. prepend - Add PDF pages to the beginning of another PDF
   Usage: python pdf_toolkit.py prepend <base.pdf> <add.pdf> <output.pdf>
   Example: python pdf_toolkit.py prepend doc1.pdf doc2.pdf merged.pdf
   
4. insert - Insert PDF pages at a specific position
   Usage: python pdf_toolkit.py insert <base.pdf> <add.pdf> <output.pdf> <position>
   Example: python pdf_toolkit.py insert doc1.pdf doc2.pdf merged.pdf 3
   
5. multiple - Merge multiple PDF files into one
   Usage: python pdf_toolkit.py multiple <output.pdf> <file1.pdf> <file2.pdf> ...
   Example: python pdf_toolkit.py multiple merged.pdf doc1.pdf doc2.pdf doc3.pdf
   
6. info - Get information about a PDF file
   Usage: python pdf_toolkit.py info <input.pdf>
   Example: python pdf_toolkit.py info document.pdf

7. help - Show this help message
   Usage: python pdf_toolkit.py help

EXAMPLES:
    # Remove pages 2, 4, and 6 from a PDF
    python pdf_toolkit.py remove input.pdf output.pdf 2,4,6
    
    # Append two PDFs
    python pdf_toolkit.py append first.pdf second.pdf combined.pdf
    
    # Insert pages at position 5
    python pdf_toolkit.py insert main.pdf insert.pdf result.pdf 5
    
    # Merge multiple PDFs
    python pdf_toolkit.py multiple final.pdf doc1.pdf doc2.pdf doc3.pdf
    """
    print(help_text)


def main():
    """Main function to handle command-line interface"""

    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1].lower()
    toolkit = PDFToolkit()

    try:
        if command == "remove":
            if len(sys.argv) < 5:
                print("Error: Missing arguments for remove command")
                print(
                    "Usage: python pdf_toolkit.py remove <input.pdf> <output.pdf> <pages>"
                )
                sys.exit(1)

            input_pdf = sys.argv[2]
            output_pdf = sys.argv[3]
            pages_to_remove = [int(page.strip()) for page in sys.argv[4].split(",")]

            print("PDF Toolkit - Remove Pages")
            print("=" * 50)
            toolkit.remove_pages(input_pdf, output_pdf, pages_to_remove)

        elif command == "append":
            if len(sys.argv) < 5:
                print("Error: Missing arguments for append command")
                print(
                    "Usage: python pdf_toolkit.py append <base.pdf> <add.pdf> <output.pdf>"
                )
                sys.exit(1)

            base_pdf = sys.argv[2]
            add_pdf = sys.argv[3]
            output_pdf = sys.argv[4]

            print("PDF Toolkit - Append Pages")
            print("=" * 50)
            toolkit.merge_pdfs(base_pdf, add_pdf, output_pdf, position="append")

        elif command == "prepend":
            if len(sys.argv) < 5:
                print("Error: Missing arguments for prepend command")
                print(
                    "Usage: python pdf_toolkit.py prepend <base.pdf> <add.pdf> <output.pdf>"
                )
                sys.exit(1)

            base_pdf = sys.argv[2]
            add_pdf = sys.argv[3]
            output_pdf = sys.argv[4]

            print("PDF Toolkit - Prepend Pages")
            print("=" * 50)
            toolkit.merge_pdfs(base_pdf, add_pdf, output_pdf, position="prepend")

        elif command == "insert":
            if len(sys.argv) < 6:
                print("Error: Missing arguments for insert command")
                print(
                    "Usage: python pdf_toolkit.py insert <base.pdf> <add.pdf> <output.pdf> <position>"
                )
                sys.exit(1)

            base_pdf = sys.argv[2]
            add_pdf = sys.argv[3]
            output_pdf = sys.argv[4]
            position = int(sys.argv[5])

            print("PDF Toolkit - Insert Pages")
            print("=" * 50)
            toolkit.merge_pdfs(
                base_pdf, add_pdf, output_pdf, position="insert", page_number=position
            )

        elif command == "multiple":
            if len(sys.argv) < 4:
                print("Error: Missing arguments for multiple command")
                print(
                    "Usage: python pdf_toolkit.py multiple <output.pdf> <file1.pdf> <file2.pdf> ..."
                )
                sys.exit(1)

            output_pdf = sys.argv[2]
            pdf_files = sys.argv[3:]

            print("PDF Toolkit - Merge Multiple PDFs")
            print("=" * 50)
            toolkit.merge_multiple(pdf_files, output_pdf)

        elif command == "info":
            if len(sys.argv) < 3:
                print("Error: Missing argument for info command")
                print("Usage: python pdf_toolkit.py info <input.pdf>")
                sys.exit(1)

            pdf_file = sys.argv[2]
            info = toolkit.get_pdf_info(pdf_file)

            if info:
                print("PDF Information")
                print("=" * 50)
                print(f"Filename: {info['filename']}")
                print(f"Pages: {info['pages']}")
                if info["metadata"]:
                    print("\nMetadata:")
                    for key, value in info["metadata"].items():
                        print(f"  {key}: {value}")

        elif command == "help":
            print_help()

        else:
            print(f"Error: Unknown command '{command}'")
            print("Use 'python pdf_toolkit.py help' for usage information")
            sys.exit(1)

    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
