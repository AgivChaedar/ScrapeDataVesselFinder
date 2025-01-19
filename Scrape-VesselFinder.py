from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Tentukan situs web dan path ke chromedriver
website = 'https://www.vesselfinder.com/vessels'
path = 'C:\\Users\\agivc\\Downloads\\chromedriver.exe'

# Setup Service dan driver
service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# Tunggu hingga elemen pertama (tabel) tersedia
WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr')))

# Daftar untuk menyimpan data kapal
vessels_data = []
num_pages_to_scrape = 10  # Jumlah halaman yang akan diambil datanya

for page in range(num_pages_to_scrape):
    print(f"Mengambil data dari halaman {page + 1}...")
    
    # Dapatkan ulang elemen kapal untuk menghindari "stale element reference"
    ships = driver.find_elements(By.CSS_SELECTOR, 'tr')
    
    for i in range(len(ships)):
        try:
            # Refresh elemen kapal untuk setiap iterasi
            ships = driver.find_elements(By.CSS_SELECTOR, 'tr')
            ship = ships[i]

            # Ambil nama dan tipe kapal
            vessel_name = ship.find_element(By.CLASS_NAME, 'slna').text if ship.find_elements(By.CLASS_NAME, 'slna') else ''
            vessel_type = ship.find_element(By.CLASS_NAME, 'slty').text if ship.find_elements(By.CLASS_NAME, 'slty') else ''
            
            # Ambil tautan untuk detail kapal
            link_element = ship.find_element(By.CSS_SELECTOR, 'a.ship-link') if ship.find_elements(By.CSS_SELECTOR, 'a.ship-link') else None
            
            if link_element:
                # Navigasi ke halaman detail kapal
                driver.get(link_element.get_attribute('href'))
                WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CLASS_NAME, 'aparams')))
                
                # Ambil detail informasi kapal
                details = {row.find_element(By.CLASS_NAME, 'n3').text: row.find_element(By.CLASS_NAME, 'v3').text 
                           for row in driver.find_elements(By.CSS_SELECTOR, '.aparams tr')}
                
                # Simpan data kapal ke daftar vessels_data
                vessels_data.append({
                    "Nama Kapal": vessel_name,
                    "Tipe Kapal": vessel_type,
                    "Prediksi ETA": details.get('Predicted ETA', '-'),
                    "Jarak / Waktu": details.get('Distance / Time', '-'),
                    "Arah / Kecepatan": details.get('Course / Speed', '-'),
                    "Draught Saat Ini": details.get('Current draught', '-'),
                    "Status Navigasi": details.get('Navigation Status', '-'),
                    "Posisi Diterima": details.get('Position received', '-'),
                    "IMO / MMSI": details.get('IMO / MMSI', '-'),
                    "Panggilan Sinyal": details.get('Callsign', '-'),
                    "Bendera": details.get('Flag', '-'),
                    "Panjang / Lebar": details.get('Length / Beam', '-'),
                })

                # Kembali ke halaman daftar kapal
                driver.back()
                WebDriverWait(driver, 25).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr')))
        
        except Exception as e:
            print(f"Kesalahan saat memproses kapal: {e}")

    # Klik tombol "Berikutnya" untuk ke halaman berikutnya
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'a.pagination-next')
        next_button.click()
        WebDriverWait(driver, 25).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'tr')))
    except Exception as e:
        print("Tidak ada halaman berikutnya atau ada kesalahan saat klik tombol berikutnya:", e)
        break

# Tutup browser
driver.quit()

# Simpan hasil ke CSV
df = pd.DataFrame(vessels_data)
df.to_csv("C:/Users/agivc/Downloads/vessel_detail_data_10hlmnew.csv", index=False)
print("Data berhasil disimpan ke vessel_detail_data_10hlmnew.csv")
