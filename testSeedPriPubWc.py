from staking_deposit.key_handling.key_derivation.mnemonic import get_seed
from staking_deposit.key_handling.key_derivation.tree import derive_master_SK,derive_child_SK
from staking_deposit.key_handling.key_derivation.path import path_to_nodes
from staking_deposit.utils.crypto import SHA256
from py_ecc.bls import G2ProofOfPossession as bls
seed = get_seed(mnemonic="urban control nasty achieve upon beauty round casual apology front mosquito already pink hedgehog circle basket brief require buzz hospital three moral include attitude", password="")
print("seed",seed.hex())
sk = derive_master_SK(seed)
print("sk",sk)
purpose = '12381'
coin_type = '3600'
index = 0
account = str(index)
withdrawal_key_path = f'm/{purpose}/{coin_type}/{account}/0'
print("path",withdrawal_key_path)
for node in path_to_nodes(withdrawal_key_path):
    sk = derive_child_SK(parent_SK=sk, index=node)
print("final sk",sk)
pk = bls.SkToPk(sk)
print("pk",pk.hex())
BLS_WITHDRAWAL_PREFIX = bytes.fromhex('00')
withdrawal_credentials = BLS_WITHDRAWAL_PREFIX
withdrawal_credentials += SHA256(pk)[1:]
print("wc",withdrawal_credentials.hex())
