# 📊 Eksperimen dan Preprocessing Dataset Mental Health

Repository ini berisi proses eksperimen dan preprocessing data untuk proyek prediksi kebutuhan perawatan kesehatan mental di lingkungan kerja.** Dataset yang digunakan berasal dari survei global tentang kesehatan mental di tempat kerja.

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk membersihkan dan menyiapkan dataset **mental health in tech workplace** agar dapat digunakan dalam pembuatan model machine learning.

Tahapan yang dilakukan meliputi:

1. Eksplorasi Data Awal (EDA)
2. Pra-pemrosesan Dataset (Preprocessing)
3. Pembuatan Dataset Siap Latih

Hasil akhir dari proyek ini berupa dataset yang telah bersih dan siap digunakan untuk **training model machine learning**.

---

## 📁 Struktur Folder

```
Eksperimen_Nabila-Febriyanti-Valentinn/
├── .workflow/                  # (opsional, untuk integrasi lanjutan)
├── namadataset_raw/            # Dataset mentah/raw (opsional)
├── preprocessing/
│   ├── Eksperimen_Nabila-Febriyanti-Valentin.ipynb  # Eksplorasi & preprocessing manual
│   ├── automate_Nabila-Febriyanti-Valentin.py       # Automatisasi preprocessing (Skilled)
│   └── mental_health_cleaned.csv                    # Dataset hasil preprocessing
└── README.md
```

---

## 📦 Dataset

Dataset yang digunakan adalah hasil survei online mengenai kesehatan mental di lingkungan kerja, dengan fitur-fitur sebagai berikut:

| Fitur                       | Deskripsi                                                      |
| --------------------------- | -------------------------------------------------------------- |
| `Age`                       | Usia responden                                                 |
| `Gender`                    | Jenis kelamin                                                  |
| `self_employed`             | Apakah wiraswasta                                              |
| `family_history`            | Ada riwayat keluarga terkait kesehatan mental                  |
| `treatment`                 | **Target** → Apakah pernah mendapat perawatan kesehatan mental |
| `work_interfere`            | Pengaruh kesehatan mental terhadap pekerjaan                   |
| `no_employees`              | Jumlah karyawan di tempat kerja                                |
| `remote_work`               | Bekerja remote atau tidak                                      |
| `tech_company`              | Apakah bekerja di perusahaan teknologi                         |
| `benefits`                  | Apakah perusahaan menyediakan fasilitas kesehatan mental       |
| `care_options`              | Tersedia atau tidak pilihan perawatan                          |
| `wellness_program`          | Apakah perusahaan punya program kesehatan mental               |
| `seek_help`                 | Kemudahan mencari bantuan terkait kesehatan mental             |
| `anonymity`                 | Privasi karyawan terkait masalah kesehatan mental              |
| `leave`                     | Kemudahan cuti untuk alasan kesehatan mental                   |
| `mental_health_consequence` | Dampak kesehatan mental terhadap karir                         |
| `phys_health_consequence`   | Dampak kesehatan fisik terhadap karir                          |
| `coworkers`                 | Nyaman berbicara dengan rekan kerja terkait kesehatan mental   |
| `supervisor`                | Nyaman berbicara dengan atasan terkait kesehatan mental        |
| `mental_health_interview`   | Nyaman bicara soal mental health saat interview kerja          |
| `phys_health_interview`     | Nyaman bicara soal kesehatan fisik saat interview              |
| `mental_vs_physical`        | Apakah mental health diperlakukan setara fisik health          |
| `obs_consequence`           | Pernah mengalami konsekuensi terkait masalah mental health     |

📌 **Target**: `treatment`

---

## ⚙️ Cara Menjalankan Automatisasi Preprocessing

1️⃣ **Clone Repository**

```bash
git clone https://github.com/nfvalenn/Eksperimen_Nabila-Febriyanti-Valentinn.git
cd Eksperimen_Nabila-Febriyanti-Valentinn/preprocessing
```

2️⃣ **Jalankan Automatisasi Preprocessing**

```bash
python automate_Nabila-Febriyanti-Valentin.py
```

3️⃣ **Hasil Output**

* Dataset hasil preprocessing akan tersimpan sebagai [mental_health_cleaned.csv](https://github.com/nfvalenn/Eksperimen_Nabila-Febriyanti-Valentinn/blob/main/preprocessing/mental_health_cleaned.csv)

---

## 📚 Referensi Dataset

* [Original Dataset - Mental Health in Tech Survey](https://www.kaggle.com/osmi/mental-health-in-tech-survey)

---

## 👩‍💻 Author

**Nabila Febriyanti Valentin**
Dicoding ID: nfvalen02
