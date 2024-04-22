from dataclasses import dataclass, field
from typing import List, Dict, Any
from dataclasses_json import dataclass_json
from datetime import datetime


@dataclass_json
@dataclass
class WorkItem:
    id: int
    rev: int
    area_path: str
    team_project: str
    iteration_path: str
    work_item_type: str
    state: str
    reason: str
    assigned_to_display_name: str
    assigned_to_url: str
    assigned_to_id: str
    assigned_to_unique_name: str
    assigned_to_image_url: str
    assigned_to_descriptor: str
    created_date: datetime
    created_by_display_name: str
    created_by_url: str
    created_by_id: str
    created_by_unique_name: str
    created_by_image_url: str
    created_by_descriptor: str
    changed_date: datetime
    changed_by_display_name: str
    changed_by_url: str
    changed_by_id: str
    changed_by_unique_name: str
    changed_by_image_url: str
    changed_by_descriptor: str
    comment_count: int
    title: str
    state_change_date: datetime
    priority: int
    description: str
    history: str
    tags: str
    comment_version_ref: Dict[str, Any]
    links: Dict[str, Dict[str, str]]
    url: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'WorkItem':
        fields = data.get("fields", {})
        assigned_to = fields.get("System.AssignedTo", {})
        created_by = fields.get("System.CreatedBy", {})
        changed_by = fields.get("System.ChangedBy", {})

        return cls(
            id=data.get("id"),
            rev=data.get("rev"),
            area_path=fields.get("System.AreaPath"),
            team_project=fields.get("System.TeamProject"),
            iteration_path=fields.get("System.IterationPath"),
            work_item_type=fields.get("System.WorkItemType"),
            state=fields.get("System.State"),
            reason=fields.get("System.Reason"),
            assigned_to_display_name=assigned_to.get("displayName"),
            assigned_to_url=assigned_to.get("url"),
            assigned_to_id=assigned_to.get("id"),
            assigned_to_unique_name=assigned_to.get("uniqueName"),
            assigned_to_image_url=assigned_to.get("imageUrl"),
            assigned_to_descriptor=assigned_to.get("descriptor"),
            created_date=datetime.fromisoformat(fields.get("System.CreatedDate")),
            created_by_display_name=created_by.get("displayName"),
            created_by_url=created_by.get("url"),
            created_by_id=created_by.get("id"),
            created_by_unique_name=created_by.get("uniqueName"),
            created_by_image_url=created_by.get("imageUrl"),
            created_by_descriptor=created_by.get("descriptor"),
            changed_date=datetime.fromisoformat(fields.get("System.ChangedDate")),
            changed_by_display_name=changed_by.get("displayName"),
            changed_by_url=changed_by.get("url"),
            changed_by_id=changed_by.get("id"),
            changed_by_unique_name=changed_by.get("uniqueName"),
            changed_by_image_url=changed_by.get("imageUrl"),
            changed_by_descriptor=changed_by.get("descriptor"),
            comment_count=fields.get("System.CommentCount"),
            title=fields.get("System.Title"),
            state_change_date=datetime.fromisoformat(fields.get("Microsoft.VSTS.Common.StateChangeDate")),
            priority=fields.get("Microsoft.VSTS.Common.Priority"),
            description=fields.get("System.Description"),
            history=fields.get("System.History"),
            tags=fields.get("System.Tags"),
            comment_version_ref=data.get("commentVersionRef", {}),
            links=data.get("_links", {}),
            url=data.get("url")
        )

#work_item = WorkItem.from_dict(json_data)
