
from prometheus_client import Counter, Histogram

borrow_requests_total = Counter(
    "library_borrow_requests_total",
    "Total borrow requests"
)

borrow_latency_seconds = Histogram(
    "library_borrow_latency_seconds",
    "Borrow request latency"
)
