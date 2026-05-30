import json, re, csv

src = open('index.html', encoding='utf-8', errors='replace').read()

def balanced(i):
    open_ch = src[i]; close_ch = '}' if open_ch == '{' else ']'
    depth = 0; in_str = False; esc = False; q = ''; start = i
    while i < len(src):
        c = src[i]
        if in_str:
            if esc: esc = False
            elif c == '\\': esc = True
            elif c == q: in_str = False
        else:
            if c in '"\'': in_str = True; q = c
            elif c == open_ch: depth += 1
            elif c == close_ch:
                depth -= 1
                if depth == 0:
                    return src[start:i+1]
        i += 1
    return None

def extract(varname):
    # the DEFINITION is `<var> = {` or `<var> = [`  (optionally preceded by `var `)
    for m in re.finditer(r'\b' + re.escape(varname) + r'\s*=\s*([\{\[])', src):
        raw = balanced(m.start(1))
        if raw:
            try:
                return json.loads(raw)
            except Exception as e:
                print(varname, 'parse-fail', e)
    return None

results = {}
for v in ['_Flourish_data', '_Flourish_data_column_names', '_Flourish_settings']:
    val = extract(v)
    results[v] = val
    print(v, 'OK' if val is not None else 'MISSING',
          type(val).__name__ if val is not None else '')

json.dump(results, open('flourish_data_full.json', 'w'))

# ---- Build deliverables ----
data = results['_Flourish_data']
# data is a dict keyed by dataset name -> {column_name: [rows...]}  OR {regions:[...]}
print('\n_Flourish_data top keys:', list(data.keys()) if isinstance(data, dict) else type(data))
