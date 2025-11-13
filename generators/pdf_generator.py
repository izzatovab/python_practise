from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from .base import InvoiceGenerator


class PDFInvoiceGenerator(InvoiceGenerator):
    def generate_invoice(self):
        folder = "invoices"
        os.makedirs(folder, exist_ok=True)

        fayl_nomi = os.path.join(folder, f"{self.client_name}_invoice.pdf")
        pdf = canvas.Canvas(fayl_nomi, pagesize=A4)

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(180, 800, "🍽️ Restoran Hisob-fakturasi")

        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, 770, f"Mijoz: {self.client_name}")
        pdf.drawString(50, 750, f"Sana: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

        pdf.drawString(50, 720, "Buyurtmalar:")
        y = 700
        for item in self.items:
            line = f"- {item['name']} x{item['quantity']} = {item['price'] * item['quantity']} so‘m"
            pdf.drawString(70, y, line)
            y -= 20

        pdf.drawString(50, y - 10, f"Jami: {self.calculate_total()} so‘m")
        pdf.save()
        return fayl_nomi
