import domain_model
import proposal_error
import abc

__proposals = {
    "Sem19A-023": domain_model.create_proposal("Sem19A-023"),
    "Sem19A-024": domain_model.create_proposal("Sem19A-024"),
    "Sem19A-025": domain_model.create_proposal("Sem19A-025"),
}


class AbstractRepository(abc.ABC):
    @abc.abstractclassmethod
    def find_by_id(id: str):
        raise NotImplementedError

    @abc.abstractclassmethod
    def list():
        raise NotImplementedError

    @abc.abstractclassmethod
    def add(proposal: domain_model.Proposal):
        raise NotImplementedError


class InMemoryRepository(AbstractRepository):
    def __init__(self, __proposals) -> None:
        self.proposals = {
            "Sem19A-023": domain_model.create_proposal("Sem19A-023"),
            "Sem19A-024": domain_model.create_proposal("Sem19A-024"),
            "Sem19A-025": domain_model.create_proposal("Sem19A-025"),
        }
        super().__init__()

    def find_by_id(self, id: str):
        if id in self.proposals:
            return self.proposals[id].dict()
        else:
            raise proposal_error.ProposalError("Proposal not found.", status_code=404)

    def list(self):
        return self.proposals

    def add(self, proposal: domain_model.Proposal):
        if proposal.id not in self.proposals:
            proposal.serial_number = domain_model.get_new_serial_number()
            self.proposals[proposal.id] = proposal


class SQLAlchemyRepository(AbstractRepository):
    def __init__(self) -> None:
        super().__init__()

    def find_by_id(self, id: str):
        pass

    def list(self):
        pass

    def add(self, proposal: domain_model.Proposal):
        pass


repo = InMemoryRepository(__proposals)
# repo = SQLAlchemyRepository()
