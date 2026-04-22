
import logging

import maya.cmds as cmds

import maya_data_lab.logging_utils as logging_utils

logger = logging.getLogger(__name__)

def initialize() -> None:
    logging_utils.configure_logging(logging.INFO)

    cmds.scriptEditorInfo(
        suppressInfo=True,
        suppressWarnings=False,
        suppressErrors=False,
        suppressResults=True,
    )
    
    logger.info('maya_data_lab startup initialized')