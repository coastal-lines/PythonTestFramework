from dataclasses import dataclass, field
from typing import List, Dict, Any
from dataclasses_json import dataclass_json


@dataclass
class MainPatchResponseUser:
    displayName: str
    url: str
    _links: Dict[str, Dict[str, str]]
    id: str
    uniqueName: str
    imageUrl: str
    descriptor: str

@dataclass
class MainPatchResponseRelationAttributes:
    authorizedDate: str
    id: int
    resourceCreatedDate: str
    resourceModifiedDate: str
    revisedDate: str
    name: str

@dataclass
class MainPatchResponseRelation:
    rel: str
    url: str
    attributes: MainPatchResponseRelationAttributes

@dataclass
class MainPatchResponseLinks:
    self_: Dict[str, str] = field(default_factory=dict)
    workItemUpdates: Dict[str, str] = field(default_factory=dict)
    workItemRevisions: Dict[str, str] = field(default_factory=dict)
    workItemComments: Dict[str, str] = field(default_factory=dict)
    html: Dict[str, str] = field(default_factory=dict)
    workItemType: Dict[str, str] = field(default_factory=dict)
    fields: Dict[str, str] = field(default_factory=dict)

@dataclass
class MainPatchResponseFields:
    System_AreaPath: str
    System_TeamProject: str
    System_IterationPath: str
    System_WorkItemType: str
    System_State: str
    System_Reason: str
    System_CreatedDate: str
    System_CreatedBy: MainPatchResponseUser
    System_ChangedDate: str
    System_ChangedBy: MainPatchResponseUser
    System_CommentCount: int
    System_Title: str
    Microsoft_VSTS_Common_StateChangeDate: str
    Microsoft_VSTS_Common_Priority: int
    System_Description: str

@dataclass_json
@dataclass
class MainPatchResponse:
    id: int
    rev: int
    fields: MainPatchResponseFields
    relations: List[MainPatchResponseRelation]
    _links: MainPatchResponseLinks
    url: str
