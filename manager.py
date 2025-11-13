from generators.pdf_generator import PDFInvoiceGenerator
from generators.excel_generator import ExcelInvoiceGenerator
from generators.html_generator import HTMLInvoiceGenerator
from main import InvoiceManager
from menu import buyurtma_olish


if __name__ == "__main__":
    tanlanganlar = buyurtma_olish()

    if not tanlanganlar:
        print("Hech narsa tanlanmadi.")
    else:
        ism = input("\nMijoz ismini kiriting: ")

        pdf_gen = PDFInvoiceGenerator(ism, tanlanganlar)
        excel_gen = ExcelInvoiceGenerator(ism, tanlanganlar)
        html_gen = HTMLInvoiceGenerator(ism, tanlanganlar)

        for gen in [pdf_gen, excel_gen, html_gen]:
            manager = InvoiceManager(gen)
            manager.export_invoice()

        print("\n✅ Barcha hisob-fakturalar muvaffaqiyatli yaratildi!")
