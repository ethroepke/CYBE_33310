  GNU nano 6.2                                                             part03_drug_trial_researcher_skel.py                                                                       
# Lab 12 part 03
# Now you have received the encrypted averages back from your work in the cloud.
# You now want to decrypt them to share the results with the FDA in an attempt
# to get your drug to the health care market.
# Of course, you have the private key because you created it before you encrypted
# the data with the public key.

from phe import paillier
import pickle

# Load the private key
with open('privateKey.pkl', 'rb') as f:
    privateKey = pickle.load(f)

# Load the encrypted averages
with open('encryptedAverages.pkl', 'rb') as f:
    encryptedAverages = pickle.load(f)

# TODO:
# Decrypt the averages.  This can be accomplished using the decrypt() method
# privateKey.decrypt() will be useful to you.  
decryptedAverages = [privateKey.decrypt(avg) for avg in encryptedAverages]

print("Decrypted averages:", decryptedAverages)

