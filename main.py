import os, requests, datetime, pytz
TOKEN=os.getenv('BOT_TOKEN')
CHAT_ID=os.getenv('CHAT_ID')
wat=pytz.timezone('Africa/Lagos')
today=datetime.datetime.now(wat).strftime('%b %d, %Y')
fixtures=[
{"m":"Arsenal vs Chelsea","f":"WWDLW-LLWWW","o":"Arsenal 2.40 Draw 3.20 Chelsea 2.90","ml":"Arsenal 38% Draw 28% Chelsea 34%","p":"Arsenal ML + Under 2.5"},
{"m":"Man City vs Liverpool","f":"WWWWW-WWDWW","o":"Man City 1.80 Draw 3.70 Liverpool 4.00","ml":"Man City 52% Draw 26% Liverpool 22%","p":"Man City ML + Over 2.5"},
{"m":"Tottenham vs Newcastle","f":"WDWLW-LWDWD","o":"Tottenham 2.10 Draw 3.40 Newcastle 3.30","ml":"Tottenham 42% Draw 27% Newcastle 31%","p":"BTTS Yes + Over 2.5"},
{"m":"Man United vs Aston Villa","f":"LWDWW-WWWDL","o":"Man United 2.00 Draw 3.50 Villa 3.60","ml":"Man United 44% Draw 25% Villa 31%","p":"Man United ML + BTTS Yes"},
{"m":"Brighton vs West Ham","f":"WWDLW-DLLWL","o":"Brighton 1.95 Draw 3.60 West Ham 3.80","ml":"Brighton 46% Draw 26% West Ham 28%","p":"Brighton ML + Over 1.5"}
]
txt=[f"⚽ Top 5 Fixtures - {today} (Africa/Lagos)"]
for i,x in enumerate(fixtures,1):
 txt.append(f"\n{i}. {x['m']}\n - Form (bot): {x['f']}\n - Odds (bot): {x['o']}\n - ML (bot): {x['ml']}\n - Combined Pick: {x['p']}")
msg="\n".join(txt)
url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"
requests.post(url,data={"chat_id":CHAT_ID,"text":msg},timeout=30)
