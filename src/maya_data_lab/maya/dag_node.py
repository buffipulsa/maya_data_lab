
import logging

import maya.api.OpenMaya as om

import maya_data_lab.maya.dependency_node as dependency_node

logger = logging.getLogger(__name__)

class DagNodeHandle(dependency_node.DependencyNodeHandle):
    """
    Lightweight wrapper around a Maya DAG node.

    This class extends `DependencyNodeHandle` by validating that the resolved
    node is part of the DAG and by exposing both an `MDagPath` and an
    `MFnDagNode` for querying DAG-specific information using the Maya Python
    API 2.0.

    This avoids repeated boilerplate when validating DAG nodes and constructing
    DAG function sets.

    Parameters
    ----------
    node_name : str
        Name of the Maya node to resolve.

    Raises
    ------
    ValueError
        If the node cannot be resolved or if the resolved node is not a DAG node.

    Examples
    --------
    >>> node = DagNodeHandle("pCube1")
    >>> node.dag_fn.fullPathName()
    '|pCube1'
    """
    def __init__(self, node_name: str) -> None:
        super().__init__(node_name)
        
        logger.debug('Creating DagNodeHandle for node "%s"', node_name)
        
        if not self.m_object.hasFn(om.MFn.kDagNode):
            raise ValueError(f'Node "{node_name}" is not a DAG node.')
        
        self._dag_path = om.MDagPath.getAPathTo(self.m_object)
        self._dag_fn = om.MFnDagNode(self._dag_path)
        
        logger.debug('Resolved DagNodeHandle for node "%s"', node_name)
        
    @property
    def dag_path(self) -> om.MDagPath:
        """
        Return the DAG path for the wrapped node.

        Returns
        -------
        om.MDagPath
            The DAG path associated with the node.
        """
        return self._dag_path
    
    @property
    def dag_fn(self) -> om.MFnDagNode:
        """
        Return the DAG function set for the wrapped node.

        Returns
        -------
        om.MFnDagNode
            Function set used to query DAG-specific properties such as
            hierarchy, path, and child relationships.
        """
        return self._dag_fn