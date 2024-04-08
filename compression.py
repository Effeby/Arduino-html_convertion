import gzip

def compress_html_to_arduino_code(file_path):
    with open(file_path, 'rb') as file:
        html_content = file.read()

    compressed_data = gzip.compress(html_content)

    print("#define index_html_gz_len {}".format(len(compressed_data)))
    print("const uint8_t index_html_gz[] = {")
    for i in range(0, len(compressed_data), 12):
        print("  " + ", ".join("0x{:02X}".format(b) for b in compressed_data[i:i+12]) + ",")
    print("};")

    # Appeler la fonction avec le chemin du fichier HTML
# Vous devez mettre le nom du fichier html a compresser en arduino dans les doubles cotes
compress_html_to_arduino_code("codeWeb.html")
