from termcolor import colored
import datetime

LOG_MODES = {
    "WARNING": "yellow",
    "INFO": "blue",
    "SUCCESS": "green",
    "FAILURE": "red",
    "CRITICAL": "grey"
}


class log:

    def __init__(self, terminal_only=True, logfile=None) -> None:
        self.logfile = logfile
        self.terminal_only = terminal_only

    def INFO(self, message):
        _timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_statement = f"[{_timestamp}] INFO : {message}"
        print(colored(text=log_statement, color=LOG_MODES["INFO"]))

    def WARN(self, message):
        _timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_statement = f"[{_timestamp}] WARNING : {message}"
        print(colored(text=log_statement, color=LOG_MODES["WARNING"]))

    def SUCCESS(self, message):
        _timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_statement = f"[{_timestamp}] SUCCESS : {message}"
        print(colored(text=log_statement, color=LOG_MODES["SUCCESS"]))

    def FAILURE(self, message):
        _timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_statement = f"[{_timestamp}] FAILURE : {message}"
        print(colored(text=log_statement, color=LOG_MODES["FAILURE"]))

    def CRITICAL(self, message):
        _timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_statement = f"[{_timestamp}] CRITICAL : {message}"
        print(colored(text=log_statement, color=LOG_MODES["CRITICAL"], on_color="on_red"))


# log = log()

# log.INFO("Table Created")
# log.WARN("Table Created")
# log.SUCCESS("Table Created")
# log.FAILURE("Table Created")
# log.CRITICAL("Table Created")

# # _timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# # print(f"[{_timestamp}] INFO : authProfiles_dev Table Created! ")
