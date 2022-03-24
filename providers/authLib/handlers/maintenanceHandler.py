import json
import datetime

from configPy import JSONConfigParser
from logsmith import log

# Import Configurations
configObject = JSONConfigParser(configFilePath=".configs/datafiles.config.json")
configurations = configObject.getConfigurations()

# Initiate Logging
log = log()
log.configure(console_only=True, ENV="Dev")

# JSON Writer Function
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


class MAINTENANCE:

    __authlib = {}

    def __init__(self) -> None:
        with open(configurations["authlib-store"]) as authlibObject:
            self.__authlib = json.load(authlibObject)

    # Purge Un-verified AuthLib Profiles with over [60]-Days of Activity
    def long_term_purge(self):
        for mail_id in list(self.__authlib):
            self.requestTimestamp = datetime.datetime.fromisoformat(self.__authlib[mail_id]["requestTimestamp"])
            self.currentTimestamp = datetime.datetime.now(tz=datetime.timezone.utc)

            self.timespan = self.currentTimestamp - self.requestTimestamp
            
            if self.timespan.days >= configurations["long-term-purge-timespan"]:
                del self.__authlib[mail_id]
                write_json(self.__authlib, configurations["authlib-store"])
            else:
                pass

    # Delete the Hashed Secret and Timestamp of Request 
    def short_term_purge():

        pass
