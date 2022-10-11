from typing import List
from pydantic import BaseModel
import uuid


class Author(BaseModel):
    name: str
    principle_investigator: bool
    contact_author: bool


class Proposal(BaseModel):
    serial_number: str
    id: str
    authors: List[Author] = None
    title: str
    abstract: str
    scientific_justification: str


def create_proposal(id: str):
    author1_data = {
        "name": "Author1",
        "principle_investigator": False,
        "contact_author": False,
    }
    author1 = Author(**author1_data)

    author2_data = {
        "name": "Author2",
        "principle_investigator": True,
        "contact_author": True,
    }
    author2 = Author(**author2_data)

    proposal_data = {
        "serial_number": str(uuid.uuid4()),
        "id": id,
        "authors": [author1, author2],
        "title": "title1",
        "abstract": "abstract1",
        "scientific_justification": "scientific_justification1",
    }

    return Proposal(**proposal_data)


def get_new_serial_number():
    return str(uuid.uuid4())


def create_invalid_proposal(id: str):

    proposal_data = {
        "serial_number": "",
        "id": "invalid id: " + id,
        "authors": [],
        "title": "",
        "abstract": "",
        "scientific_justification": "",
    }

    return Proposal(**proposal_data)
