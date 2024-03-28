from dataclasses import dataclass
from typing import Optional

@dataclass
class BrowserstackSessionLogModel:
    name: str
    duration: Optional[float]
    os: str
    os_version: str
    browser_version: Optional[str]
    browser: Optional[str]
    device: str
    status: str
    hashed_id: str
    reason: Optional[str]
    build_name: str
    project_name: str
    build_hashed_id: str
    test_priority: Optional[str]
    logs: str
    browserstack_status: str
    created_at: str
    browser_url: str
    public_url: str
    video_url: str
    browser_console_logs_url: str
    har_logs_url: str
    selenium_logs_url: str
