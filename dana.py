def hitung_biaya_admin(nominal, persen):
    return nominal * persen / 100

def validasi_nominal(nominal,min_nominal, max_nominal):
    return min_nominal <= nominal <= max_nominal

def validasi_nomor_tujuan(nomor):
    return nomor.isdigit() and 10 <= len(nomor) <= 15

print(hitung_biaya_admin(100000, 2))  
print(validasi_nominal(50000, 10000, 1000000))
print(validasi_nomor_tujuan("081234567890"))

# Biaya admin transaksi
def fitur_topup_bank(nominal):
    admin = hitung_biaya_admin(nominal, 1.5)
    total = nominal + admin
    return f"Total top up: {total}, admin: {admin}"

# Tarik tunai
def fitur_tarik_tunai(nominal):
    admin = hitung_biaya_admin(nominal, 2.0)
    total = nominal + admin
    return f"Total tarik tunai: {total}, admin: {admin}"

# Validasi nomor tujuan kirim uang
def fitur_kirim_uang(nomor):
    if validasi_nomor_tujuan(nomor):
        return "Nomor valid. Proses lanjut."
    return "Nomor tujuan tidak valid."

# Validasi nomor tujuan top up pulsa/data
def fitur_topup_pulsa(nomor):
    if validasi_nomor_tujuan(nomor):
        return "Nomor pulsa valid."
    return "Nomor tidak valid untuk pulsa."

# Validasi nominal top up
def fitur_nominal_topup(nominal):
    if validasi_nominal(nominal, 10000, 2000000):
        return "Nominal top up valid."
    return "Nominal di luar batas."

# Validasi nominal tarik tunai
def fitur_nominal_tarik_tunai(nominal):
    if validasi_nominal(nominal, 50000, 1000000):
        return "Nominal tarik tunai valid."
    return "Nominal tidak sesuai aturan."
