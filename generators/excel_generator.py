from datetime import datetime
from openpyxl import Workbook
import os
from .base import InvoiceGenerator


class ExcelInvoiceGenerator(InvoiceGenerator):
    def generate_invoice(self):
        folder = "invoices"
        os.makedirs(folder, exist_ok=True)

        fayl_nomi = os.path.join(folder, f"{self.client_name}_invoice.xlsx")
        wb = Workbook()
        ws = wb.active
        ws.title = "Hisob-faktura"

        ws.append(["Taom nomi", "Narxi (so‘m)", "Soni", "Jami"])
        for item in self.items:
            ws.append([
                item["name"],
                item["price"],
                item["quantity"],
                item["price"] * item["quantity"]
            ])

        ws.append(["", "", "Umumiy:", self.calculate_total()])
        ws.append(["", "", "Sana:", datetime.now().strftime("%Y-%m-%d %H:%M")])

        wb.save(fayl_nomi)
        return fayl_nomi
