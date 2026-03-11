from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    user_id: str
    num_items: int = 10

class RecommendationService:
    """Service stub for user recommendations. Connect to BentoML in production."""

    def predict(self, parsed: dict) -> dict:
        req = RecommendationRequest(**parsed)
        # TODO: integrate with BentoML and Feast for real inference
        return {"recommendations": [], "status": "stub", "request": req.dict()}
