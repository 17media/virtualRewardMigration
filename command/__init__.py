import datetime
from abc import abstractmethod, ABC


class Command(ABC):
    @abstractmethod
    def process(self):
        pass


def _save_to_file(fail_style_ids, style_type):
    if len(fail_style_ids) > 0:
        with open(f"{datetime.datetime.now().isoformat()}_{style_type}_err.csv", "w") as errFile:
            errFile.writelines("\n".join(fail_style_ids))
