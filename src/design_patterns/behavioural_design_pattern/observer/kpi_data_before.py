from collections import namedtuple
from itertools import starmap

data = (("new", 10), ("open", 20), ("closed", 30))
nt = namedtuple("KPI", "name value")
KPI_Data = starmap(nt, data)

# Sending as email or restapi
# Way to handle this sort of a problem
if __name__ == "__main__":
    for kpi in KPI_Data:
        if kpi.name == "open":
            print("Current open Tickets: %s" % kpi.value)
        elif kpi.name == "new":
            print("New Tickets in last hour: %s" % kpi.value)
        elif kpi.name == "closed":
            print("Tickets closed in last hour: %s" % kpi.value)
