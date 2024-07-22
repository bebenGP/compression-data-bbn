import os
import shutil
import zipfile

print("Script ini menggunakan library shutil\nSebaiknya file yang di compress menjadi ZIP yaitu foldering\ndisarankan tidak langsung mengcompress sebuah data yang sifatnya adalah file")

def main() :
    source_folder = str(input("Lokasi/path Data yang ingin di compress : "))
    output_folder = str(input("Lokasi Output log status hasil compress data (untuk checking/tracking data : "))
    daftar_item = os.path.join(output_folder, "data_compress.txt")
    error_log = os.path.join(output_folder, "error_log.txt")

    # Membuat folder output jika belum ada
    os.makedirs(output_folder, exist_ok=True)

    # Membaca daftar semua item
    items = os.listdir(source_folder)

    # Menulis daftar item ke file teks
    with open(daftar_item, 'w') as file_success, open(error_log, 'w') as file_error:
        file_success.write("Daftar item yang telah di-zip:\n")
        file_success.flush()
        os.fsync(file_success.fileno())
        
        file_error.write("Daftar item yang gagal di-zip:\n")
        file_error.flush()
        os.fsync(file_error.fileno())
        
        for item in items:
            item_path = os.path.join(source_folder, item)
            zip_path = os.path.join(source_folder, item + '.zip')
            
            try:
                if os.path.isdir(item_path):
                    # Jika item adalah folder
                    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', item_path)
                else:
                    # Jika item adalah file
                    with zipfile.ZipFile(zip_path, 'w') as zipf:
                        zipf.write(item_path, arcname=item)
                
                # Menulis nama file ZIP ke file teks
                print(f"{zip_path} telah dibuat")
                file_success.write(zip_path + "\n")
                file_success.flush()
                os.fsync(file_success.fileno())
                
            except Exception as e:
                # Menulis item yang gagal di-zip ke file error log
                error_message = f"Gagal meng-zip {item}: {str(e)}"
                print(error_message)
                file_error.write(error_message + "\n")
                file_error.flush()
                os.fsync(file_error.fileno())

                # Menghapus file ZIP yang mungkin telah dibuat
                if os.path.exists(zip_path):
                    os.remove(zip_path)

    print(f"Daftar item telah disimpan ke {daftar_item}")
    print(f"Log error telah disimpan ke {error_log}")

if __name__ == "__main__" :
    main()
