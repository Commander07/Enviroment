from enviroment import Enviroment, Level
ENV = Enviroment("ENV", logger_level=Level.DEBUG)
ENV.logger.debug("DEBUG")
ENV.logger.info("INFO")
ENV.logger.warning("WARNING")
ENV.logger.error("ERROR")
ENV.logger.critical("CRITICAL")
ENV.console.print("[cyan bold]Hello, World!")
