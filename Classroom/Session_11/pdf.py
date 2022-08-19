import PyPDF2

#creating pdf file object
pdfFileObj = open(r'C:\Users\Chanponleusophea Ho\OneDrive\Documents\CamTech University\Year 1\Term 1\Basic Programming\Python\Classroom\Session_11\Autonomous Fruit Picking Robot System.pdf','rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of page in pdf file
print(pdfReader.numPages)

# creating a page object 
pageObj = pdfReader.getPage(0)

#extracting text form page 
print(pageObj.extractText())

#closing the pdf file object
pdfFileObj.close()
