
import requests

def download_audio(url, output_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()  
    with open(output_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print("File downloaded successfully.")

# Example usage:
url = "https://media.ringba.com/recording-public?v=v1&k=QCjI3TVCUf9F4qkdwM9tju%2f6uxqNuMyd6dtESxMHrJ7MaAmAEs72f9TDkHKgitjeMViWBzoyZ5NxYg45Au32LKNqHV21v%2fWq8EO%2fcMh5KE%2bNhqr4aHlrzUvqv2my9kyTymLnnQvobITSRa8MPtDXBfT0b252tOgnEOEoeQ7YFQMmFf6vR325D%2b2YYRX7KKYzc1PS3TxmtdBBGE8keUCa7umvznIpEkrhfWCBfeyOJXd3E%2ba4s9v4ckniIVmfSj6JfQUyduVaFln7m%2fGkbpO3ASKgNpc%3d"  # Replace with the actual URL of the audio file
output_path = "/content/sample_data/audio.mp3"  # Replace with the desired output path and file name

download_audio(url, output_path)

!whisper /content/sample_data/audio.mp3 --model large
output_path2 = "/content/audio.txt"
with open(output_path2, "r") as file:
    file_contents = file.read()

print(file_contents)
