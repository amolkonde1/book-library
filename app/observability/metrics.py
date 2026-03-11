
from prometheus_client import Counter

borrow_requests_total = Counter(
    "library_borrow_requests_total",
    "Total number of borrow requests"
)
