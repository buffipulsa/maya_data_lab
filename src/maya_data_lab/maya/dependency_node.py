
import logging

import maya.api.OpenMaya as om

logger = logging.getLogger(__name__)

class DependencyNodeHandle:
    
    def __init__(self, node_name: str):
        
        if not node_name:
            raise TypeError('Please specify a node name.')
        
        logger.debug('Creating DependencyNodeHandle for node "%s"', node_name)
        
        self._m_object = self._resolve_m_object(node_name)
        self._dependency_fn = om.MFnDependencyNode(self._m_object)
        
        logger.debug('Resolved DependencyNodeHandle for node "%s"', node_name)
        
    def _resolve_m_object(self, node_name:str) -> om.MObject:
        
        selection_list = om.MSelectionList()
        
        try:
            m_object = selection_list.add(node_name).getDependNode(0)
            
            return m_object
        
        except RuntimeError as error:
            raise ValueError(f'No valid node found for {node_name}') from error
        
    @property
    def m_object(self) -> om.MObject:
        
        return self._m_object

    @property
    def dependency_fn(self) -> om.MFnDependencyNode:
        
        return self._dependency_fn