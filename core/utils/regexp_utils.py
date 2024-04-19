import re


class RegExpUtils:

    @staticmethod
    def match_and_return_group(text: str, pattern: str, group_number: int) -> tuple:

        matches = re.search(pattern, text)

        result = ()
        if matches:
            result = matches.groups()[:group_number]

        return result

