import sqlite3
from datetime import datetime

from loguru import logger


class Database:

    def __init__(self):
        logger.remove()
        self.logger = logger.add(
            'database.log',
            format='{time}:{level}:{message}'
        )
        self.connection = sqlite3.connect(database='database.sql')
        self.connection.cursor().execute("""CREATE TABLE IF NOT EXISTS "users"
                                            ("user_id"	INTEGER NOT NULL UNIQUE,
                                            "date"	TEXT NOT NULL,
                                            "language"	TEXT)""")
        self.connection.cursor().execute("""CREATE TABLE IF NOT EXISTS "wallets"
                                            ("user_id" INTEGER NOT NULL,
                                            "address"	TEXT NOT NULL,
                                            "label"	TEXT)""")
        self.connection.commit()

    async def execute(
            self,
            sql: str,
            params: tuple,
            method: str,
            fetchone: bool = False,
            fetchall: bool = False
    ):
        cursor = self.connection.cursor()
        data = None

        try:
            cursor.execute(sql, params)
            self.connection.commit()
        except sqlite3.Error:
            logger.error(f'{method} error')

        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        return data

    async def signup(self, user_id: int, registration_date: datetime):
        sql = """INSERT INTO users (user_id, date) VALUES (?, ?);"""
        params = (user_id, registration_date)
        await self.execute(sql, params, ' sign up')
        logger.info(f'[{user_id}]: just signed up')

    async def remove(self, user_id: int):
        sql = """DELETE FROM users WHERE user_id = ?"""
        params = (user_id,)
        await self.execute(sql, params, ' user removing')
        logger.info(f'[{user_id}]: successfully removed')
        await self.remove_all_addresses(user_id)

    async def is_user_registered(self, user_id: int) -> bool:
        sql = """SELECT * FROM users WHERE user_id = ?"""
        params = (user_id,)
        result = await self.execute(
            sql, params, ' sign up check', fetchone=True
        )
        return result if result else False

    async def set_language(self, user_id: int, language: str):
        sql = """UPDATE users SET language = ? WHERE user_id = ?"""
        params = (language, user_id)
        await self.execute(sql, params, ' language setting')
        logger.info(f'[{user_id}]: set language -> [{language}]')

    async def get_user_language(self, user_id: int) -> str:
        sql = """SELECT language FROM users WHERE user_id = ?"""
        params = (user_id,)
        result = await self.execute(
            sql, params, ' user language getting', fetchone=True
        )
        if result:
            return result[0]

    async def add_wallet_address(self, user_id: int, address: str):
        sql = """INSERT INTO 'wallets' (user_id, address) VALUES (?, ?)"""
        params = (user_id, address)
        await self.execute(sql, params, ' address adding error')
        logger.info(f'[{user_id}]: new wallet address -> [{address}]')

    async def set_address_label(self, user_id: int, address: str, label: str):
        sql = """UPDATE 'wallets' SET label = ? WHERE (user_id, address)
        = (?, ?)"""
        params = (label, user_id, address)
        await self.execute(sql, params, ' label setting')
        logger.info(f'[{user_id}]: set [{label}] label for [{address}]')

    async def get_address_label(self, user_id: int, address: str) -> str:
        sql = """SELECT label FROM 'wallets' WHERE (user_id, address)
        = (?, ?)"""
        params = (user_id, address)
        result = await self.execute(
            sql, params, ' address label getting', fetchone=True
        )
        return result[0] if result else None

    async def is_pair_exists(self, user_id: int, address: str) -> bool:
        sql = """SELECT * FROM 'wallets' WHERE (user_id, address) = (?, ?)"""
        params = (user_id, address)
        return await self.execute(sql, params, ' pair check', fetchone=True)

    async def get_address_list(self, user_id: int) -> list:
        sql = """SELECT * FROM 'wallets' WHERE user_id = ?"""
        params = (user_id,)
        result = await self.execute(
            sql, params, ' address list getting', fetchall=True
        )
        return result if result else None

    async def count_user_addresses(self, user_id: int) -> int:
        result = await self.get_address_list(user_id)
        return len(result) if result else 0

    async def remove_address(self, user_id: int, address: str):
        sql = """DELETE FROM 'wallets' WHERE (user_id, address) = (?, ?)"""
        params = (user_id, address)
        await self.execute(sql, params, ' address removing')
        logger.info(f'[{user_id}]: address successfully removed -> [{address}]')

    async def remove_all_addresses(self, user_id: int):
        sql = """DELETE FROM 'wallets' WHERE user_id = ?"""
        params = (user_id,)
        await self.execute(sql, params, ' addresses removing')
        logger.info(f'[{user_id}]: all addresses successfully removed')


db = Database()
