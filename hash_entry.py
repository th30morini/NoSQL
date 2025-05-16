import hashlib
from datetime import datetime

def add_log_hash(entry):
    original_timestamp = entry["timestamp"] 
    concat = original_timestamp + entry["ip"] + entry["user"] + entry["action"] + entry["status"]
    log_hash = hashlib.sha256(concat.encode("utf-8")).hexdigest()
    entry["log_hash"] = log_hash
    entry["timestamp"] = datetime.strptime(original_timestamp, "%Y-%m-%dT%H:%M:%SZ")
    return entry
