from .logbase import logger
#

logger.create_log(logger_name="main.py", message="Application started running...", message_level="INFO")
from .app import Application
Application(logger)