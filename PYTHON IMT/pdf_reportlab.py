import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def page_Pdf(c):
    c.drawString(45,45,'welcome......')
c=canvas.Canvas("demo.pdf")
page_Pdf(c)
c.showPage()
c.save()
    

