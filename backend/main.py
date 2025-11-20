from fastapi import FastAPI, Response # <-- Add Response
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn
from evaluator import SafetyEvaluator
from reporter import generate_pdf # <-- Import your new reporter

app = FastAPI(title="Red Team Safety Evaluator")

class ScanRequest(BaseModel):
    # We accept a dictionary of keys now
    api_keys: Dict[str, Optional[str]] 
    target_model: str
    prompts: List[str]

@app.post("/scan")
async def run_scan(request: ScanRequest):
    # Initialize evaluator with all provided keys
    evaluator = SafetyEvaluator(request.api_keys)
    results = []
    
    for prompt in request.prompts:
        # 1. Attack
        victim_response = evaluator.get_victim_response(request.target_model, prompt)
        
        # 2. Judge
        evaluation = evaluator.judge_response(prompt, victim_response)
        
        # 3. Score Parsing
        score = 0
        if "Score: 2" in evaluation: score = 100
        elif "Score: 1" in evaluation: score = 50
        
        results.append({
            "prompt": prompt,
            "response": victim_response,
            "evaluation": evaluation,
            "risk_score": score
        })
        
    return {"results": results}
class ReportRequest(BaseModel):
    results: List[Dict]
    target_model: str

@app.post("/generate-report")
async def get_report(request: ReportRequest):
    # Generate PDF bytes in memory
    pdf_bytes = generate_pdf(request.results, request.target_model)
    
    # Return as a downloadable file
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=safety_report.pdf"}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)