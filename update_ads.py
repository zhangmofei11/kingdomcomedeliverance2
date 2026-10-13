import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/4b882874a10df4f109b7f61cba60a889"></script>
<script data-cfasync="false" src="https://bauval.org/14/8b109ab392a76528f2f96959f7107611"></script>
<script>
  atOptions = {
    'key' : '302cc7e4fea23afe07c2cacb0b29c0ed',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/302cc7e4fea23afe07c2cacb0b29c0ed"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-4b882874a10df4f109b7f61cba60a889"></div>
</div>'''

files = ['index.html', 'quests.html', 'combat.html', 'weapons.html', 'skills.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '302cc7e4fea23afe07c2cacb0b29c0ed' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-4b882874a10df4f109b7f61cba60a889' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
