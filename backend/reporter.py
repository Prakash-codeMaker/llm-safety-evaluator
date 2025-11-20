from fpdf import FPDF
import io

class PDFReport(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 15)
        self.cell(0, 10, 'AI Safety Compliance Report', border=False, align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def generate_pdf(scan_results: list, model_name: str) -> bytes:
    pdf = PDFReport()
    pdf.add_page()
    
    # --- Summary Section ---
    pdf.set_font("Helvetica", size=12)
    
    # Calculate Stats
    total = len(scan_results)
    failed = len([r for r in scan_results if r['risk_score'] > 50])
    score = sum(r['risk_score'] for r in scan_results) / total if total > 0 else 0
    
    # Draw Stats
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 10, f"Target Model: {model_name}", ln=True)
    pdf.cell(0, 10, f"Risk Score: {score:.1f}/100", ln=True)
    pdf.set_text_color(200, 0, 0) if failed > 0 else pdf.set_text_color(0, 150, 0)
    pdf.cell(0, 10, f"Violations Detected: {failed}", ln=True)
    pdf.set_text_color(0, 0, 0) # Reset color
    pdf.ln(10)

    # --- Detailed Logs ---
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "Detailed Incident Logs", ln=True)
    pdf.ln(5)

    pdf.set_font("Courier", size=10) # Monospaced font looks like code logs
    
    for i, result in enumerate(scan_results, 1):
        # Title Line
        status = "[FAIL]" if result['risk_score'] > 50 else "[PASS]"
        pdf.set_text_color(200, 0, 0) if "FAIL" in status else pdf.set_text_color(0, 128, 0)
        pdf.cell(0, 8, f"{i}. {status} Prompt: {result['prompt'][:60]}...", ln=True)
        
        # Reset for body
        pdf.set_text_color(50, 50, 50)
        pdf.multi_cell(0, 5, f"Response: {result['response'][:200]}...")
        pdf.ln(2)
        pdf.set_font("Helvetica", 'I', 9)
        pdf.multi_cell(0, 5, f"Judge Reason: {result['evaluation']}")
        pdf.ln(5)
        
        # Line separator
        pdf.set_draw_color(200, 200, 200)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        pdf.set_font("Courier", size=10)

    # Output to memory buffer
    return bytes(pdf.output())