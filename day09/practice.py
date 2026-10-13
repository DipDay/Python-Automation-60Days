from bs4 import BeautifulSoup

# html_content created by gemini
html_content = """                                    
<div class="product-card">
    <h2 class="title">  Laptop Pro  \n</h2>
    <a href="https://example.com/item1">View Item</a>
    <span class="price">$999</span>
</div>

<div class="product-card">
    <h2 class="title">Mouse</h2>
    <a href="https://example.com/item2">View Item</a>
    <!-- Here price Missing (Missing Data) -->
</div>
"""

soup = BeautifulSoup(html_content, 'lxml')

products = soup.find_all('div', class_='product-card')

for product in products:
    # 1. Nested Elements & Text + Strip
    title_tag = product.find('h2', class_='title')
    title = title_tag.text.strip() if title_tag else "No Title"

    link_tag = product.find('a')
    link = link_tag.get('href') if link_tag else "No Link"

    # Missing Data Handle 
    price_tag = product.find('span', class_='price')
    price = price_tag.text.strip() if price_tag else "N/A"  

    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Price: {price}")
    print("-" * 20)