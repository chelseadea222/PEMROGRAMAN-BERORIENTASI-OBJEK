# Data klinik
data_klinik = {
    "nama_klinik": "Klinik Informatika Sehat",
    "rekam_medis": [
        {"id": 1, "bpm": 70},
        {"id": 2, "bpm": 110},
        {"id": 3, "bpm": 65},
        {"id": 4, "bpm": 120},
        {"id": 5, "bpm": 80},
        {"id": 6, "bpm": 140},
        {"id": 7, "bpm": 75}
    ]
}

# Function untuk analisa kondisi
def analisa_kondisi(bpm):
    if bpm > 100:
        return "Peringatan: Takikardia (Detak Tinggi)"
    else:
        return "Kondisi: Normal"

# Iterasi untuk memproses data rekam medis
print("=== Sistem Monitoring Kesehatan ===")
print(f"Klinik: {data_klinik['nama_klinik']}\n")

for pasien in data_klinik["rekam_medis"]:
    status = analisa_kondisi(pasien["bpm"])
    print(f"Data ke-{pasien['id']}: {pasien['bpm']} BPM -> {status}")