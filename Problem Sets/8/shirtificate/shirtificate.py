from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="portrait", format="A4")

pdf.add_page()

pdf.set_font("helvetica", "B", 16)

pdf.cell(0, 70, "CS50 Shitificate", new_x="LMARGIN", new_y="NEXT", align='C')

pdf.image("shirtificate.png", w=pdf.epw)

pdf.set_text_color(255, 255, 255)
pdf.text(x=85, y=140, txt = f"{name} took CS50")

pdf.output("shirtificate.pdf")
