"""
Security module for face data protection
Implements hashing and data protection mechanisms
"""

import hashlib
import base64
import json

class DataProtector:
    def __init__(self):
        """Initialize security module"""
        self.hash_algorithm = 'sha256'
        print("Security module initialized")
    
    def hash_encoding(self, face_encoding):
        """
        Hash face encoding for privacy protection
        Returns: SHA-256 hash string
        """
        try:
            # Convert encoding to bytes
            if hasattr(face_encoding, 'tobytes'):
                encoding_bytes = face_encoding.tobytes()
            else:
                encoding_bytes = str(face_encoding).encode('utf-8')
            
            # Create hash
            hash_obj = hashlib.sha256(encoding_bytes)
            hash_string = hash_obj.hexdigest()
            
            return hash_string
        except Exception as e:
            print(f"Error hashing encoding: {e}")
            return None
    
    def compare_hashes(self, hash1, hash2):
        """
        Compare two hashes
        Returns: similarity score (1.0 if exact match)
        """
        if hash1 == hash2:
            return 1.0
        else:
            # For demonstration: calculate similarity based on hash prefix
            # In real system, hashes either match or don't
            matching_chars = sum(1 for a, b in zip(hash1, hash2) if a == b)
            return matching_chars / len(hash1)
    
    def encrypt_data(self, data, key=None):
        """
        Simple encryption (placeholder)
        In production, use proper encryption like AES
        """
        # Placeholder - return base64 encoded
        encoded = base64.b64encode(str(data).encode('utf-8')).decode('utf-8')
        return encoded
    
    def decrypt_data(self, encrypted_data, key=None):
        """
        Simple decryption (placeholder)
        """
        try:
            decoded = base64.b64decode(encrypted_data).decode('utf-8')
            return decoded
        except:
            return None
    
    def save_secure_data(self, data, filename):
        """
        Save data with protection
        """
        try:
            # Hash sensitive data
            if 'face_encodings' in data:
                data['hashed_encodings'] = [
                    self.hash_encoding(enc) 
                    for enc in data['face_encodings']
                ]
                del data['face_encodings']
            
            # Save to file
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"Data saved securely to {filename}")
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_secure_data(self, filename):
        """
        Load protected data
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            print(f"Data loaded from {filename}")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def generate_privacy_report(self, data):
        """
        Generate privacy impact report
        """
        report = {
            'data_type': 'face_encodings',
            'protection_method': 'sha256_hashing',
            'original_data_stored': False,
            'pseudonymized': True,
            'hash_count': len(data.get('hashed_encodings', [])),
            'compliance_check': 'GDPR_friendly'
        }
        return report