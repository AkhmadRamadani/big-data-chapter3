### **Nama** : Akhmad Ramadani
### **Kelas** : TI - 3B

  

<table>

<tr  align="center">

<td>

Accumulator

<td> <img  src="https://github.com/AkhmadRamadani/big-data-chapter3/blob/main/Accumulator/Screenshot%202023-03-24%20at%2010.27.46.png?raw=true"  width=70%  height=70%><br>


Pada baris ketiga, sebuah variabel myaccum dengan nilai awal 0 dibuat menggunakan method accumulator() dari objek sc. Accumulator digunakan untuk mengakumulasi nilai dari beberapa task yang berjalan secara terdistribusi di cluster.

Pada baris keempat, sebuah RDD (Resilient Distributed Dataset) dengan nama myrdd dibuat menggunakan method parallelize() dari objek sc. RDD adalah sebuah dataset yang terdistribusi secara teratur di beberapa node dalam cluster Spark.

Pada baris kelima, sebuah fungsi lambda diteruskan ke method foreach() dari objek myrdd. Fungsi ini memanggil method add() dari objek myaccum untuk setiap elemen dalam RDD.

Pada baris keenam, nilai akumulator (yaitu jumlah semua bilangan dari 1 hingga 99) dicetak ke konsol menggunakan method value() dari objek myaccum.

Jadi, kode ini menghitung jumlah bilangan dari 1 hingga 99 dengan mengakumulasi nilai di setiap node dalam cluster menggunakan SparkContext dan RDD. Nilai akhir kemudian dicetak ke konsol.

</td>

</td>

</tr>

<tr  align="center">

<td>

Broadcast

<td><img  src="https://github.com/AkhmadRamadani/big-data-chapter3/blob/main/Broadcast/Screenshot%202023-03-24%20at%2010.28.07.png?raw=true"  width=100%  height=100%><br>

Pada baris kedua, sebuah objek SparkContext dengan nama "sc" dibuat. Objek ini mewakili koneksi ke cluster Spark yang sedang berjalan. Pada saat pembuatan objek ini, aplikasi Spark dengan nama "Log Analytics" juga ditentukan.

Pada baris ketiga, sebuah list dari angka 1 hingga 99 dibuat, kemudian di-broadcast menggunakan method broadcast() dari objek sc. Broadcast variable digunakan untuk mengirimkan data secara efisien dari driver program ke seluruh worker dalam cluster. Broadcast variable adalah variabel read-only yang dapat diakses oleh semua worker dalam cluster.

Pada baris keempat, method value() dipanggil pada broadcast variable "broadcastVar" untuk mengakses nilai yang dibroadcast, yaitu list dari angka 1 hingga 99.

Jadi, kode ini membuat sebuah broadcast variable dari list yang berisi angka 1 hingga 99 menggunakan SparkContext. Broadcast variable ini dapat diakses secara efisien oleh semua worker dalam cluster untuk mempercepat pemrosesan data dalam aplikasi Spark. Nilai broadcast variable kemudian dicetak ke konsol.

</td>

</td>

</tr>

<tr  align="center">

<td>

PairRDD

<td><img  src="https://github.com/AkhmadRamadani/big-data-chapter3/blob/main/PairRDD/Screenshot%202023-03-24%20at%2010.43.05.png?raw=true"  width=70%  height=70%><br>

Pada baris ketiga, sebuah list "mylist" dengan tiga elemen dibuat. Kemudian, list ini dijadikan RDD dengan method parallelize() dari objek sc.

Pada baris keempat, sebuah fungsi lambda diteruskan ke method map() dari objek myRDD untuk menghitung panjang dari setiap elemen dalam RDD. Hasilnya adalah RDD baru dengan pasangan key-value, di mana key adalah elemen dari RDD asli dan value adalah panjangnya.

Pada baris kelima, method collect() dipanggil pada objek myPairRDD untuk mengumpulkan semua pasangan key-value dari RDD dan mengembalikan hasil dalam bentuk list.

Pada baris keenam, method keys() dipanggil pada objek myPairRDD untuk mengambil semua key dari pasangan key-value dalam RDD, kemudian method collect() dipanggil untuk mengumpulkan semua key dan mengembalikan hasil dalam bentuk list.

Pada baris ketujuh, method values() dipanggil pada objek myPairRDD untuk mengambil semua value dari pasangan key-value dalam RDD, kemudian method collect() dipanggil untuk mengumpulkan semua value dan mengembalikan hasil dalam bentuk list.

Jadi, kode ini membuat sebuah RDD dari list "mylist" dan kemudian mengubahnya menjadi sebuah RDD baru dengan pasangan key-value menggunakan method map(). Objek RDD baru kemudian digunakan untuk mendapatkan key, value, atau pasangan key-value melalui pemanggilan method keys(), values(), dan collect().

