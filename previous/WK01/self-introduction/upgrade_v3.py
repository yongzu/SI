from pathlib import Path
import re
root=Path(__file__).resolve().parent
p=root/'outline-template.html'
s=p.read_text(encoding='utf-8')
assert '<main id="top">' in s and 'id="life-log"' not in s
s=re.sub(r'<style>.*?</style>',lambda m:'<style>\n'+(root/'outline-v3.css').read_text(encoding='utf-8')+'\n</style>',s,flags=re.S)
s=re.sub(r'<script>.*?</script>',lambda m:'<script>\n'+(root/'outline-v3.js').read_text(encoding='utf-8')+'\n</script>',s,flags=re.S)
start=s.index('<main id="top">');end=s.index('<ul aria-label="인생의 장면">')
s=s[:start]+'''<header class="toolbar">
<a class="brand" href="#top" aria-label="처음으로"><img src="data:image/png;base64,__MARK__" alt="" width="95" height="27"></a>
<form class="search" role="search"><input id="search" type="search" placeholder="검색" aria-label="장면과 내용 검색" autocomplete="off"><button id="clear-search" type="button" aria-label="검색 지우기" hidden>×</button></form>
<button class="profile-button" id="profile-trigger" aria-haspopup="dialog" aria-expanded="false" aria-controls="profile-panel">프로필</button>
</header>
<main id="top">
<header class="identity"><p>Self Introduce</p><h1><span class="slash">/</span>용주 조</h1><p class="description">어떤 디자인을 할 지 모르겠는 비계획적 디자이너 지망생</p></header>
<details class="log-section" id="life-log" open><summary class="log-title"><span class="log-sign" aria-hidden="true"></span><span>log</span></summary>
<p id="result-status" class="result-status" role="status" hidden></p><p id="no-results" class="empty" role="status" hidden>검색 결과가 없습니다.</p>
<ul class="scene-list" aria-label="인생의 장면">
'''+s[end+len('<ul aria-label="인생의 장면">'):]
s=s.replace('</ul>\n<details class="scene logs"','</ul>\n</details>\n<details class="scene logs"',1)
s=s.replace('<div class="log-entry"><p>v2.0', '<div class="log-entry"><p>v3.0 · 2026.09.10</p><p>변경 — 상단 소개와 들여쓴 log 목록. 호버 시 log의 점을 화살표로, 장면 앞에는 점을 표시.</p><p>추가 — 제공 이미지, 장면·본문 검색, 프로필 패널.</p></div>\n<div class="log-entry"><p>v2.0',1)
s=s.replace('<div class="cursor" aria-hidden="true"></div>', '''<dialog class="profile-panel" id="profile-panel" aria-labelledby="profile-title">
<div class="panel-header"><h2 id="profile-title">용주 조</h2><button id="close-profile" aria-label="프로필 닫기" autofocus>×</button></div>
<p>어떤 디자인을 할 지 모르겠는 비계획적 디자이너 지망생</p>
<dl><dt>출생</dt><dd>1999년 3월 11일 오전11시 출생. 사주 안믿음.</dd><dt>지금</dt><dd>무엇으로 특화할지 선택하지 못한 채 졸업(예정)</dd><dt>목표</dt><dd>Phi에 다니며 디자인 스킬과 씽킹을 극한까지 끌어올려 미친 디자이너가 되는 게 목표.</dd></dl>
<button class="panel-link" id="profile-log-link">log 보기 →</button>
</dialog>''')
p.write_text(s,encoding='utf-8')
