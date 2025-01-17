
import os
import ipfshttpclient

class GlobalConfig:
    # PostgreSQL Configuration
    POSTGRES_DB = os.getenv('POSTGRES_DB', 'default_db')
    POSTGRES_USER = os.getenv('POSTGRES_USER', 'user')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)
    
    # IPFS Configuration
    IPFS_API = os.getenv('IPFS_API', '/dns/localhost/tcp/5001/http')

    @staticmethod
    def init_postgres():
        from sqlalchemy import create_engine
        engine = create_engine(
            f"postgresql://{GlobalConfig.POSTGRES_USER}:"
            f"{GlobalConfig.POSTGRES_PASSWORD}@"
            f"{GlobalConfig.POSTGRES_HOST}:{GlobalConfig.POSTGRES_PORT}/"
            f"{GlobalConfig.POSTGRES_DB}"
        )
        return engine

    @staticmethod
    def init_ipfs():
        try:
            client = ipfshttpclient.connect(GlobalConfig.IPFS_API)
            return client
        except ipfshttpclient.exceptions.ConnectionError:
            print("Failed to connect to IPFS. Ensure the IPFS daemon is running.")
            return None
