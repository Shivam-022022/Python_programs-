class Report:
    def generate(self):
        print("Generating generic report")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF report with page layout and fonts...")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report with rows, columns and formulas...")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML report with tags and styles...")


def produce_report(report):
    """Accepts any report object and calls generate()."""
    report.generate()


for r in (PDFReport(), ExcelReport(), HTMLReport()):
    produce_report(r)
