from django.shortcuts import render

def show_main(request):
    context = {
        'nama': 'Anastasia Keisha Bella Arianne Pepe',
        'kelas': 'PBP F',
        'informasi' : [
            {
                'name': 'Bumi',
                'amount': '55',
                'description': 'Novel ini bercerita mengenai petualangan antarklan dengan tokoh utamanya, yaitu Raib. Raib adalah generasi keturunan murni dari Klan Bulan dan ia melakukan petualangan ke dunia paralel bersama dua sahabatnya, yaitu Seli dan Ali.',
            },
            {
                'name': 'Semua Ikan di Langit',
                'amount': '25',
                'description': 'Buku ini bercerita mengenai perjalanan Bus yang di dalamnya terdapat anak kecil dengan panggilan Beliau, dan kecoak bule perempuan bernama Nadheza (Nad). Mereka melakukan perjalanan jauh yang bahkan tidak berada di trayeknya lagi. Lebih jauh dari sekadar perjalanan antar Dipatiukur - Leuwi panjang. Bukan juga perjalanan antar provinsi. Melainkan mengelilingi angkasa, melintasi dimensi ruang dan waktu.',
            },
            {
                'name': 'The Bliss Bakery #2: A Dash of Magic',
                'amount': '35',
                'description': 'A Dash of Magic merupakan buku kedua dari The Bliss Bakery Series karya Kathryn Littewood. Buku ini masih menceritakan tentang Rosemary Bliss dan keluarganya yang memiliki rahasia dalam menciptakan kue-kue yang tidak hanya sekedar lezat tapi juga mampu mengubah keadaan.',
            }
        ]
    }

    return render(request, "main.html", context)