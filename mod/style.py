"""Translucent iMac G3 casing and Aqua controls, with no external assets."""
import streamlit as st

css = """
<style>
:root { --shell-rgb: __SHELL__; --deep-rgb: __DEEP__;
--ink:#2A363B; --muted:#56646b; --screen:#1c262a; --glow:#c4e6c1; --glow-warm:#FECEA8; --coral:#E84A5F;
--sans: 'Lucida Grande','Lucida Sans Unicode','Helvetica Neue',Helvetica,Arial,sans-serif;
--mono: ui-monospace,'SF Mono',Menlo,Consolas,'Courier New',monospace; }

/* Page and shell */
.stApp {background:radial-gradient(ellipse at 50% 12%,#fff 0%,#f4f6f7 55%,#e3e9eb 100%);color:var(--ink);font-family:var(--sans)}
header[data-testid="stHeader"] {background:transparent}
[data-testid="stAppDeployButton"],[data-testid="stToolbarActions"] {display:none!important}
.stApp p,.stApp li,.stApp label,.stApp input,.stApp td,.stApp th {font-family:var(--sans);color:var(--ink)}
.stApp p,.stApp li,.stApp label {font-size:.95rem;line-height:1.55}
[data-testid="stMainBlockContainer"] {
max-width:760px!important;margin:2rem auto 3rem;padding:1.8rem 2.2rem 1.6rem!important;
border-radius:56px 56px 96px 96px;border:2px solid rgba(255,255,255,.95);
background:linear-gradient(135deg,rgba(255,255,255,.84),rgba(255,255,255,.08) 38%,rgba(255,255,255,.34) 64%,rgba(255,255,255,.1)),linear-gradient(180deg,rgba(var(--shell-rgb),.56),rgba(var(--shell-rgb),.94));
box-shadow:inset 0 3px 2px #fff,inset 0 0 0 8px rgba(255,255,255,.24),inset 0 -18px 34px rgba(var(--deep-rgb),.26),0 34px 55px -24px #65777c80,0 2px 0 #fff;
}
[data-testid="stMainBlockContainer"]::after {content:"";display:block;width:34%;height:24px;margin:1.6rem auto 0;border-radius:30px;background:radial-gradient(circle,#2a363b66 1px,transparent 1.6px) 0 0/6px 6px;border:1px solid #ffffffb3;box-shadow:inset 0 2px 4px #2a363b26}

/* Header */
.bezel {position:relative;text-align:center;background:linear-gradient(#fff,#eef1f1);border:1px solid #fff;border-radius:32px 32px 18px 18px;padding:1.6rem 1rem 1.3rem;box-shadow:0 6px 12px #2a363b1a,inset 0 -2px 4px #2a363b0d;margin-bottom:1rem}
.bezel-title {font-family:var(--sans);font-size:clamp(1.8rem,5.4vw,2.6rem);font-weight:600;letter-spacing:-.045em;line-height:1.1;color:var(--ink)}
.bezel .bezel-sub {font-size:.88rem!important;color:var(--muted)!important;margin:.55rem auto 0!important;max-width:330px;text-align:center}
.bezel-led {position:absolute;right:22px;top:22px;width:8px;height:8px;border-radius:50%;background:#8fc47a;box-shadow:0 0 7px #8fc47a,inset 0 1px 1px #fff;animation:breathe 3.2s ease-in-out infinite}
@keyframes breathe {0%,100%{opacity:1}50%{opacity:.45}}

/* Menu: centered dock */
.st-key-nav {align-items:center!important;margin-bottom:.3rem}
.part-name {font:600 .8rem var(--sans);margin:1.1rem 0 .5rem;color:var(--ink)}

/* Display: dark recessed CRT */
.lcd-frame {background:linear-gradient(#fff,#e4ebeb);border:1px solid #fff;border-radius:28px;padding:14px 14px 10px;box-shadow:0 8px 16px #2a363b26,inset 0 -2px 3px #2a363b14;margin:.4rem 0 .8rem}
.lcd {position:relative;overflow:hidden;background:radial-gradient(ellipse at 50% 30%,#3a4b51 0%,#26343a 55%,#182125 100%);border:1px solid #0e1518;border-radius:20px;padding:1.1rem 1.4rem 1.2rem;color:var(--glow);font-family:var(--mono);box-shadow:inset 0 0 44px #000b,inset 0 3px 10px #000c,0 1px 0 #fff}
.lcd::before {content:"";position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(0deg,rgba(255,255,255,.04) 0 1px,transparent 1px 3px)}
.lcd::after {content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(128deg,#ffffff26,transparent 38%)}
.lcd>* {position:relative;z-index:1}
.lcd-row {display:flex;justify-content:space-between;gap:1rem;font:.78rem/1.6 var(--sans);color:#93a9ae}
.lcd-caption {font:.85rem var(--sans);margin-top:1.3rem;color:#a9bcc0}
.lcd-big {font-family:var(--mono);font-size:clamp(2.8rem,11vw,4.8rem);font-weight:bold;letter-spacing:-.05em;line-height:1.15;margin:.2rem 0 .7rem;font-variant-numeric:tabular-nums;color:var(--glow);text-shadow:0 0 6px #c4e6c199,0 0 22px #99B89888}
.lcd-feedback {font:.92rem var(--sans);min-height:1.5rem;color:#d3e0e2}
.lcd-feedback.warn {color:#ffb3a9}.lcd-feedback.win {color:#d7f0d3}
.lcd.win .lcd-big {color:#e4f8e0;text-shadow:0 0 8px #e4f8e0aa,0 0 30px #99B898}
.lcd.lose .lcd-big {color:#ff9d94;text-shadow:0 0 8px #ff847caa,0 0 28px #E84A5F99}
.lcd-brand {display:flex;justify-content:space-between;align-items:center;margin:9px 6px 0;font:600 .68rem var(--sans);color:#66797f;letter-spacing:.02em}
.lcd-brand i {display:inline-block;width:6px;height:6px;border-radius:50%;background:#8fc47a;box-shadow:0 0 5px #8fc47a;margin-left:6px;vertical-align:1px}
.cells {display:flex;flex-wrap:wrap;justify-content:flex-end;gap:4px;max-width:200px!important;margin-top:6px}
.cell {width:8px;height:8px;border-radius:50%;background:var(--glow);box-shadow:0 0 5px #c4e6c1aa}
.cell.used {background:#34444a;box-shadow:inset 0 1px 2px #000a}

/* Range bar and heat LEDs */
.track {position:relative;height:18px;overflow:hidden;border-radius:20px;background:#f1f5f4;border:1px solid #ffffffd9;box-shadow:inset 0 2px 5px #2a363b40}
.window {position:absolute;top:2px;bottom:2px;min-width:4px;border-radius:20px;background:linear-gradient(#ffffffd9,rgb(var(--shell-rgb)) 55%,rgb(var(--deep-rgb)));box-shadow:0 1px 2px #2a363b40;transition:left .3s,width .3s}
.tick {position:absolute;inset:0 auto;width:2px;background:#2a363b80}.tick.secret {background:#fff;box-shadow:0 0 0 1px #2a363b}
.track-scale {display:flex;justify-content:space-between;font:.7rem var(--sans);margin-top:5px;color:var(--muted)}
.heat-row {display:flex;align-items:center;gap:14px}
.heat-leds {flex:1;display:grid;grid-template-columns:repeat(5,1fr);gap:6px;padding:5px 6px;border-radius:20px;background:#e9eff0;border:1px solid #ffffffd9;box-shadow:inset 0 2px 5px #2a363b40}
.led {height:10px;border-radius:10px;background:#c5d1d3;box-shadow:inset 0 1px 2px #2a363b40}
.led.on {box-shadow:0 0 6px var(--c),inset 0 1px 1px #ffffff99;background:linear-gradient(#ffffffaa,var(--c) 60%)}
.heat-label {font:600 .8rem var(--sans);width:78px;text-align:right}
.chips {display:flex;flex-wrap:wrap;gap:6px}.chip {font:.85rem var(--mono);padding:5px 12px;background:#ffffffc0;border:1px solid #ffffffcc;border-radius:20px;box-shadow:0 2px 3px #2a363b18}.chip.hit {background:var(--ink);color:#fff}.chip.hint {border-style:dashed;font-family:var(--sans)}.chip.up {border-left:3px solid #FF847C}.chip.down {border-left:3px solid #99B898}.empty-note {font:.8rem var(--sans);color:#415358}

/* Aqua controls */
[data-testid^="stBaseButton-primary"],[data-testid^="stBaseButton-secondary"] {min-height:46px;border-radius:26px!important;background:linear-gradient(#fff 0%,#f7f8f8 48%,#dce3e4 51%,#f5f7f7 100%)!important;border:1px solid #9aabad!important;box-shadow:inset 0 1px 1px #fff,0 3px 6px #2a363b2e;color:var(--ink)!important;transition:transform .12s,filter .12s}
[data-testid^="stBaseButton-primary"] {background:linear-gradient(#ffe9e6 0%,#ffb4aa 46%,#f17470 50%,#ffb0a3 100%)!important;border-color:#b85655!important}
[data-testid^="stBaseButton-primary"]:hover,[data-testid^="stBaseButton-secondary"]:hover {filter:brightness(1.04)}
.stApp button p {font:600 .85rem var(--sans)!important;color:var(--ink)!important}
.stApp button:disabled {opacity:.45}
[data-testid^="stBaseButton-primary"]:active,[data-testid^="stBaseButton-secondary"]:active {transform:translateY(2px);box-shadow:inset 0 2px 4px #2a363b33}
.stApp button[kind^="segmented_control"] {background:linear-gradient(#fff,#e8eded)!important;border-color:#9dafb2!important;min-height:40px;color:var(--ink)!important;padding:.3rem .8rem!important}
.stApp button[kind="segmented_controlActive"] {background:linear-gradient(#ffffffd9,rgba(var(--shell-rgb),.8))!important;box-shadow:inset 0 1px 3px #2a363b40}
.stApp button[kind^="segmented_control"] p {font-size:.78rem!important}
.stApp [data-baseweb="input"],.stApp [data-baseweb="base-input"] {background:#f9fbfb!important;border-radius:14px!important}
.stApp [data-baseweb="input"] {border:1px solid #97aeb3!important;box-shadow:inset 0 2px 4px #2a363b1f}
.stNumberInput input {font:bold 1.4rem var(--mono)!important;text-align:center}.stTextInput input {font-size:.95rem!important}
[data-testid="InputInstructions"] {display:none}
[data-testid="stForm"] {border:none;padding:0}
[data-testid="stExpander"] {border:1px solid #ffffff99;border-radius:18px;background:#ffffff33;margin-top:.9rem}
[data-testid="stExpander"] summary p {font-size:.8rem!important}
.stApp button:focus-visible,.stApp input:focus-visible {outline:3px solid #285e80!important;outline-offset:3px}

/* Cards, stats, tables */
.pearl {background:linear-gradient(#fffffff2,#edf2f2e6);border:1px solid #fff;border-radius:20px;padding:1rem 1.2rem;margin-bottom:.75rem;box-shadow:0 4px 10px #2a363b16}
.rules p:last-child {margin-bottom:0}
.stats {display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.stat {text-align:center;padding:1rem .5rem;margin:0}.stat-value {font:600 1.4rem var(--sans);overflow-wrap:anywhere}.stat-name {font:.72rem var(--sans);color:var(--muted);margin-top:5px}
.table-wrap {overflow-x:auto}.retro-table {width:100%;border-collapse:collapse;font:.85rem var(--sans)}.retro-table th {text-align:left;font-size:.72rem;color:var(--muted);padding:.6rem .5rem;border-bottom:1px solid #c1ced1}.retro-table td {padding:.6rem .5rem;white-space:nowrap;border-bottom:1px solid #dbe3e5}.retro-table tbody tr:last-child td {border-bottom:none}.retro-table .num {text-align:right;font-variant-numeric:tabular-nums}.badge {padding:3px 9px;border-radius:12px}.badge.won {background:#dae9d6;color:#315c30}.badge.lost {background:#f7dddc;color:#8b303d}

@media(max-width:640px) {[data-testid="stMainBlockContainer"] {max-width:calc(100% - 20px)!important;margin:1rem auto;padding:1.1rem 1rem 1.4rem!important;border-radius:34px 34px 60px 60px}.stats {grid-template-columns:repeat(2,1fr)}.lcd {padding:1rem}.bezel {padding:1.4rem .6rem 1rem}.lcd-row {gap:.5rem}.heat-label {width:64px}}
@media(prefers-reduced-motion:reduce) {*,*::before,*::after {animation:none!important;transition:none!important}}
</style>
"""


def inject_style(flavor, background_gif=None, background_light=None):
    shell = ','.join(map(str, flavor['rgb']))
    deep = ','.join(map(str, flavor['deep']))
    st.markdown(css.replace('__SHELL__', shell).replace('__DEEP__', deep), unsafe_allow_html=True)
