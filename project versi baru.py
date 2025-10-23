# 🧠 AI Project Management System for Startup Digitalstreamlit run "project versi baru.py"

# Dibuat oleh: Agam Al Hakim Hasibuan
# Tema: Abstract Class & Interface dengan efek animasi (Streamlit)

import streamlit as st
import time
from abc import ABC, abstractmethod
import random

# === Abstract Class ===
class Project(ABC):
    def __init__(self, name, deadline, team_size):
        self.name = name
        self.deadline = deadline
        self.team_size = team_size
    
    @abstractmethod
    def project_info(self):
        pass
    
    @abstractmethod
    def calculate_efficiency(self):
        pass


# === Interface (AI Evaluator) ===
class AIEvaluator(ABC):
    @abstractmethod
    def evaluate_project(self):
        pass


# === Concrete Class ===
class AIProjectManager(Project, AIEvaluator):
    def __init__(self, name, deadline, team_size, progress):
        super().__init__(name, deadline, team_size)
        self.progress = progress  # dalam %
    
    def project_info(self):
        return f"📁 Project: {self.name} | 👥 Tim: {self.team_size} orang | ⏳ Deadline: {self.deadline}"
    
    def calculate_efficiency(self):
        # Rumus efisiensi sederhana berdasarkan progress & ukuran tim
        efficiency = (self.progress / 100) * (10 / self.team_size)
        return min(efficiency, 1.0)
    
    def evaluate_project(self):
        efficiency = self.calculate_efficiency()
        if efficiency > 0.8:
            return "🚀 Status: Excellent - Proyek berjalan sangat efisien!"
        elif efficiency > 0.5:
            return "⚙️ Status: Good - Masih dalam jalur yang baik."
        else:
            return "⏰ Status: Warning - Perlu perbaikan manajemen proyek."


# === Tampilan Streamlit ===
st.set_page_config(page_title="AI Project Management System", page_icon="🤖", layout="centered")

st.title("🤖 AI Project Management System")
st.subheader("Smart Project Evaluator for Digital Startup 🚀")
st.markdown("---")

# Input interaktif
project_name = st.text_input("Nama Proyek:", "AI Startup Booster")
deadline = st.date_input("Deadline Proyek:")
team_size = st.slider("Jumlah Anggota Tim:", 1, 10, 4)
progress = st.slider("Progress Proyek (%):", 0, 100, 70)

if st.button("🚀 Jalankan Analisis AI"):
    st.write("🔍 **Memproses data proyek dengan kecerdasan buatan...**")
    progress_bar = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    
    project = AIProjectManager(project_name, deadline, team_size, progress)
    
    st.success("✅ Analisis selesai!")
    st.write(project.project_info())
    
    with st.expander("📊 Lihat Hasil Evaluasi AI"):
        st.write(project.evaluate_project())
        st.balloons()
    
    # Efek tambahan hasil analisis acak
    insights = [
        "💡 Rekomendasi: Tingkatkan kolaborasi antar tim untuk efisiensi yang lebih tinggi.",
        "🧩 Insight: Tim kecil bekerja efisien jika diberi target mingguan yang jelas.",
        "📈 Saran AI: Gunakan tracking tools otomatis untuk memantau progress harian.",
        "🎯 Optimalisasi: AI mendeteksi potensi percepatan deadline sebesar 15%.",
    ]
    st.info(random.choice(insights))

st.markdown("---")
st.caption("🧠 Dibuat oleh Agam Al Hakim Hasibuan | Abstract Class & Interface | Python + Streamlit")

