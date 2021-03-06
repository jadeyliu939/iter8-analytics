"""
Module containing pydantic data models for iter8 v2
"""
# core python dependencies
from typing import Sequence, Dict
from datetime import datetime

# external module dependencies
from pydantic import BaseModel, Field, conlist

class Version(BaseModel):
    """
    Pydantic model for Version
    """
    name: str = Field(..., description = "version name")
    tags: Dict[str, str] = Field(None, descriptiopn = "version tags (key-value pairs)")

class VersionInfo(BaseModel):
    """
    Pydantic model for versionInfo field in experiment spec subresource
    """
    baseline: Version = Field(..., description = "baseline version")
    candidates: Sequence[Version] = Field(None, description = "a list of candidate versions")

class Objective(BaseModel):
    """
    Pydantic model for experiment objective
    """
    metric: str = Field(..., description = "metric name")
    upperLimit: float = Field(None, description = "upper limit for the metric")
    lowerLimit: float = Field(None, description = "lower limit for the metric")

class Criteria(BaseModel):
    """
    Pydantic model for Criteria field in experiment spec
    """
    objectives: Sequence[Objective] = Field(None, description = "sequence of objectives")

class ExperimentSpec(BaseModel):
    """
    Pydantic model for experiment spec subresource
    """
    versionInfo: VersionInfo = Field(..., description = "versions in the experiment")
    criteria: Criteria = Field(None, description = "experiment criteria")

class ObjectMeta(BaseModel):
    """
    Pydantic model for k8s object meta
    """
    name: str = Field(..., description = "name of the k8s resource")

class MetricSpec(BaseModel):
    """
    Pydantic model for metric spec subresource
    """
    params: Dict[str, str] = Field(None, description = "parameters to be used \
        as part of the REST query for this metric")
    provider: str = Field(..., description = "identifier for the metrics backend")

class MetricResource(BaseModel):
    """
    Pydantic model for metric resource
    """
    metadata: ObjectMeta = Field(..., description = "metrics resource metadata")
    spec: MetricSpec = Field(..., description = "metrics resource spec")

class VersionMetric(BaseModel):
    """
    Pydantic model for a version metric object
    """
    max: float = Field(None, description = "maximum observed value \
        for this metric for this version")
    min: float = Field(None, description = "minimum observed value \
        for this metric for this version")
    value: float = Field(None, description = "last observed value \
        for this metric for this version")
    sample_size: float = Field(None, description = "last observed value \
        for the sample_size metric for this version; this is none if sample_size is not specified")

class AggregatedMetric(BaseModel):
    """
    Pydantic model for an aggregated metric object
    """
    max: float = Field(None, description = "maximum observed value for this metric")
    min: float = Field(None, description = "minimum observed value for this metric")
    # min_items == 1 since at least one version (baseline) will be present
    data: Dict[str, VersionMetric] = Field(..., \
        description = "dictionary with version names as keys and VersionMetric objects as values")

class AggregatedMetrics(BaseModel):
    """
    Pydantic model for aggregated metrics response
    """
    data: Dict[str, AggregatedMetric] = Field(..., \
    description = "dictionary with metric names as keys and AggregatedMetric objects as values")
    message: str = Field(None, description = "human-readable description of aggregated metrics")

class VersionAssessments(BaseModel):
    """
    Pydantic model for version assessments returned by iter8 analytics v2
    """
    data: Dict[str, Sequence[bool]] = Field(..., \
    description = "dictionary with version name as key and sequence of booleans as value; each element of the sequence indicates if the version satisfies the corresponding objective.")
    message: str = Field(None, description = "human-readable description of version assessments")

class WinnerAssessment(BaseModel):
    """
    Pydantic model for winner assessment
    """
    winnerFound: bool = Field(False, description = "boolean value indicating if winner is found")
    winner: str = Field(None, description = "winning version; None if winner not found")

class Weights(BaseModel):
    """
    Pydantic model for weights returned by iter8 analytics v2
    """
    dummy: int

class Analysis(BaseModel):
    """
    Pydantic model for analysis section of experiment status
    """
    aggregatedMetrics: AggregatedMetrics = Field(None, \
        description = "aggregated metrics")
    versionAssessments: VersionAssessments = Field(None, \
        description = "version assessments")
    winnerAssessment: WinnerAssessment = Field(None, \
        description = "winner assessment")
    weights: Weights = Field(None, description = "weight recommendations")

class ExperimentStatus(BaseModel):
    """
    Pydantic model for experiment status subresource
    """
    startTime: datetime = Field(..., description = "starttime of the experiment")
    analysis: Analysis = Field(None, description = "currently available analysis")

class ExperimentResource(BaseModel):
    """
    Pydantic model for experiment resource
    """
    spec: ExperimentSpec = Field(..., description = "experiment spec subresource")
    status: ExperimentStatus = Field(..., description = "experiment status subresource")

class ExperimentResourceAndMetricResources(BaseModel):
    """
    Pydantic model that encapsulates experiment resource and a list of metric resources
    """
    experimentResource: ExperimentResource = Field(..., description="experiment resource")
    metricResources: Sequence[MetricResource] = Field(..., \
        description="a sequence of metric resources")
