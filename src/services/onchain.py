from web3 import Web3


async def is_valid_address(address: str) -> bool:
    return Web3.isAddress(address)
