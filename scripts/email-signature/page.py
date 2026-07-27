#!/usr/bin/env python3
"""
Emit the Gmail-pasteable signature page.

Layout: the card is ONE solid image (so it can never come apart when dragged),
linked to the portfolio. The Instagram / YouTube icons sit just below it as
their own small images, each with its own link — which is the only way Gmail
allows more than one destination, since an inserted image carries exactly one
link and Gmail strips image maps.

  in : public/email-signature-card.png, public/sig/icon-*.png
  out: public/email-signature/index.html
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.abspath(os.path.join(HERE, '..', '..', 'public'))

SITE = 'https://kayleerenaud.com'
IG = 'https://www.instagram.com/the.miss.kaylee/'
YT = 'https://www.youtube.com/@the.miss.kaylee'

W, H = 500, 168     # card display size
ICON = 22           # icon display size

IMG_STYLE = ('display:block;border:0;outline:none;text-decoration:none;'
             '-ms-interpolation-mode:bicubic;')


def icon(src, href, alt):
    return (f'<td style="padding:0;font-size:0;line-height:0;">'
            f'<a href="{href}" style="text-decoration:none;border:0;">'
            f'<img src="{SITE}/sig/{src}" width="{ICON}" height="{ICON}" '
            f'alt="{alt}" style="{IMG_STYLE}" /></a></td>')


gap = '<td style="font-size:0;line-height:0;width:12px;">&nbsp;</td>'

signature = f'''<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
  <tr>
    <td style="padding:0;font-size:0;line-height:0;">
      <a href="{SITE}" style="text-decoration:none;border:0;"><img
        src="{SITE}/email-signature.png" width="{W}" height="{H}"
        alt="Kaylee Renaud &mdash; Film, Costume, Writing &mdash; kayleerenaud.com"
        style="{IMG_STYLE}" /></a>
    </td>
  </tr>
  <tr>
    <td style="padding:11px 0 0 26px;font-size:0;line-height:0;">
      <table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
        <tr>
          {icon('icon-instagram.png', IG, 'Instagram')}
          {gap}
          {icon('icon-youtube.png', YT, 'YouTube')}
        </tr>
      </table>
    </td>
  </tr>
</table>'''

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Email signature &mdash; Kaylee Renaud</title>
<style>
  body {{ margin:0; padding:44px 20px 80px; background:#14110f; color:#f1ece4;
         font-family:Georgia,serif; line-height:1.65; }}
  .wrap {{ max-width:660px; margin:0 auto; }}
  h1 {{ font-size:1.5rem; font-weight:600; margin:0 0 .4rem; }}
  h2 {{ font-size:1.05rem; font-weight:600; margin:2.8rem 0 .4rem; }}
  p  {{ color:#b0a89b; font-size:.95rem; }}
  ol {{ color:#b0a89b; font-size:.95rem; padding-left:1.25rem; }}
  li {{ margin:.4rem 0; }}
  .stage {{ background:#fff; padding:28px; border-radius:6px; margin:1.4rem 0 1.6rem; }}
  code {{ background:#1d1916; padding:.1rem .35rem; border-radius:3px; color:#d98a9e; }}
  hr {{ border:0; border-top:1px solid #2c2722; margin:3rem 0 0; }}
  a {{ color:#d98a9e; }}
  .note {{ border-left:2px solid #d98a9e; padding-left:.9rem; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>Your email signature</h1>
  <p>The card is one solid image &mdash; it can&rsquo;t come apart. The two icons sit
     underneath as their own links, so Instagram and YouTube are both clickable.</p>

  <div class="stage">
{signature}
  </div>

  <h2>Putting it in Gmail</h2>
  <ol>
    <li>Click just above the card and drag down to just below the icons, so the whole
        block is highlighted.</li>
    <li><b>Copy</b> &nbsp;(Cmd&#8209;C / Ctrl&#8209;C).</li>
    <li>Go to <b>Gmail &rarr; Settings &rarr; See all settings &rarr; General</b>,
        scroll to <b>Signature</b>, and hit <b>Create new</b>.</li>
    <li><b>Paste</b> into the box, then <b>Save Changes</b> at the very bottom of the page.</li>
  </ol>

  <p class="note">One habit: after pasting, don&rsquo;t <i>drag</i> the image to move it.
     Gmail treats a drag as a cut-and-repaste and it can shuffle things. Click beside it
     and use Enter / Backspace instead.</p>

  <hr>

  <h2>Files</h2>
  <p><a href="/email-signature.png">email-signature.png</a> &mdash; the card, 1000&times;336
     (retina, displays at 500&times;168).<br>
     <a href="/sig/icon-instagram.png">icon-instagram.png</a> &middot;
     <a href="/sig/icon-youtube.png">icon-youtube.png</a> &mdash; 44&times;44 each,
     transparent background.</p>
  <p>Everything points at <code>kayleerenaud.com</code>, so the icons keep working from
     any computer &mdash; nothing is stored locally.</p>
</div>
</body>
</html>
'''

os.makedirs(os.path.join(PUB, 'email-signature'), exist_ok=True)
with open(os.path.join(PUB, 'email-signature', 'index.html'), 'w') as f:
    f.write(page)
print('  email-signature/index.html written')
