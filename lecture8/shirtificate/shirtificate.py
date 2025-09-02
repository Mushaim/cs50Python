from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        page_width = pdf.w
        image_width = 180
        center = (page_width - image_width) / 2
        self.image("shirtificate.png", center, 60, image_width)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=25)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(40, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", style="I", size=8)

name = input("Name: ")

# Instantiation of inherited class
pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Times", size=25)
pdf.set_text_color(255,255,255)
pdf.cell(0, 180, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
