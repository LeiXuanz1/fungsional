# dana_utils/validator.py

def validasi_nominal(nominal, min_nominal, max_nominal):
    return min_nominal <= nominal <= max_nominal

def validasi_nomor_tujuan(nomor):
    return nomor.isdigit() and 10 <= len(nomor) <= 15