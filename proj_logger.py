import os
import sys
import logging
import traceback
from logging.handlers import RotatingFileHandler
from pathlib import Path
from datetime import datetime
from typing import Optional


__file_path = os.path.realpath(__file__)  # abs path to this script
__file_parent_dir = Path(__file_path).parent
__file_dirname = __file_parent_dir.name
__file_parent_dir = str(__file_parent_dir)
LOGS_DIRNAME = ".logs"
LOGS_DIR = os.path.join(__file_parent_dir, LOGS_DIRNAME)
assert os.path.exists(LOGS_DIR), f'Not exists: "{LOGS_DIR}". Create {LOGS_DIRNAME}/ directory by the path'

D_LOG_LEVEL = logging.DEBUG  # Default logging level


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    # DEFAULT VALUES:
    d_debug_clr = "\x1b[38;21m"  # grey (white)
    d_info_clr = "\x1b[94m"  # deep blue
    d_warning_clr = "\x1b[33;21m"  # yellow
    d_error_clr = "\x1b[31;21m"  # red
    d_critical_clr = "\x1b[31;1m"  # bold_red
    reset_clr = "\x1b[0m"
    d_message_format: Optional[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    d_datefmt: Optional[str] = None
    d_style: Optional[str] = '%'
    d_validate: bool = True

    def __init__(self, fmt: Optional[str] = None,
                 debug_clr: Optional[str] = None, info_clr: Optional[str] = None,
                 warning_clr: Optional[str] = None, error_clr: Optional[str] = None,
                 critical_clr: Optional[str] = None,
                 datefmt: Optional[str] = None, style: Optional[str] = '%', validate: Optional[bool] = None):
        if fmt is None:
            fmt = self.d_message_format
            style = self.d_style
        if debug_clr is None:
            debug_clr = self.d_debug_clr
        if info_clr is None:
            info_clr = self.d_info_clr
        if warning_clr is None:
            warning_clr = self.d_warning_clr
        if error_clr is None:
            error_clr = self.d_error_clr
        if critical_clr is None:
            critical_clr = self.d_critical_clr
        if validate is None:
            validate = self.d_validate

        self.FORMATS = {
            logging.DEBUG: debug_clr + fmt + self.reset_clr,
            logging.INFO: info_clr + fmt + self.reset_clr,
            logging.WARNING: warning_clr + fmt + self.reset_clr,
            logging.ERROR: error_clr + fmt + self.reset_clr,
            logging.CRITICAL: critical_clr + fmt + self.reset_clr,
        }
        # FIXME input params: logging.Formatter input value validate passing in not working
        logging.Formatter.__init__(self, fmt=fmt, datefmt=datefmt, style=style,
                                   # validate=validate
                                   )
        # print("self.d_formater after logging.Formatter.__init__(self, ...): ", self.d_formater)
        # self.d_formater = logging.Formatter(fmt=fmt, datefmt=datefmt, style=style)
        # print("self.d_formater after logging.Formatter(...): ", self.d_formater)

        self.FORMATERS = {
            logging.DEBUG: logging.Formatter(fmt=self.FORMATS[logging.DEBUG], datefmt=datefmt,
                                             style=style,
                                             # validate=validate
                                             ),
            logging.INFO: logging.Formatter(fmt=self.FORMATS[logging.INFO], datefmt=datefmt,
                                            style=style,
                                            # validate=validate
                                            ),
            logging.WARNING: logging.Formatter(fmt=self.FORMATS[logging.WARNING], datefmt=datefmt,
                                               style=style,
                                               # validate=validate
                                               ),
            logging.ERROR: logging.Formatter(fmt=self.FORMATS[logging.ERROR], datefmt=datefmt,
                                             style=style,
                                             # validate=validate
                                             ),
            logging.CRITICAL: logging.Formatter(fmt=self.FORMATS[logging.CRITICAL], datefmt=datefmt,
                                                style=style,
                                                # validate=validate
                                                ),
        }


def auto_exception_handlers(type, value, tb):
    for line in traceback.TracebackException(type, value, tb).format(chain=True):
        logging.exception(line)
    logging.exception(value)
    sys.__excepthook__(type, value, tb)  # calls default excepthook


# Install exception handler
sys.excepthook = auto_exception_handlers


def init_logger(log_level: Optional[str] = None, init_datetime: Optional[datetime] = None):
    if log_level is None:
        log_level = D_LOG_LEVEL
    if init_datetime is None:
        init_datetime = datetime.now()

    log_filename = f"{init_datetime.strftime('%Y-%m-%d_%H-%M-%S')}-{__file_dirname}.log"
    # Example of log_filename: "2021-10-24_07-02-00-rosatom_qvant.0.log"
    log_path = os.path.join(LOGS_DIR, log_filename)
    f_handler = RotatingFileHandler(filename=log_path, mode='a', maxBytes=10485760)
    save_formatter = logging.Formatter(
        fmt='[{asctime}]\t[{levelname}]\t{name}::{module}::{funcName}: {message}',
        datefmt=r'%Y-%m-%d %H:%M:%S', style='{')
    f_handler.setFormatter(save_formatter)
    f_handler.setLevel(log_level)
    # SETTING CONSOLE'S HANDLER AND FORMATTER:
    c_handler = logging.StreamHandler(stream=sys.stdout)  # console handler
    # c_formatter = logging.Formatter(
    #     fmt='[{levelname}]\t{module}::{funcName}: {message}',
    #     datefmt=r'%Y-%m-%d %H:%M:%S', style='{')
    c_formatter = CustomFormatter(
        fmt='[{levelname}]\t{module}::{funcName}: {message}',
        datefmt=r'%Y-%m-%d %H:%M:%S', style='{')
    c_handler.setFormatter(c_formatter)
    c_handler.setLevel(log_level)
    # custom_formatter = CustomFormatter(
    #     fmt=self.logging_format, datefmt=self.logging_datefmt, style=self.logging_style)
    # c_handler.setFormatter(custom_formatter)

    # ADDING HANDLERS TO LOGGER:
    # logger.addHandler(c_handler)
    # logger.addHandler(f_handler)
    # FIXME logging: should i configure root logger?
    logging.getLogger().addHandler(c_handler)  # setting to root logger
    logging.getLogger().addHandler(f_handler)  # setting to root logger
    logging.getLogger().setLevel(log_level)
    logging.info("End running of init_logger()")


init_logger()
