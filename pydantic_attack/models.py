from pydantic import BaseModel
from typing import Optional, List, Union, Literal


class Filter(BaseModel):

    platforms: List[
        Literal[
            "Linux",
            "macOS",
            "Windows",
            "Network",
            "PRE",
            "Containers",
            "Office 365",
            "SaaS",
            "Google Workspace",
            "IaaS",
            "Azure AD",
        ]
    ] = [
        "Linux",
        "macOS",
        "Windows",
        "Network",
        "PRE",
        "Containers",
        "Office 365",
        "SaaS",
        "Google Workspace",
        "IaaS",
        "Azure AD",
    ]
    # stages: Optional[Literal["act", "prepare"]] = ""


class Gradient(BaseModel):
    colors: List[str] = ["#ff6666ff", "#ffe766ff", "#8ec843ff"]
    minValue: int = 0
    maxValue: int = 100


class Layout(BaseModel):
    layout: Literal["side", "flat", "mini"] = "side"
    aggregateFunction: Literal["average", "min", "max", "sum"] = "average"
    showID: bool = False
    showName: bool = True
    showAggregateScores: bool = False
    countUnscored: bool = False


class Legend(BaseModel):
    color: str
    label: str


class Metadata(BaseModel):
    key: str = ""
    value: str = ""


class Technique(BaseModel):
    techniqueID: str
    tactic: str
    score: int = 0
    color: str = ""
    comment: str = ""
    enabled: bool = True
    metadata: Optional[Union[List[Metadata], Metadata]] = []
    links: Optional[List] = []
    showSubtechniques: bool = False
    # aggregateScore: bool = True


class Versions(BaseModel):
    attack: str = "13"
    navigator: str = "4.7.1"
    layer: Literal["3.0", "4.0", "4.1", "4.2", "4.3"] = "4.3"


class Layer(BaseModel):
    name: str
    versions: Versions = Versions()
    domain: Literal[
        "enterprise-attack", "mobile-attack", "ics-attack"
    ] = "enterprise-attack"
    description: str = ""
    filters: Filter = Filter()
    sorting: int = 0
    layout: Layout = Layout()
    hideDisabled: bool = False
    techniques: List[Technique]
    gradient: Gradient = Gradient()
    legendItems: Optional[Union[Legend, List]] = []
    metadata: Optional[List[str]] = []
    links: Optional[List[str]] = []
    showTacticRowBackground: bool = False
    tacticRowBackground: str = "#dddddd"
    selectTechniquesAcrossTactics: bool = True
    selectSubtechniquesWithParent: bool = False
