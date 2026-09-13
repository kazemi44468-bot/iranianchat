from pathlib import Path
import re
chatiha = Path('chatiha/index.html').read_text(encoding='utf-8')
ertebasan = Path('ertebasan/index.html').read_text(encoding='utf-8')
auth_style = re.search(r'<style id="chatiha-auth-style">.*?</style>', chatiha, re.S).group(0)
auth_refine = re.search(r'<style id="chatiha-auth-logo-refinement">.*?</style>', chatiha, re.S).group(0)
gate = re.search(r'<section class="auth-gate" id="authGate".*?</section>', chatiha, re.S).group(0)
script_tag = re.search(r'<script id="chatiha-auth-script">.*?</script>', chatiha, re.S).group(0)
gate = gate.replace('ورود و ثبت نام چتی‌ها', 'ورود و ثبت نام ارتباسان').replace('alt="چتی‌ها"', 'alt="ارتباسان"')
gate = gate.replace('به <span>چتی‌ها</span> خوش آمدید', 'به <span>ارتباسان</span> خوش آمدید')
gate = gate.replace('پیام‌رسان و شبکه ارتباطی ایرانیان؛ گفتگو، گروه، کانال، تماس و ارتباطات اجتماعی در یک فضای یکپارچه.', 'شبکه ارتباطی آسان و امن برای ارتباطات صوتی، تصویری و متنی در یک فضای یکپارچه.')
old = re.search(r'<div class="auth-features">.*?</div>\s*</div>', gate, re.S)
new = '''<div class="auth-features">
<div class="auth-feature"><i>☎</i><span>تماس صوتی</span></div>
<div class="auth-feature"><i>▣</i><span>تماس تصویری</span></div>
<div class="auth-feature"><i>✉</i><span>تماس متنی</span></div>
</div>
</div>'''
gate = gate[:old.start()] + new + gate[old.end():]
script_tag = script_tag.replace('ورود به چتی‌ها', 'ورود به ارتباسان')
extra = '''<style id="ertebasan-auth-refinement">.auth-features{grid-template-columns:repeat(3,1fr);gap:9px;max-width:100%}.auth-feature{justify-content:center;text-align:center;min-height:58px}@media(max-width:760px){.auth-features{grid-template-columns:repeat(3,1fr);gap:5px}.auth-feature{display:flex!important;min-height:42px;padding:6px 4px;font-size:8px;flex-direction:column;gap:3px}.auth-feature i{font-size:15px}}</style>'''
ertebasan = ertebasan.replace('</head>', auth_style + auth_refine + extra + '</head>', 1)
ertebasan = ertebasan.replace('<body>', '<body>\n' + gate, 1)
ertebasan = ertebasan.replace('</body>', script_tag + '\n</body>', 1)
Path('ertebasan/index.html').write_text(ertebasan, encoding='utf-8')
