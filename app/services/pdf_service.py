# PDF service module
import uuid
from pathlib import Path

from playwright.sync_api import sync_playwright


class PDFService:

    @staticmethod
    def generate_pdf(html_content: str):

        Path("generated").mkdir(
            exist_ok=True
        )

        pdf_name = f"{uuid.uuid4()}.pdf"

        pdf_path = f"generated/{pdf_name}"

        with sync_playwright() as p:

            browser = p.chromium.launch()

            page = browser.new_page()

            page.set_content(
                html_content,
                wait_until="networkidle"
            )

            page.pdf(
                path=pdf_path,
                format="A4",
                print_background=True,
                margin={
                    "top": "10mm",
                    "bottom": "10mm",
                    "left": "10mm",
                    "right": "10mm"
                }
            )

            browser.close()

        return pdf_path