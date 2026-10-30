from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from config import OUTPUT_PATH


def generate_report(result):

    if not result:
        print("No data available for report.")
        return

    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    pdf_path = OUTPUT_PATH / "sales_report.pdf"

    try:
        pdf = SimpleDocTemplate(str(pdf_path), pagesize=A4)
        styles = getSampleStyleSheet()

        content = []

        # Report title
        content.append(Paragraph("Automated Sales Report", styles["Title"]))
        content.append(Spacer(1, 20))

        # Financial summary
        content.append(Paragraph("Financial Summary", styles["Heading2"]))

        content.append(Paragraph(
            f"Total Revenue: {result['total_revenue']:,.2f}",
            styles["Normal"]
        ))

        content.append(Paragraph(
            f"Total Cost: {result['total_cost']:,.2f}",
            styles["Normal"]
        ))

        content.append(Paragraph(
            f"Total Margin: {result['total_margin']:,.2f}",
            styles["Normal"]
        ))

        content.append(Paragraph(
            f"Total Units Sold: {result['total_units_sold']:,}",
            styles["Normal"]
        ))

        content.append(Spacer(1, 20))

        # Best products
        content.append(Paragraph("Top Products", styles["Heading2"]))

        products = sorted(
            result["best_products_by_revenue"].items(),
            key=lambda x: x[1],
            reverse=True
        )

        for product, revenue in products[:5]:
            content.append(Paragraph(
                f"{product}: {revenue:,.2f}",
                styles["Normal"]
            ))

        content.append(Spacer(1, 20))

        # Revenue by category
        content.append(Paragraph("Revenue by Category", styles["Heading2"]))

        for category, revenue in result["revenue_by_category"].items():
            content.append(Paragraph(
                f"{category.title()}: {revenue:,.2f}",
                styles["Normal"]
            ))

        content.append(Spacer(1, 20))

        # Monthly revenue
        content.append(Paragraph("Monthly Revenue", styles["Heading2"]))

        for month, revenue in result["revenue_by_month"].items():
            content.append(Paragraph(
                f"{month}: {revenue:,.2f}",
                styles["Normal"]
            ))

        # Generate PDF
        pdf.build(content)

        print(f"Report generated: {pdf_path}")

    except Exception as e:
        print(f"Report generation failed: {e}")
