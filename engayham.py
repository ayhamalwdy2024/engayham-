import requests

# قائمة من المسارات الشائعة لصفحات الإدارة
admin_paths = [
    'admin', 'admin.php', 'admin.html', 'admin/login', 'admin/login.php', 'admin/login.html',
    'administrator', 'administrator.php', 'administrator.html', 'admin1', 'admin1.php',
    'admin1.html', 'admin2', 'admin2.php', 'admin2.html', 'admin_area', 'admin_area.php',
    'admin_area.html', 'admincontrol', 'admincontrol.php', 'admincontrol.html', 'adminpanel',
    'adminpanel.php', 'adminpanel.html', 'admin_login', 'admin_login.php', 'admin_login.html',
    'wp-admin', 'wp-login', 'user', 'user.php', 'user.html', 'users', 'users.php', 'users.html',
    'controlpanel', 'controlpanel.php', 'controlpanel.html', 'cpanel', 'cpanel.php', 'cpanel.html',
    'adm', 'adm.php', 'adm.html', 'admin/account.php', 'admin/account.html', 'admin/home.php',
    'admin/home.html', 'admin/controlpanel.php', 'admin/controlpanel.html'
]

def find_admin_page(url):
    if not url.startswith("http"):
        url = "http://" + url

    for path in admin_paths:
        full_url = f"{url.rstrip('/')}/{path}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"Found admin page: {full_url}")
            else:
                print(f"Checked: {full_url} - Not Found (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {full_url}: {e}")

if __name__ == "__main__":
    site_url = input("Enter the website URL: ")
    find_admin_page(site_url)
