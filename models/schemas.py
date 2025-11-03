from pydantic import BaseModel
from typing import List, Optional, Dict


class PackageDependency(BaseModel):
    name: str
    version: Optional[str] = None


class PythonDependenciesRequest(BaseModel):
    """Request model for Python dependencies - mimics requirements.txt structure"""
    packages: List[str] = []  # e.g., ["flask==2.0.1", "requests>=2.25.0", "numpy"]


class NpmDependenciesRequest(BaseModel):
    """Request model for npm dependencies - mimics package.json structure"""
    dependencies: Optional[Dict[str, str]] = None
    devDependencies: Optional[Dict[str, str]] = None


class PackageHealthResponse(BaseModel):
    name: str
    current_version: Optional[str]
    latest_version: Optional[str]
    is_outdated: bool
    has_vulnerabilities: bool
    vulnerability_count: int
    is_deprecated: bool
    health_score: int
    recommendation: str
    vulnerabilities: List[Dict] = []


class OverallHealthResponse(BaseModel):
    total_packages: int
    outdated_count: int
    vulnerable_count: int
    deprecated_count: int
    overall_health_score: int
    packages: List[PackageHealthResponse]
