import os
from docx import Document
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# WordPress panel URL'niz, kullanıcı adı ve şifre bilgileri
wp_url = "/xmlrpc.php"
wp_username = ""
wp_password = ""

# WordPress'e bağlanma
client = Client(wp_url, wp_username, wp_password)

# Word dosyasının içeriğini okuma fonksiyonu
def read_word_file(file_path):
    doc = Document(file_path)
    content = ""
    for paragraph in doc.paragraphs:
        content += paragraph.text + "\n"
    return content

# Klasördeki tüm Word dosyalarını işleme
directory = ""
for filename in os.listdir(directory):
    if filename.endswith(".docx"):
        file_path = os.path.join(directory, filename)
        
        # Word dosyasının içeriğini oku
        content = read_word_file(file_path)
        
        # Kullanıcıdan başlık isteme
        post_title = input(f"Başlık girin ({filename}): ")
        
        # Yeni bir blog yazısı oluşturma
        post = WordPressPost()
        post.title = post_title
        post.content = content
        post.post_status = 'draft'  # Yazıyı hemen yayınlar
        
        # Yazıyı yayınlama
        client.call(NewPost(post))
        print(f"{filename} başarıyla yayınlandı!")

print("Tüm dosyalar işlendi ve yayınlandı!")


