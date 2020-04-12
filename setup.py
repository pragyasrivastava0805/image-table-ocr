import setuptools

long_description = """
Utilities for turning images of tables into CSV data. Uses Tesseract and OpenCV.

Requires binaries for tesseract and pdfimages (from Poppler).
"""
setuptools.setup(
    name="table_ocr",
    version="0.0.1",
    author="Eric Ihli",
    author_email="eihli@owoga.com",
    description="Turn images of tables into CSV data.",
    long_description=long_description,
    long_description_content_type="text/plain",
    url="https://github.com/eihli/image-table-ocr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pytesseract~=0.3",
        "opencv-python~=4.2",
    ],
    python_requires='>=3.6',
)
