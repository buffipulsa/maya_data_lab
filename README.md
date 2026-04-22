# maya_data_lab

[![Docs](https://img.shields.io/badge/docs-online-blue)](https://buffipulsa.github.io/maya_data_lab/)

Research and prototype project exploring **Git-friendly, deterministic data formats for Maya asset data**.

---

## Overview

This project explores externalizing Maya data (UVs, skin weights, proxy meshes, etc.)
into structured, deterministic formats that are:

- versionable in Git
- decoupled from Maya scene files
- safe to reapply later in the pipeline

The goal is to make asset data easier to:
- track
- validate
- update without rebuilding rigs

---

## Why

Working directly inside Maya scene files makes it difficult to:

- track changes in version control
- validate data independently
- update data without rebuilding assets

This project separates data from scene state, enabling more predictable and maintainable workflows.

---

## Quick Example

```python
from maya_data_lab.maya.dependency_node import DependencyNodeHandle

node = DependencyNodeHandle("pCube1")
print(node.dependency_fn.name())
```

Example UV data (JSON):

```json
{
    "schema_version": 1,
    "mesh_name": "pPlaneShape1",
    "topology": {
        "vertex_count": 4,
        "face_counts": [4],
        "face_vertex_indicies": [0,1,2,3]
    },
    "uv_sets": [
        {
            "uv_set_name": "map1",
            "u_values": [0.0, 1.0, 1.0, 0.0],
            "v_values": [0.0, 0.0, 1.0, 1.0],
            "uv_counts": [4],
            "uv_indices": [0, 1, 2, 3]
        }
    ]
}
```

---

## Current Scope

The current prototype focuses on:

- UV export/import (in progress)
- topology validation
- JSON-based data schemas

Future areas may include:

- skinCluster weight data
- proxy mesh data
- generalized data contracts for rigging pipelines

---

## Project Structure

```text
src/maya_data_lab/
    uv/
        exporter.py
        importer.py
        models.py

docs/
    source/

examples/
    uv/
        sample_uv_data.json
```

- `src/` → core library code  
- `docs/` → Sphinx documentation  
- `examples/` → reference data and schema examples  

---

## Goals

- Define clear data contracts for Maya asset data  
- Ensure deterministic output for Git-friendly diffs  
- Separate data from scene state  
- Enable safe re-application of data later in the pipeline  

---

## Status

🚧 Early prototype / R&D

---

## Documentation

👉 https://buffipulsa.github.io/maya_data_lab/

---

## License

MIT
