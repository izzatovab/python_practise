class InvoiceManager:
    def __init__(self, generator):
        self.generator = generator

    def export_invoice(self):
        path = self.generator.generate_invoice()
        print(f"✅ Hisob-faktura yaratildi: {path}")
