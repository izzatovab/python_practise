from datetime import datetime
import os
from .base import InvoiceGenerator


class HTMLInvoiceGenerator(InvoiceGenerator):
    def generate_invoice(self):
        folder = "invoices"
        os.makedirs(folder, exist_ok=True)

        fayl_nomi = os.path.join(folder, f"{self.client_name}_invoice.html")
        jami = self.calculate_total()

        with open(fayl_nomi, "w", encoding="utf-8") as f:
            f.write("<html><head><title>Hisob-faktura</title></head><body>")
            f.write(f"<h1>🍽️ Mijoz: {self.client_name}</h1>")
            f.write(f"<p>Sana: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>")
            f.write("<table border='1' cellpadding='5' cellspacing='0'>")
            f.write("<tr><th>Taom</th><th>Narxi</th><th>Soni</th><th>Jami</th></tr>")
            for item in self.items:
                f.write(f"<tr><td>{item['name']}</td><td>{item['price']}</td><td>{item['quantity']}</td><td>{item['price'] * item['quantity']}</td></tr>")
            f.write(f"<tr><td colspan='3'><b>Umumiy summa:</b></td><td><b>{jami} so‘m</b></td></tr>")
            f.write("</table></body></html>")

        return fayl_nomi
