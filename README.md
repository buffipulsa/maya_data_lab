# maya_data_lab

Research and prototype project exploring **Git-friendly, deterministic data formats for Maya asset data**.

## Overview

This project focuses on externalizing Maya data (UVs, skin weights, proxy meshes, etc.) into structured formats that are:

* deterministic
* versionable
* decoupled from Maya scene files

The goal is to make asset data easier to:

* track in Git
* validate
* update later in the pipeline without rebuilding rigs

---

## Current Scope

Initial development is focused on:

* UV export/import
* topology validation
* JSON-based data representation

Future areas may include:

* skinCluster weight data
* proxy mesh data
* generalized data contracts for rigging pipelines

---

## Project Structure

```text
src/maya_data_lab/
    uv/
        exporter.py
        importer.py
        models.py

examples/
    uv/
        sample_uv_data.json
```

* `src/` → core library code
* `examples/` → reference data and schema examples

---

## Goals

* Define clear data contracts for Maya asset data
* Ensure deterministic output for Git-friendly diffs
* Separate data from scene state
* Enable safe re-application of data later in the pipeline

---

## Status

🚧 Early prototype / R&D

This project is under active exploration. The data formats and structure are expected to evolve.

---

## Notes

* This is not intended to replace Maya scene files
* Instead, it focuses on **externalizing specific data layers** (UVs, weights, etc.)
* Topology consistency is assumed for re-application workflows

---

## License

MIT
