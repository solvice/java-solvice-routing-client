# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**UUID**](UUID.md) |  |  [optional]
**solver** | [**SolverEnum**](#SolverEnum) |  |  [optional]
**status** | [**StatusEnum**](#StatusEnum) |  |  [optional]

<a name="SolverEnum"></a>
## Enum: SolverEnum
Name | Value
---- | -----
VRP | &quot;VRP&quot;
PDP | &quot;PDP&quot;

<a name="StatusEnum"></a>
## Enum: StatusEnum
Name | Value
---- | -----
ERROR | &quot;ERROR&quot;
QUEUED | &quot;QUEUED&quot;
SOLVING | &quot;SOLVING&quot;
SOLVED | &quot;SOLVED&quot;