</td>

</td>

</tr>

<tr  align="center">

<td>

WordCount

<td>

<img  src="https://github.com/AkhmadRamadani/big-data-chapter3/blob/main/WordCount/Screenshot%202023-03-24%20at%2010.49.25.png?raw=true"  width=70%  height=70%>

Pada baris ketiga, modul operator diimpor. Operator ini digunakan untuk melakukan operasi matematika dan logika pada RDD.

Pada baris keempat, sebuah file teks "README.md" dibaca ke dalam RDD dengan menggunakan method textFile() dari objek sc.

Pada baris kelima, RDD dari setiap baris dalam file dibagi menjadi kata-kata individual menggunakan method flatMap() dengan fungsi lambda. Fungsi lambda ini akan membagi setiap baris menjadi beberapa kata menggunakan spasi sebagai delimiter.

Pada baris keenam, setiap kata dalam RDD diberi nilai awal 1 dan dijadikan pasangan key-value menggunakan method map() dengan fungsi lambda.

Pada baris ketujuh, pasangan key-value dalam RDD dihitung jumlahnya menggunakan method reduceByKey() dengan operator add().

Pada baris kedelapan, hasil akhir dalam bentuk list disimpan dalam variabel "output".

Pada baris kesembilan dan kesepuluh, setiap pasangan key-value dalam list "output" diambil dan dicetak ke konsol.

Jadi, kode ini membaca sebuah file teks "README.md" ke dalam RDD, kemudian menghitung jumlah kata yang muncul dalam file tersebut dan mencetak hasilnya ke konsol.

</td>

</td>

</tr>

<tr  align="center">

<td>

LogAnalytics

<td>

<img  src="https://github.com/AkhmadRamadani/big-data-chapter3/blob/main/LogAnalytics/Screenshot%202023-03-24%20at%2010.57.37.png?raw=true"  width=70%  height=70%><br>

Kode di atas menggunakan Pyspark untuk menganalisis file log akses. File log ini dibaca oleh SparkContext, dan dipecah menjadi beberapa bagian. Kemudian, baris-baris di dalam file yang mengandung kata "ERROR" disaring dan disimpan dalam variabel "error_log". Variabel ini di-cache di dalam memori untuk mempercepat pengolahan data.

Pada baris terakhir, terdapat dua operasi yang dilakukan. Pertama, jumlah keseluruhan baris yang mengandung kata "ERROR" dihitung menggunakan method count() dari variabel "cached_log", dan di-print ke konsol. Kedua, jumlah baris yang mengandung kata "product" dan "ERROR" dihitung menggunakan method filter() dan count(), dan juga dicetak ke konsol.

Kode ini menggunakan argumen command-line untuk menentukan file log akses yang akan diolah. Jika jumlah argumen yang diberikan tidak sama dengan 2, maka kode akan mengeluarkan pesan error dan keluar. Jika jumlah argumen sesuai, maka argumen kedua (yang merupakan path ke file log akses) akan digunakan untuk membaca file tersebut dengan menggunakan method textFile() dari objek sc.

Dalam rangka meningkatkan kinerja, variabel "access_log" dibagi menjadi 4 partisi untuk pemrosesan yang lebih cepat.
</td>

</td>

</tr>

<tr  align="center">

<td>

UnderstandingRDD

<td>

<img  src="https://github.com/AkhmadRamadani/big-data-chapter3/blob/main/UnderstandingRDDs/Screenshot%202023-03-24%20at%2011.04.33.png?raw=true"  width=70%  height=70%><br>

Kode di atas menggunakan Pyspark untuk mempelajari tentang parallelism, yaitu bagaimana RDD dipecah menjadi beberapa partisi untuk meningkatkan kinerja.

Pertama-tama, kode mengambil nilai default parallelism (jumlah partisi default) dari SparkContext menggunakan method defaultParallelism. Kemudian, kode membuat RDD dari sebuah list dan memeriksa jumlah partisinya menggunakan method getNumPartitions(). Kemudian, kode menciptakan RDD yang sama dengan jumlah partisi yang lebih banyak menggunakan argument opsional kedua pada method parallelize(). Kemudian, kode menghitung jumlah elemen dalam RDD menggunakan method count().

Selanjutnya, kode menampilkan isi dari setiap partisi menggunakan method mapPartitionsWithIndex() dan collect(). Kode juga menunjukkan bagaimana meningkatkan dan mengurangi jumlah partisi menggunakan method repartition() dan coalesce().

Terakhir, kode menampilkan lineage graph RDD menggunakan method toDebugString(). Lineage graph adalah grafik yang menunjukkan riwayat bagaimana RDD dibuat melalui serangkaian transformasi.
</td>

</td>

</tr>

</table>