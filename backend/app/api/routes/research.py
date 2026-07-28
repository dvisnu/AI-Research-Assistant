from fastapi import APIRouter

from app.web_research.models.research_request import (
    ResearchRequest,
)

from app.web_research.services.research_service import (
    ResearchService,
)

router = APIRouter()

service = ResearchService()


@router.post("/research")
async def research(request: ResearchRequest):

    return await service.research(request.query)