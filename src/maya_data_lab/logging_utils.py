import logging

def configure_logging(log_level: int = logging.INFO) -> None:
    
    root_logger = logging.getLogger('maya_data_lab')
    
    root_logger.setLevel(log_level)
    
    if not root_logger.handlers:
        stream_handler = logging.StreamHandler()
        
        formatter = logging.Formatter(
            fmt='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        )
        stream_handler.setFormatter(formatter)
        
        root_logger.addHandler(stream_handler)
    
    for handler in root_logger.handlers:
        handler.setLevel(log_level)

    root_logger.propagate = False
    