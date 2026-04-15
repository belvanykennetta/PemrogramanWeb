<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VenomIT - Join the Future</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background: linear-gradient(135deg, #271161 0%, #9e37b0 50%, #6bebe0 100%);
            background-attachment: fixed;
            color: white;
            overflow-x: hidden;
        }

        /*TOP BAR*/
        .top-bar {
            position: fixed;
            top: 0;
            width: 100%;
            height: 80px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 8%;
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 1000;
        }

        .logo { 
            display: flex; 
            align-items: center; 
            gap: 12px; 
            font-size: 24px; 
            font-weight: 800; 
        }
        .logo img {
            height: 40px;
            width: auto;
        }

        .nav-links { display: flex; gap: 30px; }
        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: 600;
            transition: 0.3s;
        }
        .nav-links a:hover { color: #6bebe0; }

        /*SECTION LAYOUT*/
        section {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 100px 8%;
            text-align: center;
        }

        /*HOME SECTION*/
        .hero-h1 {
            font-size: clamp(3.5rem, 10vw, 6rem);
            font-weight: 800;
            line-height: 1;
            margin-bottom: 20px;
            background: linear-gradient(to bottom, #fff, #6bebe0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: bounceIn 1s ease;
        }

        .hero-p {
            font-size: 1.4rem;
            max-width: 700px;
            margin-bottom: 40px;
            opacity: 0.9;
        }

        .btn-join-now {
            background: #ff9e7d;
            color: white;
            padding: 20px 50px;
            font-size: 1.5rem;
            font-weight: 800;
            text-decoration: none;
            border-radius: 60px;
            box-shadow: 0 10px 30px rgba(255, 158, 125, 0.5);
            transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: inline-block;
        }

        .btn-join-now:hover {
            transform: scale(1.1) rotate(-2deg);
            background: white;
            color: #271161;
        }

        /*ABOUT US SECTION*/
        #about { background: rgba(0, 0, 0, 0.1); }
        .history-container {
            display: flex;
            align-items: center;
            gap: 50px;
            max-width: 1000px;
            margin-bottom: 100px;
            text-align: left;
            flex-wrap: wrap;
        }
        .history-text { flex: 1; min-width: 300px; }
        .history-text h2 { font-size: 2.5rem; font-weight: 800; margin-bottom: 15px; color: #6bebe0; }
        .history-text p { font-size: 1.1rem; line-height: 1.8; opacity: 0.9; }
        .history-img {
            flex: 1; 
            min-width: 300px; 
            height: 350px;
            /* Gunakan url() untuk memanggil file gambar */
            background: url('kursus.png') no-repeat center;
            background-size: cover; 
            border-radius: 30px;
            box-shadow: 20px 20px 0px rgba(255, 255, 255, 0.1);
            transition: 0.5s;
        }
        .history-img:hover { transform: scale(1.02); box-shadow: 10px 10px 0px #ff9e7d; }
        
        .review-box {
            background: rgba(255, 255, 255, 0.95); padding: 40px; border-radius: 35px;
            color: #333; width: 100%; max-width: 800px; margin-bottom: 60px;
            transform: rotate(0deg); 
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .review-box:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 25px 50px rgba(0,0,0,0.25);
        }

        textarea {
            width: 100%; height: 100px; border: 3px dashed #9e37b0;
            border-radius: 20px; padding: 15px; font-size: 1rem;
            outline: none; resize: none; margin: 15px 0;
        }
        .testi-container { width: 100%; max-width: 800px; display: flex; flex-direction: column; gap: 20px; margin-bottom: 80px; }
        .testi-card {
            background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px);
            padding: 25px; border-radius: 25px; display: flex; align-items: center; gap: 20px; text-align: left; transition: 0.4s;
        }
        .testi-card:hover { background: white; color: #333; transform: translateX(20px); }
        .profile-img { width: 60px; height: 60px; border-radius: 50%; border: 3px solid #6bebe0; }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 900px;
            margin-top: 30px;
        }
        .contact-item {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 20px;
            text-decoration: none;
            color: white;
            font-weight: 600;
            transition: 0.3s;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .contact-item:hover {
            background: #6bebe0;
            color: #271161;
            transform: translateY(-5px);
        }

        /*COURSES SECTION*/
        #courses { background: rgba(0, 0, 0, 0.2); }
        .course-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            width: 100%;
            max-width: 1200px;
            margin-top: 40px;
        }
        .course-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 30px;
            padding: 50px 30px;
            text-align: left;
            transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        .course-card:hover {
            transform: translateY(-15px);
            background: rgba(255, 255, 255, 0.15);
            border-color: #6bebe0;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }
        .course-badge {
            position: absolute;
            top: 20px; right: -30px;
            background: #ff9e7d;
            padding: 5px 40px;
            transform: rotate(45deg);
            font-size: 0.7rem;
            font-weight: 800;
        }
        .course-card h3 { 
            font-size: 2.2rem;
            font-weight: 800; 
            margin-bottom: 15px; 
            line-height: 1.1;
            letter-spacing: -1px;
            background: linear-gradient(to right, #6bebe0, #fff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .course-card p { font-size: 0.95rem; line-height: 1.6; opacity: 0.8; margin-bottom: 30px; min-height: 70px;}

        .course-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid rgba(255,255,255,0.1);
            padding-top: 20px;
        }
        .price-tag { font-weight: 800; font-size: 1.2rem; }
        .btn-enroll {
            color: #fff;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            padding: 8px 20px;
            border: 1px solid #6bebe0;
            border-radius: 50px;
            transition: 0.3s;
        }
        .btn-enroll:hover { background: #6bebe0; color: #271161; }

        @keyframes bounceIn {
            0% { opacity: 0; transform: scale(0.5); }
            100% { opacity: 1; transform: scale(1); }
        }

        @media (max-width: 768px) {
            .history-container { text-align: center; }
            .testi-card { flex-direction: column; text-align: center; }
        }

        /* MODAL STYLES */
    .modal-overlay {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(10px);
        display: none; /* Sembunyi secara default */
        justify-content: center;
        align-items: center;
        z-index: 2000;
    }

    .modal-content {
        background: white;
        color: #333;
        padding: 40px;
        border-radius: 30px;
        width: 90%;
        max-width: 500px;
        position: relative;
        animation: slideUp 0.4s ease;
    }

    @keyframes slideUp {
        from { transform: translateY(50px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    .modal-content h2 {
        margin-bottom: 20px;
        color: #271161;
        font-weight: 800;
    }

    .form-group {
        text-align: left;
        margin-bottom: 15px;
    }

    .form-group label {
        display: block;
        font-weight: 600;
        margin-bottom: 5px;
        font-size: 0.9rem;
    }

    .form-group input, .form-group select {
        width: 100%;
        padding: 12px 15px;
        border: 2px solid #eee;
        border-radius: 12px;
        outline: none;
        font-family: inherit;
    }

    .form-group input:focus {
        border-color: #9e37b0;
    }

    .btn-submit {
        background: #271161;
        color: white;
        width: 100%;
        padding: 15px;
        border: none;
        border-radius: 50px;
        font-weight: 800;
        font-size: 1rem;
        cursor: pointer;
        margin-top: 10px;
        transition: 0.3s;
    }

    .btn-submit:hover {
        background: #6bebe0;
        color: #271161;
    }

    .close-modal {
        position: absolute;
        top: 20px;
        right: 20px;
        font-size: 1.5rem;
        cursor: pointer;
        color: #999;
    }
    </style>
</head>
<body>

    <header class="top-bar">
        <div class="logo">
            <img src="logo.png" alt="Logo">
            <span>VenomIT</span>
        </div>
        <nav class="nav-links">
            <a href="#home">Home</a>
            <a href="#courses">Courses</a>
            <a href="#about">About Us</a>
        </nav>
    </header>

    <section id="home">
        <h1 class="hero-h1">READY TO BE<br>MASTER?</h1>
        <p class="hero-p">Release the Venom. Rule the System!</p>
        <a href="#courses" class="btn-join-now">EXPLORE COURSES ⚡</a>
    </section>

    <section id="courses">
        <h2 style="font-size: 3rem; font-weight: 800;">Our Specialized Tracks</h2>
        <p style="opacity: 0.8; margin-top: 10px;">Choose your path to success.</p>

        <div class="course-grid">
            <div class="course-card">
                <div class="course-badge">HOT</div>
                <h3>AI & Machine Learning</h3>
                <p>Bangun model cerdas dengan Python, Deep Learning, dan Computer Vision untuk masa depan.</p>
                <div class="course-footer">
                    <span class="price-tag">Rp 499k</span>
                    <a href="#" class="btn-enroll">Join Track →</a>
                </div>
            </div>

            <div class="course-card">
                <h3>Software Engineering</h3>
                <p>Pelajari arsitektur perangkat lunak, Clean Code, hingga cara kerja sistem skala besar.</p>
                <div class="course-footer">
                    <span class="price-tag">Rp 550k</span>
                    <a href="#" class="btn-enroll">Join Track →</a>
                </div>
            </div>

            <div class="course-card">
                <h3>Big Data Analysis</h3>
                <p>Ubah data mentah menjadi keputusan bisnis yang berharga melalui statistik canggih.</p>
                <div class="course-footer">
                    <span class="price-tag">Rp 450k</span>
                    <a href="#" class="btn-enroll">Join Track →</a>
                </div>
            </div>

            <div class="course-card">
                <div class="course-badge" style="background: #6bebe0; color: #271161;">NEW</div>
                <h3>Fullstack Web Dev</h3>
                <p>Kuasai Frontend & Backend menggunakan React dan Node.js untuk membangun aplikasi modern.</p>
                <div class="course-footer">
                    <span class="price-tag">Rp 599k</span>
                    <a href="#" class="btn-enroll">Join Track →</a>
                </div>
            </div>

            <div class="course-card">
                <div class="course-badge">HOT</div>
                <h3>UI/UX Design</h3>
                <p>Desain antarmuka yang menarik dan pengalaman pengguna yang optimal untuk aplikasi digital.</p>
                <div class="course-footer">
                    <span class="price-tag">Rp 400k</span>
                    <a href="#" class="btn-enroll">Join Track →</a>
                </div>
            </div>

            <div class="course-card">
                <div class="course-badge">HOT</div>
                <h3>Cyber Security</h3>
                <p>Belajar perlindungan sistem dan jaringan dari ancaman cyber threats.</p>
                <div class="course-footer">
                    <span class="price-tag">Rp 499k</span>
                    <a href="#" class="btn-enroll">Join Track →</a>
                </div>
            </div>
        </div>
    </section>

    <section id="about">
        <div class="history-container">
            <div class="history-text">
                <h2>Established Since 2018</h2>
                <p>VenomIT bermula dari sebuah garasi kecil dengan mimpi besar: membuat edukasi teknologi menjadi asik dan mudah diakses siapa saja. Selama lebih dari 8 tahun, kami telah melahirkan ribuan talenta digital.</p>
                <div style="margin-top: 20px; font-weight: 800; color: #ff9e7d;">#BuildSkillsForFuture</div>
            </div>
            <div class="history-img"></div>
        </div>

        <h2 style="font-size: 3rem; margin-bottom: 40px; font-weight: 800;">What They Say?</h2>
        
        <div class="review-box">
            <h3 style="color: #271161;">We wanna hear your review! ✨</h3>
            <textarea placeholder="Ceritakan pengalaman belajarmu di sini..."></textarea>
            <button style="background: #ff9e7d; color: white; border: none; padding: 12px 30px; border-radius: 50px; font-weight: 800; cursor: pointer;">SEND REVIEW 💌</button>
        </div>

        <div class="testi-container">
            <div class="testi-card">
                <img src="https://i.pravatar.cc/150?u=11" class="profile-img">
                <div>
                    <h4>Sitti Aminah</h4>
                    <p style="color: #ff9e7d;">⭐⭐⭐⭐⭐</p>
                    <p>"GILSS ini VenomIT gacor bangettt! UI-nya aja udah bikin betah, apalagi materinya."</p>
                </div>
            </div>
            <div class="testi-card">
                <img src="https://i.pravatar.cc/150?u=22" class="profile-img" style="border-color: #ff9e7d;">
                <div>
                    <h4>Henry Alifian</h4>
                    <p style="color: #ff9e7d;">⭐⭐⭐⭐⭐</p>
                    <p>"First time banget nemu tempat les yang gak bikin pusing. Mantap VenomIT!"</p>
                </div>
            </div>
            <div class="testi-card">
                <img src="https://i.pravatar.cc/150?u=33" class="profile-img" style="border-color: #9e37b0;">
                <div>
                    <h4>Muhammad Aditya</h4>
                    <p style="color: #ff9e7d;">⭐⭐⭐⭐⭐</p>
                    <p>"Materi deep learningnya gampang banget dipahami buat pemula kaya aku."</p>
                </div>
            </div>
            <div class="testi-card">
                <img src="https://i.pravatar.cc/150?u=44" class="profile-img">
                <div>
                    <h4>Shabrina Sarayati</h4>
                    <p style="color: #ff9e7d;">⭐⭐⭐⭐</p>
                    <p>"Recomended PARAHH buat yang mau switch career ke tech industry."</p>
                </div>
            </div>
        </div>

        <h2 style="font-size: 2.5rem; font-weight: 800; margin-top: 40px;">Connect With Us</h2>
        <div class="contact-grid">
            <a href="https://www.instagram.com/belvanyyy" target="_blank" class="contact-item">Instagram</a>
            <a href="mailto:hellow.belva@gmail.com" class="contact-item">Email</a>
            <a href="https://www.tiktok.com/@cia0obellva" target="_blank" class="contact-item">TikTok</a>
            <a href="https://wa.me/6287881700906" target="_blank" class="contact-item">WhatsApp</a>
        </div>
    </section>

    <div class="modal-overlay" id="modalForm">
    <div class="modal-content">
        <span class="close-modal" onclick="closeForm()">&times;</span>
        <h2>Daftar Sekarang 🚀</h2>
        <form id="registrationForm">
            <div class="form-group">
                <label>Nama Lengkap</label>
                <input type="text" id="nama" placeholder="Contoh: Budi Santoso" required>
            </div>
            <div class="form-group">
                <label>Jenjang Pendidikan</label>
                <select id="pendidikan" required>
                    <option value="">Pilih Jenjang</option>
                    <option value="SMA/SMK">SMA/SMK</option>
                    <option value="D3/D4/S1">Mahasiswa (D3/D4/S1)</option>
                    <option value="Umum">Umum / Profesional</option>
                </select>
            </div>
            <div class="form-group">
                <label>Course yang Dipilih</label>
                <input type="text" id="selectedCourse" readonly>
            </div>
            <div class="form-group">
                <label>Asal Kota</label>
                <input type="text" id="kota" placeholder="Contoh: Jakarta" required>
            </div>
            <div class="form-group">
                <label>Nomor WhatsApp</label>
                <input type="tel" id="wa" placeholder="0812xxxx" required>
            </div>
            <button type="submit" class="btn-submit">LANJUT KE PEMBAYARAN 💳</button>
        </form>
    </div>
</div>
<script>
    const modal = document.getElementById('modalForm');
    const courseInput = document.getElementById('selectedCourse');
    const regForm = document.getElementById('registrationForm');

    // Fungsi membuka modal
    // Kita cari semua tombol join track
    document.querySelectorAll('.btn-enroll').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            // Ambil nama course dari elemen H3 terdekat
            const courseName = this.closest('.course-card').querySelector('h3').innerText;
            courseInput.value = courseName;
            modal.style.display = 'flex';
        });
    });

    // Fungsi tutup modal
    function closeForm() {
        modal.style.display = 'none';
    }

    // Klik di luar modal untuk tutup
    window.onclick = function(event) {
        if (event.target == modal) {
            closeForm();
        }
    }

    // Handle Submit Form
    regForm.onsubmit = function(e) {
        e.preventDefault();
        
        const nama = document.getElementById('nama').value;
        const course = courseInput.value;

        // Simulasi Loading
        alert(`Halo ${nama}! Data kamu untuk kursus ${course} sudah tersimpan.\n\nKamu akan diarahkan ke halaman pembayaran...`);
        
        // Diarahkan ke halaman simulasi pembayaran (misal WhatsApp atau eksternal link)
        // Di sini saya contohkan mengarahkan ke link WhatsApp dengan pesan otomatis
        const phone = "6287881700906"; 
        const message = `Halo VenomIT, saya ingin daftar kursus!\n\nNama: ${nama}\nCourse: ${course}\nKota: ${document.getElementById('kota').value}`;
        
        window.location.href = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
    }
</script>
</body>
</html>
