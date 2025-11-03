from pydantic import BaseModel, Field, ConfigDict
from typing import Literal, Optional, List, Dict, Any, Union
from datetime import datetime
from uuid import uuid4

class MessagePart(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    kind: str  # Changed from Literal to str for flexibility
    text: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    file_url: Optional[str] = None

class A2AMessage(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    kind: Optional[str] = "message"  # Made optional
    role: str  # Changed from Literal to str
    parts: List[MessagePart]
    messageId: Optional[str] = Field(default_factory=lambda: str(uuid4()))
    taskId: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class PushNotificationConfig(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    url: str
    token: Optional[str] = None
    authentication: Optional[Dict[str, Any]] = None

class MessageConfiguration(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    blocking: bool = True
    acceptedOutputModes: Optional[List[str]] = ["text/plain", "image/png", "image/svg+xml"]
    pushNotificationConfig: Optional[PushNotificationConfig] = None

class MessageParams(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    message: A2AMessage
    configuration: Optional[MessageConfiguration] = Field(default_factory=MessageConfiguration)

class ExecuteParams(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    contextId: Optional[str] = None
    taskId: Optional[str] = None
    messages: List[A2AMessage]

class JSONRPCRequest(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    jsonrpc: str  # Changed from Literal to str
    id: str
    method: str  # Changed from Literal to str
    params: Union[MessageParams, ExecuteParams, Dict[str, Any]]  # More flexible

class TaskStatus(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    state: str  # Changed from Literal to str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    message: Optional[A2AMessage] = None

class Artifact(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    artifactId: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    parts: List[MessagePart]

class TaskResult(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    id: str
    contextId: str
    status: TaskStatus
    artifacts: List[Artifact] = []
    history: List[A2AMessage] = []
    kind: str = "task"

class JSONRPCResponse(BaseModel):
    model_config = ConfigDict(extra='allow')
    
    jsonrpc: str = "2.0"
    id: str
    result: Optional[TaskResult] = None
    error: Optional[Dict[str, Any]] = None
