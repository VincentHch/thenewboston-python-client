from tnb.base_client import BaseClient


class Validator(BaseClient):
    def fetch_accounts(self):
        """
        Fetch accounts from validator
        Return response as a Python object
        """

        return self.fetch("/accounts")

    def fetch_account_balance(self, account_number):
        """
        Fetch account balance from account
        :param account_number: The account number of the account

        Return response as a Python object
        """

        return self.fetch(f"/accounts/{account_number}/balance")

    def fetch_account_balance_lock(self, account_number):
        """
        Fetch balance lock for account with number account_number
        :param account_number: The account number of the account

        Return response as a Python object
        """
        return self.fetch(f"/accounts/{account_number}/balance_lock")

    def fetch_confirmation_block(self, block_identifier):
        """
        Fetch confirmation block by block_identifier
        :param block_identifier: ID for the block

        Return response as Python object
        """

        return self.fetch(f"/confirmation_blocks/{block_identifier}/valid")
