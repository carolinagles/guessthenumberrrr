"""Translucent iMac G3 casing and Aqua controls, with no external assets."""
import streamlit as st

css = """
<style>
:root { --shell-rgb: __SHELL__; --deep-rgb: __DEEP__; --ink:#2A363B; --muted:#56646b;
--sans: 'Lucida Grande','Lucida Sans Unicode',Helvetica,Arial,sans-serif;
--mono: 'Courier New',monospace; }
.stApp {background:radial-gradient(ellipse at 50% 15%,#fff 0%,#f4f6f7 55%,#e6ebed 100%);color:var(--ink);font-family:var(--sans)}
header[data-testid="stHeader"] {background:transparent}
.stApp p,.stApp li,.stApp label,.stApp input,.stApp td,.stApp th {font-family:var(--sans);color:var(--ink)}
.stApp p,.stApp li,.stApp label {font-size:.95rem;line-height:1.55}
[data-testid="stMainBlockContainer"] {
max-width:760px!important;margin:2.5rem auto 3rem;padding:1.8rem 2.2rem 2rem!important;
border-radius:52px 52px 92px 92px;border:2px solid rgba(255,255,255,.95);
background:linear-gradient(135deg,rgba(255,255,255,.84),rgba(255,255,255,.1) 40%,rgba(255,255,255,.35) 65%,rgba(255,255,255,.12)),linear-gradient(180deg,rgba(var(--shell-rgb),.56),rgba(var(--shell-rgb),.92));
box-shadow:inset 0 3px 2px #fff,inset 0 0 0 8px rgba(255,255,255,.24),inset 0 -15px 30px rgba(var(--deep-rgb),.24),0 30px 55px -22px #65777c66;
}
[data-testid="stMainBlockContainer"]::after {content:"";display:block;width:34%;height:24px;margin:1.8rem auto 0;border-radius:30px;background:radial-gradient(circle,#2a363b66 1px,transparent 1.6px) 0 0/6px 6px;border:1px solid #ffffffb3;box-shadow:inset 0 2px 4px #2a363b26}
.bezel {position:relative;text-align:center;background:linear-gradient(#fff,#eef1f1);border:1px solid #fff;border-radius:30px 30px 16px 16px;padding:1.5rem 1rem 1.1rem;box-shadow:0 5px 10px #2a363b14; margin-bottom:.5rem}
.bezel-title {font-family:var(--sans);font-size:clamp(1.7rem,5vw,2.5rem);font-weight:600;letter-spacing:-.065em;line-height:1.15;color:var(--ink)}
.bezel-sub {font-size:.85rem!important;color:var(--muted)!important;margin:.6rem auto 0;max-width:350px}
.bezel-led {position:absolute;right:20px;top:20px;width:7px;height:7px;border-radius:50%;background:#8aac72;box-shadow:0 0 5px #8aac7266,inset 0 1px 1px #fff}
.part-name {font:600 .8rem var(--sans);margin:1rem 0 .5rem;color:var(--ink)}
.lcd-frame {background:linear-gradient(#fff,#e8eeee);border:1px solid #fff;border-radius:24px;padding:14px 14px 9px;box-shadow:0 7px 15px #2a363b20;margin:.5rem 0 .6rem}
.lcd {position:relative;overflow:hidden;background:linear-gradient(135deg,#f8fcfc,#e5eff1);border:1px solid #b8c9cd;border-radius:12px;padding:1.1rem 1.3rem;color:var(--ink);font-family:var(--sans);box-shadow:inset 0 2px 7px #2a363b14}
.lcd::after {content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(125deg,#ffffff66,transparent 48%)}
.lcd>* {position:relative;z-index:1}
.lcd-row {display:flex;justify-content:space-between;gap:1rem;font-size:.78rem;line-height:1.6;color:var(--muted)}
.lcd-caption {font-size:.85rem;margin-top:1.5rem;color:var(--muted)}
.lcd-big {font-family:var(--mono);font-size:clamp(2.8rem,10vw,4.5rem);font-weight:bold;letter-spacing:-.065em;line-height:1.2;margin:.25rem 0 .6rem;font-variant-numeric:tabular-nums}
.lcd-feedback {font-size:.9rem;min-height:1.5rem}
.lcd-feedback.warn {color:#a92e43}.lcd-feedback.win {color:#37653a}
.lcd-brand {display:flex;justify-content:space-between;margin:8px 5px 0;font:600 .6rem var(--sans);color:#66797f;text-transform:uppercase;letter-spacing:.15em}
.cells {display:flex;flex-wrap:wrap;gap:3px;max-width:180px!important;margin-top:5px}
.cell {width:7px;height:9px;border-radius:3px;background:#607c82}.cell.used {background:#ccd8db}
.track {position:relative;height:16px;overflow:hidden;border-radius:20px;background:#f1f5f4;border:1px solid #ffffffd9;box-shadow:inset 0 2px 4px #2a363b33}
.window {position:absolute;top:2px;bottom:2px;min-width:4px;border-radius:20px;background:linear-gradient(#ffffffc9,rgb(var(--shell-rgb)) 55%,rgb(var(--deep-rgb)));transition:left .25s,width .25s}
.tick {position:absolute;inset:0 auto;width:2px;background:#2a363b80}.tick.secret {background:#fff;box-shadow:0 0 0 1px #2a363b}
.track-scale {display:flex;justify-content:space-between;font: .7rem var(--sans);margin-top:5px}
.heat-row {display:flex;align-items:center;gap:12px}.heat-row .track {flex:1}.heat-label {font: .75rem var(--sans);width:75px;text-align:right}
.heat-fill {position:absolute;top:2px;bottom:2px;left:3px;border-radius:20px;background:linear-gradient(90deg,#99B898,#FECEA8,#FF847C,#E84A5F);transition:width .25s}
.chips {display:flex;flex-wrap:wrap;gap:6px}.chip {font:.85rem var(--sans);padding:5px 12px;background:#ffffffb3;border:1px solid #ffffffcc;border-radius:20px;box-shadow:0 2px 3px #2a363b14}.chip.hit {background:#2a363b;color:#fff}.chip.hint {border-style:dashed}.empty-note {font:.8rem var(--sans);color:#415358}
[data-testid^="stBaseButton-primary"],[data-testid^="stBaseButton-secondary"] {min-height:44px;border-radius:24px!important;background:linear-gradient(#fff 0%,#f7f8f8 48%,#dce3e4 51%,#f5f7f7 100%)!important;border:1px solid #9aabad!important;box-shadow:inset 0 1px 1px #fff,0 3px 5px #2a363b26;color:var(--ink)!important;transition:transform .15s}
[data-testid^="stBaseButton-primary"] {background:linear-gradient(#ffe6e3 0%,#ffb4aa 46%,#f17470 50%,#ffb0a3 100%)!important;border-color:#b85655!important}
.stApp button p {font:600 .82rem var(--sans)!important;color:var(--ink)!important}
.stApp button:disabled {opacity:.45}
[data-testid^="stBaseButton-primary"]:active,[data-testid^="stBaseButton-secondary"]:active {transform:translateY(2px)}
.stApp button[kind^="segmented_control"] {background:linear-gradient(#fff,#e8eded)!important;border-color:#9dafb2!important;min-height:38px;color:var(--ink)!important;padding:.3rem .65rem!important}
.stApp button[kind="segmented_controlActive"] {background:linear-gradient(#ffffffd9,rgba(var(--shell-rgb),.75))!important;box-shadow:inset 0 1px 3px #2a363b33}
.stApp button[kind^="segmented_control"] p {font-size:.75rem!important}
.stApp [data-baseweb="input"],.stApp [data-baseweb="base-input"] {background:#f9fbfb!important;border-radius:12px!important}
.stApp [data-baseweb="input"] {border:1px solid #97aeb3!important;box-shadow:inset 0 2px 3px #2a363b14}
.stNumberInput input {font-size:1.3rem!important;text-align:center}.stTextInput input {font-size:.95rem!important}
[data-testid="stForm"] {border:none;padding:0}
.stApp button:focus-visible,.stApp input:focus-visible {outline:3px solid #285e80!important;outline-offset:3px}
.pearl {background:linear-gradient(#fffffff2,#edf2f2e6);border:1px solid #fff;border-radius:18px;padding:1rem 1.2rem;margin-bottom:.75rem;box-shadow:0 3px 8px #2a363b14}
.stats {display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.stat {text-align:center;padding:1rem .5rem}.stat-value {font:600 1.35rem var(--sans);overflow-wrap:anywhere}.stat-name {font:.72rem var(--sans);color:var(--muted);margin-top:5px}
.table-wrap {overflow-x:auto}.retro-table {width:100%;border-collapse:collapse;font:.85rem var(--sans)}.retro-table th {text-align:left;font-size:.7rem;color:var(--muted);padding:.6rem .5rem;border-bottom:1px solid #c1ced1}.retro-table td {padding:.6rem .5rem;white-space:nowrap;border-bottom:1px solid #dbe3e5}.retro-table .num {text-align:right}.badge {padding:3px 8px;border-radius:12px}.badge.won {background:#dae9d6;color:#315c30}.badge.lost {background:#f7dddc;color:#8b303d}
@media(max-width:640px) {[data-testid="stMainBlockContainer"] {max-width:calc(100% - 20px)!important;margin:1rem auto;padding:1.1rem 1rem 1.5rem!important;border-radius:32px 32px 56px 56px}.stats {grid-template-columns:repeat(2,1fr)}.lcd {padding:1rem}.bezel {padding:1.4rem .6rem 1rem}.lcd-row {gap:.5rem}}
@media(prefers-reduced-motion:reduce) {*,*::before,*::after {animation:none!important;transition:none!important}}
</style>
"""


def inject_style(flavor, background_gif=None, background_light=None):
    shell = ','.join(map(str, flavor['rgb']))
    deep = ','.join(map(str, flavor['deep']))
    st.markdown(css.replace('__SHELL__', shell).replace('__DEEP__', deep), unsafe_allow_html=True)
