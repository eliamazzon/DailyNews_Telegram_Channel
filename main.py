import markdown
import os

#open md post and convert it to html
with open(f"blog-posts/md-posts/{post_name}.md", 'r') as f:
    text = f.read()
    html = markdown.markdown(text)

#write converted html to file
with open(f'blog-posts/converted_{post_name}.html', 'w') as f:
    f.write(html)
