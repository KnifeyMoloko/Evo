"""
main file for the app orchestration
"""
import logging
import logging.config as logging_cfg
from helpers import general
from app import create_app


def main():
    # general app configuration
    # Logger configuration
    config = general.get_config()
    log_path = config.get("root") / 'logs'

    # create logs directory if not present
    log_path.mkdir(mode=0o755, parents=True, exist_ok=True)

    # load the logger configuration from the configuration file
    logging_cfg.fileConfig(config.get("cfg_path"), disable_existing_loggers=False)

    # initialize logger
    logger = logging.getLogger(__name__)

    # create app instance for dev, test or prod
    app = create_app(config.get("cfg"))

    logger.info("Running app")
    # here is where the actual app instructions will be
    return True


if __name__ == "__main__":
    main()
