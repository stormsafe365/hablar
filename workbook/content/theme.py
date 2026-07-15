"""Shared look-and-feel + page shell for the Hablar personalized workbook.

Everything renders to self-contained HTML files that look good on screen and
print cleanly to PDF (letter size, real page breaks, light background).
"""
import html as _html

def esc(s):
    return _html.escape(str(s), quote=True)

# Fonts are loaded from Google Fonts to match the Hablar app (Fraunces + Inter).
# If you print offline they gracefully fall back to Georgia / system sans.
FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700;9..144,900&'
    'family=Inter:wght@400;500;600;700;800&'
    'family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">'
)

CSS = r"""
:root{
  --bg:#fbfaf6; --paper:#ffffff; --sand:#f3f1ea; --sand2:#eae7dd;
  --ink:#2a2824; --soft:#6a655c; --faint:#9a948a; --line:#e3e0d5;
  --accent:#1c8a5d; --accent2:#22b378; --accent-soft:#e6f5ee;
  --cuba:#c85a49; --cuba-soft:#f7e6e3;
  --sea:#2f8f9e; --sea-soft:#e2f0f2;
  --sun:#c68a2e; --sun-soft:#f6ecd7;
  --coral:#e0524f; --coral-soft:#fbe7e6;
  --serif:'Fraunces',Georgia,'Times New Roman',serif;
  --sans:'Inter',system-ui,-apple-system,Segoe UI,sans-serif;
  --round:'Nunito',var(--sans);
}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{background:var(--sand);color:var(--ink);font-family:var(--sans);
  line-height:1.6;font-size:16px;-webkit-font-smoothing:antialiased}
.page{background:var(--paper);max-width:820px;margin:26px auto;padding:56px 64px;
  box-shadow:0 1px 2px rgba(25,23,20,.05),0 18px 44px rgba(25,23,20,.09);
  border-radius:6px;position:relative}
h1,h2,h3,h4{font-family:var(--serif);font-weight:600;line-height:1.15;color:var(--ink)}
h1{font-size:40px;font-weight:700;letter-spacing:-.02em}
h2{font-size:28px;margin:34px 0 12px;letter-spacing:-.01em}
h3{font-size:21px;margin:26px 0 8px}
h4{font-size:17px;margin:18px 0 6px;font-family:var(--sans);font-weight:700}
p{margin:10px 0}
a{color:var(--accent);text-decoration:none}
strong{font-weight:700}
em{font-style:italic}
ul,ol{margin:10px 0 10px 24px}
li{margin:4px 0}
.small{font-size:13px;color:var(--soft)}
.muted{color:var(--soft)}
.center{text-align:center}
.es{color:var(--accent);font-weight:600}            /* spanish text */
.en{color:var(--soft)}                               /* english gloss */
hr{border:none;border-top:1px solid var(--line);margin:26px 0}

/* eyebrow / part label */
.eyebrow{font-family:var(--round);font-weight:800;text-transform:uppercase;
  letter-spacing:.14em;font-size:12px;color:var(--accent);margin-bottom:6px}

/* callout boxes */
.box{border-radius:14px;padding:16px 20px;margin:16px 0;border:1px solid var(--line);
  background:var(--bg)}
.box .lead{font-family:var(--round);font-weight:800;font-size:12px;
  text-transform:uppercase;letter-spacing:.1em;margin-bottom:6px;display:block}
.tip{background:var(--accent-soft);border-color:#cfe9dd}
.tip .lead{color:var(--accent)}
.trick{background:var(--sun-soft);border-color:#eaddbf}
.trick .lead{color:var(--sun)}
.warn{background:var(--coral-soft);border-color:#f3cfcd}
.warn .lead{color:var(--coral)}
.cuba{background:var(--cuba-soft);border-color:#eecfc9}
.cuba .lead{color:var(--cuba)}
.sea{background:var(--sea-soft);border-color:#c9e4e8}
.sea .lead{color:var(--sea)}

/* conjugation table */
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:15px}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line)}
th{font-family:var(--round);font-weight:800;font-size:12px;text-transform:uppercase;
  letter-spacing:.06em;color:var(--soft);background:var(--bg)}
.conj{border:1px solid var(--line);border-radius:12px;overflow:hidden}
.conj td:first-child{color:var(--soft);width:34%}
.conj .v{color:var(--accent);font-weight:700}
.conj tr:last-child td{border-bottom:none}

/* vocab table */
.vocab td:first-child{font-weight:600;color:var(--accent);width:38%}
.vocab td:nth-child(2){color:var(--ink)}
.vocab .ipa{color:var(--faint);font-size:13px}

/* example list */
.ex{list-style:none;margin:12px 0;padding:0}
.ex li{padding:7px 0;border-bottom:1px dashed var(--line)}
.ex li:last-child{border-bottom:none}
.ex .n{color:var(--faint);font-size:12px;font-family:var(--round);
  font-weight:800;margin-right:8px}
.ex .es{display:inline}
.ex .en{display:block;margin-left:22px;font-size:14px}

/* dialogue */
.dlg{margin:14px 0;border-left:3px solid var(--accent-soft);padding-left:16px}
.dlg .line{margin:8px 0}
.dlg .who{font-family:var(--round);font-weight:800;font-size:12px;
  color:var(--accent);display:inline-block;min-width:64px}
.dlg .en{display:block;margin-left:64px;font-size:14px}

/* exercises */
.drill{background:var(--bg);border:1px solid var(--line);border-radius:14px;
  padding:18px 22px;margin:18px 0}
.drill h4{margin-top:0}
.q{margin:9px 0;padding-left:30px;position:relative}
.q .num{position:absolute;left:0;top:0;font-family:var(--round);font-weight:800;
  color:var(--accent);font-size:14px}
.blank{display:inline-block;min-width:120px;border-bottom:1.5px solid var(--faint);
  margin:0 3px}
.write-lines{margin:10px 0}
.write-lines .ln{border-bottom:1px solid var(--line);height:26px}

/* pills / chips */
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
.chip{background:var(--sand);border:1px solid var(--line);border-radius:999px;
  padding:5px 13px;font-size:14px;font-weight:600}
.chip .en{color:var(--soft);font-weight:400;margin-left:5px}

/* flashcards */
.cards{display:grid;grid-template-columns:1fr 1fr;gap:0}
.card{border:1px dashed var(--faint);padding:16px;min-height:118px;
  display:flex;flex-direction:column;justify-content:center;text-align:center}
.card .front{font-family:var(--serif);font-size:22px;font-weight:600;color:var(--accent)}
.card .ipa{color:var(--faint);font-size:13px;margin-top:3px}
.card .back{font-size:15px;color:var(--ink);margin-top:6px}
.card .tag{font-size:11px;color:var(--faint);font-family:var(--round);
  font-weight:800;text-transform:uppercase;letter-spacing:.08em}

/* toc */
.toc{list-style:none;margin:18px 0;padding:0}
.toc li{display:flex;align-items:baseline;gap:8px;padding:7px 0;
  border-bottom:1px solid var(--line)}
.toc .t{font-weight:600}
.toc .d{color:var(--soft);font-size:14px;flex:1}
.toc .pg{color:var(--faint);font-size:13px;font-family:var(--round);font-weight:800}

/* cover */
.cover{min-height:78vh;display:flex;flex-direction:column;justify-content:center}
.cover h1{font-size:58px;font-weight:900;letter-spacing:-.03em;line-height:1.02}
.cover .sub{font-size:20px;color:var(--soft);margin-top:14px;max-width:30em}
.cover .who{margin-top:36px;font-family:var(--round);font-weight:800;
  text-transform:uppercase;letter-spacing:.12em;font-size:13px;color:var(--accent)}
.cover .flag{font-size:40px;margin-bottom:18px;letter-spacing:6px}

/* footer running head */
.foot{margin-top:40px;padding-top:14px;border-top:1px solid var(--line);
  display:flex;justify-content:space-between;color:var(--faint);font-size:12px;
  font-family:var(--round);font-weight:700;text-transform:uppercase;letter-spacing:.08em}

/* index landing grid */
.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:22px 0}
.tile{display:block;border:1px solid var(--line);border-radius:16px;padding:20px 22px;
  background:var(--bg);transition:transform .1s}
.tile:hover{transform:translateY(-2px)}
.tile .ic{font-size:26px}
.tile .tt{font-family:var(--serif);font-size:20px;font-weight:600;color:var(--ink);
  margin:6px 0 4px}
.tile .dd{font-size:14px;color:var(--soft)}

@media (max-width:640px){
  .page{padding:32px 22px;margin:10px}
  .grid,.cards{grid-template-columns:1fr}
  .cover h1{font-size:40px}
  h1{font-size:32px}
}

@media print{
  @page{size:letter;margin:16mm 15mm}
  body{background:#fff;font-size:11.5pt;line-height:1.5}
  .page{box-shadow:none;margin:0;padding:0;max-width:none;border-radius:0}
  .no-print{display:none!important}
  h2{page-break-after:avoid}
  h3,h4{page-break-after:avoid}
  table,.drill,.box,.dlg,.card,.conj{page-break-inside:avoid}
  .page-break{page-break-before:always}
  a{color:var(--ink);text-decoration:none}
  .cards{grid-template-columns:1fr 1fr}
}
"""

