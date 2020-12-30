import os


class Validation:
    """Validation class to validate the input"""

    def validation(self, data) -> dict:
        # Validating From
        if "from_email" not in data.keys() or data["from_email"] == "":
            status = {
                "status_code": 400,
                "message": "Missing required parameter - from or field is empty",
            }
            return status

        # Validating Subject
        if "subject" not in data.keys() or data["subject"] == "":
            status = {
                "status_code": 400,
                "message": "Missing required parameter - subject or Invalid subject passed",
            }
            return status

        # Validating html_body and text_body
        if "html_body" not in data.keys() or data["html_body"] == "":
            if "text_body" not in data.keys() or data["text_body"] == "":
                status = {
                    "status_code": 400,
                    "message": "Missing required parameter - html body or text body or field is empty",
                }
                return status

        # Validating Receipients
        if "receipients" not in data.keys() or "to" not in data["receipients"].keys():
            status = {
                "status_code": 400,
                "message": "Missing required parameter - receipients or field is empty",
            }
            return status

        return {
            "status_code": 200,
            "message": "Validation Passed",
        }

    def file_existnece(self, data):
        """Checking for the existence of the attachements"""
        for single_file in data:

            # Skipping for the calendar invite
            if single_file.split(".")[-1] == "ics":
                pass

            if os.path.exists(single_file) and os.path.isfile(single_file):
                pass
            else:
                raise FileNotFoundError(f"{single_file} not found")
        return
