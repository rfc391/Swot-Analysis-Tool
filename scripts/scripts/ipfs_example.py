
import ipfshttpclient

def upload_to_ipfs(file_path):
    """
    Uploads a file to IPFS and returns the CID.
    """
    try:
        client = ipfshttpclient.connect('/dns/localhost/tcp/5001/http')
        response = client.add(file_path)
        print(f"File uploaded to IPFS: {response['Hash']}")
        return response['Hash']
    except Exception as e:
        print(f"Error uploading to IPFS: {e}")
        return None

def retrieve_from_ipfs(cid, output_path):
    """
    Retrieves a file from IPFS using the CID and saves it to the specified path.
    """
    try:
        client = ipfshttpclient.connect('/dns/localhost/tcp/5001/http')
        client.get(cid, target=output_path)
        print(f"File retrieved from IPFS and saved to: {output_path}")
    except Exception as e:
        print(f"Error retrieving from IPFS: {e}")

# Example Usage
if __name__ == "__main__":
    file_path = "example.txt"  # Replace with your file path
    output_path = "retrieved_example.txt"
    cid = upload_to_ipfs(file_path)
    if cid:
        retrieve_from_ipfs(cid, output_path)
