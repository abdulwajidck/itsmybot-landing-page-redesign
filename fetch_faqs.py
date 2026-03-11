import urllib.request
import re

req = urllib.request.Request(
    'https://itsmybot.com', 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
        # Look for typical Elementor or WordPress FAQ accordion structures
        # The content might be inside <div class="elementor-accordion"> or similar.
        # Let's just find the text between title and content classes.
        
        # A simple dirty regex for generic HTML tags to extract readable text
        import html.parser
        
        class MyHTMLParser(html.parser.HTMLParser):
            def __init__(self):
                super().__init__()
                self.text = []
                self.recording = False
            def handle_starttag(self, tag, attrs):
                attrs_dict = dict(attrs)
                # print all classes that have "faq" or "accordion"
                cls = attrs_dict.get('class', '')
                if 'faq' in cls.lower() or 'accordion' in cls.lower():
                    self.recording = True
            def handle_data(self, data):
                if self.recording and data.strip():
                    self.text.append(data.strip())

        parser = MyHTMLParser()
        parser.feed(html)
        
        # Try a simpler regex to find Question/Answers if parser is too noisy
        questions = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>|<div[^>]*class="[^"]*title[^"]*"[^>]*>(.*?)</div>', html, re.I)
        
        # Let's just write the raw HTML of the FAQ section to a file so we can inspect it manually.
        with open("raw_faqs.html", "w") as f:
            f.write(html)
            
        print("Downloaded HTML to raw_faqs.html")

except Exception as e:
    print(f"Error: {e}")
