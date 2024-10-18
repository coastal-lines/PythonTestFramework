from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any
from dataclasses_json import dataclass_json


@dataclass
class AvatarLink:
    href: str

@dataclass
class AssignedTo:
    displayName: str
    url: str
    links: AvatarLink
    id: str
    uniqueName: str
    imageUrl: str
    descriptor: str

@dataclass
class CreatedBy:
    displayName: str
    url: str
    id: str
    links: AvatarLink
    uniqueName: str
    imageUrl: str
    descriptor: str

@dataclass
class ChangedBy:
    displayName: str
    url: str
    id: str
    links: AvatarLink
    uniqueName: str
    imageUrl: str
    descriptor: str

@dataclass
class Fields:
    System_AreaPath: str
    System_TeamProject: str
    System_IterationPath: str
    System_WorkItemType: str
    System_State: str
    System_Reason: str
    System_CreatedDate: str
    System_CreatedBy: CreatedBy
    System_ChangedDate: str
    System_ChangedBy: ChangedBy
    System_CommentCount: int
    System_Title: str
    Microsoft_VSTS_Common_StateChangeDate: str
    Microsoft_VSTS_Common_Priority: int
    System_Description: str
    System_History: str
    System_Tags: str

@dataclass
class CommentVersionRef:
    commentId: int
    version: int
    url: str

@dataclass
class Links:
    self: Dict[str, str]
    workItemUpdates: Dict[str, str]
    workItemRevisions: Dict[str, str]
    workItemComments: Dict[str, str]
    html: Dict[str, str]
    workItemType: Dict[str, str]
    fields: Dict[str, str]

@dataclass
class AttachmentAttributes:
    authorizedDate: datetime
    id: int
    resourceCreatedDate: datetime
    resourceModifiedDate: datetime
    revisedDate: datetime
    name: str

@dataclass
class Relations:
    rel: str
    url: str
    attributes: AttachmentAttributes

@dataclass
class ResponsePatchWorkitemComment:
    id: str
    rev: str
    fields: Fields
    relations: Relations
    links: Links
    url: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        fields_data = data.get("fields")
        relations = data.get("relations")[0]
        links_data = data.get("_links")
        return cls(
            id=data.get("id"),
            rev=data.get("rev"),
            fields=Fields(
                System_AreaPath=fields_data.get("System.AreaPath"),
                System_TeamProject=fields_data.get("System.TeamProject"),
                System_IterationPath=fields_data.get("System.IterationPath"),
                System_WorkItemType=fields_data.get("System.WorkItemType"),
                System_State=fields_data.get("System.State"),
                System_Reason=fields_data.get("System.Reason"),
                System_CreatedDate=fields_data.get("System.CreatedDate"),
                System_CreatedBy=CreatedBy(
                    displayName=fields_data.get("System.CreatedBy").get("displayName"),
                    url=fields_data.get("System.CreatedBy").get("url"),
                    id=fields_data.get("System.CreatedBy").get("id"),
                    links=AvatarLink(
                        href=fields_data.get("System.CreatedBy").get("_links").get("avatar").get("href")
                    ),
                    uniqueName=fields_data.get("System.CreatedBy").get("uniqueName"),
                    imageUrl=fields_data.get("System.CreatedBy").get("imageUrl"),
                    descriptor=fields_data.get("System.CreatedBy").get("descriptor")
                ),
                System_ChangedDate=fields_data.get("System.ChangedDate"),
                System_ChangedBy=ChangedBy(
                    displayName=fields_data.get("System.ChangedBy").get(""),
                    url=fields_data.get("System.ChangedBy").get("url"),
                    id=fields_data.get("System.ChangedBy").get("id"),
                    links=AvatarLink(
                        href=fields_data.get("System.ChangedBy").get("_links").get("avatar").get("href")
                    ),
                    uniqueName=fields_data.get("System.ChangedBy").get("uniqueName"),
                    imageUrl=fields_data.get("System.ChangedBy").get("imageUrl"),
                    descriptor=fields_data.get("System.ChangedBy").get("descriptor")
                ),
                System_CommentCount=fields_data.get("System.CommentCount", 0),
                System_Title=fields_data.get("System.Title"),
                Microsoft_VSTS_Common_StateChangeDate=fields_data.get("Microsoft.VSTS.Common.StateChangeDate"),
                Microsoft_VSTS_Common_Priority=fields_data.get("Microsoft.VSTS.Common.Priority", 0),
                System_Description=fields_data.get("System.Description"),
                System_History=fields_data.get("System.History"),
                System_Tags=fields_data.get("System.Tags")
            ),
            relations=Relations(
                rel=relations.get("rel"),
                url=relations.get("url"),
                attributes=AttachmentAttributes(
                    authorizedDate=relations.get("attributes").get("authorizedDate"),
                    id=relations.get("id"),
                    resourceCreatedDate=relations.get("attributes").get("resourceCreatedDate"),
                    resourceModifiedDate=relations.get("attributes").get("resourceModifiedDate"),
                    revisedDate=relations.get("attributes").get("revisedDate"),
                    name=relations.get("attributes").get("name")
                )
            ),
            links=Links(
                self=links_data.get("self", {}),
                workItemUpdates=links_data.get("workItemUpdates", {}),
                workItemRevisions=links_data.get("workItemRevisions", {}),
                workItemComments=links_data.get("workItemComments", {}),
                html=links_data.get("html", {}),
                workItemType=links_data.get("workItemType", {}),
                fields=links_data.get("fields", {})
            ),
            url=data.get("url")
        )

