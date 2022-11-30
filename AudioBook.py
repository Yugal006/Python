import pyttsx3
import PyPDF2

book = open ("try.pdf" , 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
engine = pyttsx3.init()
volume = engine.setProperty('rate', 150)
voices = engine.getProperty('voices')


for num in range(0, pages):
    engine.setProperty('voice', voices[3].id) 
    page = pdfReader.getPage(7)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
        