NAV = """
<div class="no-print" style="max-width:820px;margin:0 auto;padding:10px 16px;
  display:flex;gap:14px;flex-wrap:wrap;font-family:var(--round);font-weight:700;
  font-size:13px">
  <a href="index.html">&larr; Contents</a>
  <a href="book.html">Book</a>
  <a href="practice.html">Practice</a>
  <a href="answers.html">Answers</a>
  <a href="cheatsheets.html">Cheat&nbsp;Sheets</a>
  <a href="flashcards.html">Flashcards</a>
  <a href="tests.html">Tests</a>
</div>
"""

def shell(title, body, subtitle="", show_nav=True):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{esc(title)}</title>
{FONTS}
<style>{CSS}</style>
</head>
<body>
{NAV if show_nav else ''}
<div class="page">
{body}
<div class="foot"><span>Hablar &middot; Personalized Spanish Workbook</span>
<span>{esc(subtitle or title)}</span></div>
</div>
</body>
</html>"""

# ---- small rendering helpers shared by all content modules ----

def box(kind, lead, html_body):
    return f'<div class="box {kind}"><span class="lead">{esc(lead)}</span>{html_body}</div>'

def examples(pairs):
    """pairs: list of (spanish, english)."""
    rows = []
    for i, (es, en) in enumerate(pairs, 1):
        rows.append(
            f'<li><span class="n">{i:02d}</span>'
            f'<span class="es">{esc(es)}</span>'
            f'<span class="en">{esc(en)}</span></li>')
    return '<ul class="ex">' + "".join(rows) + "</ul>"

def dialogue(lines):
    """lines: list of (speaker, spanish, english)."""
    out = ['<div class="dlg">']
    for who, es, en in lines:
        out.append(
            f'<div class="line"><span class="who">{esc(who)}</span>'
            f'<span class="es">{esc(es)}</span>'
            f'<span class="en">{esc(en)}</span></div>')
    out.append('</div>')
    return "".join(out)

def vocab_table(rows):
    """rows: list of (spanish, english, note/ipa)."""
    out = ['<table class="vocab"><thead><tr><th>Español</th><th>English</th>'
           '<th>Note</th></tr></thead><tbody>']
    for es, en, note in rows:
        out.append(f'<tr><td>{esc(es)}</td><td>{esc(en)}</td>'
                   f'<td class="small">{esc(note)}</td></tr>')
    out.append('</tbody></table>')
    return "".join(out)

def conj_table(caption, forms):
    """forms: list of (pronoun, form). Highlights the verb form."""
    rows = []
    for pro, form in forms:
        rows.append(f'<tr><td>{esc(pro)}</td><td class="v">{esc(form)}</td></tr>')
    cap = f'<h4>{esc(caption)}</h4>' if caption else ''
    return cap + '<table class="conj"><tbody>' + "".join(rows) + '</tbody></table>'

def chips(pairs):
    out = ['<div class="chips">']
    for es, en in pairs:
        out.append(f'<span class="chip">{esc(es)}<span class="en">{esc(en)}</span></span>')
    out.append('</div>')
    return "".join(out)

def write_lines(n=3, label=""):
    lab = f'<div class="small" style="margin-bottom:4px">{esc(label)}</div>' if label else ''
    return '<div class="write-lines">' + lab + ''.join('<div class="ln"></div>' for _ in range(n)) + '</div>'

def questions(items, start=1):
    """items: list of html strings; renders numbered."""
    out = []
    for i, it in enumerate(items, start):
        out.append(f'<div class="q"><span class="num">{i}.</span>{it}</div>')
    return "".join(out)

def drill(title, inner):
    return f'<div class="drill"><h4>{esc(title)}</h4>{inner}</div>'

def blank(width=120):
    return f'<span class="blank" style="min-width:{width}px"></span>'
