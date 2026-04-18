from dataclasses import dataclass


@dataclass
class SupportRequest:
    customer: str
    issue_type: str
    message: str


class SupportHandler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request: SupportRequest):
        if self.can_handle(request):
            self.process(request)
            return
        if self._successor is not None:
            self._successor.handle(request)
            return
        print(f"No handler found for: {request.issue_type}")

    def can_handle(self, request: SupportRequest):
        raise NotImplementedError

    def process(self, request: SupportRequest):
        raise NotImplementedError


class BillingHandler(SupportHandler):
    def can_handle(self, request: SupportRequest):
        return request.issue_type == "billing"

    def process(self, request: SupportRequest):
        print(f"Billing handled request for {request.customer}")


class TechnicalHandler(SupportHandler):
    def can_handle(self, request: SupportRequest):
        return request.issue_type == "technical"

    def process(self, request: SupportRequest):
        print(f"Technical support handled request for {request.customer}")


class EscalationHandler(SupportHandler):
    def can_handle(self, request: SupportRequest):
        return request.issue_type == "priority"

    def process(self, request: SupportRequest):
        print(f"Escalation team handled request for {request.customer}")


def build_support_chain():
    return BillingHandler(TechnicalHandler(EscalationHandler()))


if __name__ == "__main__":
    support_chain = build_support_chain()

    support_chain.handle(SupportRequest("Alice", "billing", "Refund request"))
    support_chain.handle(SupportRequest("Bob", "technical", "Cannot login"))
    support_chain.handle(SupportRequest("Carol", "priority", "Production down"))
    support_chain.handle(SupportRequest("Dave", "general", "Need help"))

