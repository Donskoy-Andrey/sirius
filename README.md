# Description:
The «Gazprom Neft» Group has a portal "Knowledge Dissemination System", where every employee of the company can share useful materials (books, articles, lessons learned, etc.). 

When adding materials, employees need to fill a number of fields in the material card. This procedure requires a lot of time. Therefore, it is proposed to save staff time and optimize the business process by partially automating this task. It is necessary that when adding a material the system "scanned the document" and determine the keywords in it.

# Problem:
1. Reduce employee time to fill out a document card to be uploaded to the "Knowledge Library";

2. Unify tags to documents in the "Knowledge Library", by selecting keywords from those already created by scanning the list of already created keywords. If necessary, keywords defined in the document should change their word form, so as not to increase the list of already created keywords.

# Output
xlsx-file containing the top-N words (term) with the highest metric (value) and its most weighted variants (variants).

<p align="center">
  <img src="https://github.com/Donskoy-Andrey/sirius/blob/master/images/output.png" />
</p>

# Repository Description and Launch Conditions

0. Inside the **data** folder should be **original_data** with the following contents:\
0.1. **articles** - folder with original articles, database 1\.
0.2. **mydict** - folder with source dictionaries, database 2

1. **OCR.py** - script to start optical character recognition (in case of unreadable pdf source)
2. **check_file.py** - counting important words for file
3. **data_transfering.py** - library reading and loading script
4. **script.py** - **main script** which runs important words counting
5. **transrom_pdf.py** - library conversion from pdf to txt
6. **txt_file_processing.py** - processing txt results (converting to the original morphemes, removing garbage and unnecessary characters)

![Results](https://github.com/Donskoy-Andrey/sirius/blob/master/images/results.png)

# Basic problems
1. A person often takes keywords "out of his head," that is, they do not occur in the text.
2. It's difficult to process collections of texts because of the presence of trash words on each page.
Sometimes a person makes a keyword phrase of 5-6 words, and the algorithm is set to a maximum of 3 words.