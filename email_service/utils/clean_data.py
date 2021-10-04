class CleanMailingList:
    """Cleaning data before mailing it"""

    def __init__(self):
        pass

    @staticmethod
    def clean_mailing_list(data: dict) -> dict:
        """
        The function is used to clean up the data before sending mail
        :param data: dict
        :return: cleaned data -> dict
        """

        # Converting reply_to_addresses of string type to list of email addresses and removing spaces around the emails
        if "reply_to_addresses" in data.keys() and data["reply_to_addresses"]:
            data["reply_to_addresses"] = [
                email_id.strip() for email_id in data["reply_to_addresses"].split(",")
            ]

            # Removing empty strings
            data["reply_to_addresses"] = [
                email_id for email_id in data["reply_to_addresses"] if email_id
            ]

        else:
            data["reply_to_addresses"] = []

        # Making html_body None if nothing is provided
        if not data.get("html_body"):
            data["html_body"] = None

        # Making text_body None if nothing is provided
        if not data.get("text_body"):
            data["text_body"] = None

        # Handling keys to, cc, bcc
        if "to" not in data["recipients"].keys():
            data["recipients"]["to"] = []
        if "cc" not in data["recipients"].keys():
            data["recipients"]["cc"] = []
        if "bcc" not in data["recipients"].keys():
            data["recipients"]["bcc"] = []

        # Each email address in the personalization block should be unique between to, cc, and bcc
        # Priority order to > cc > bcc
        to_email_set = set()
        cc_email_set = set()
        bcc_email_set = set()
        for emails in data["recipients"]["to"]:
            to_email_set.add(tuple(emails.items()))
        for emails in data["recipients"]["cc"]:
            cc_email_set.add(tuple(emails.items()))
        for emails in data["recipients"]["bcc"]:
            bcc_email_set.add(tuple(emails.items()))
        data["recipients"]["to"] = [dict(email_id) for email_id in to_email_set]

        cc_email_set = cc_email_set - to_email_set
        data["recipients"]["cc"] = [dict(email_id) for email_id in cc_email_set]

        bcc_email_set = bcc_email_set - (cc_email_set.union(to_email_set))
        data["recipients"]["bcc"] = [dict(email_id) for email_id in bcc_email_set]

        return data
