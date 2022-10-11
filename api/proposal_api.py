from proposal_error import ProposalError
from typing import Dict
from domain_model import Proposal
import fastapi
import proposal_repository
from typing import DefaultDict

router = fastapi.APIRouter()


@router.get("/api/proposal/{id}")
def proposal(id: str) -> Proposal:
    try:
        return proposal_repository.repo.find_by_id(id)
    except ProposalError as pe:
        return fastapi.Response(content=pe.error_msg, status_code=pe.status_code)


@router.get("/api/proposals", name="all_proposals")
def proposals() -> DefaultDict(Proposal):
    return proposal_repository.repo.list()


@router.post("/api/proposal", name="add_proposal", status_code=201)
async def proposal_post(proposal: Proposal) -> Proposal:
    proposal_repository.repo.add(proposal)
    return proposal
