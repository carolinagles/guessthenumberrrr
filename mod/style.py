"""
Style

- Translucent candy shell (like late 90s computers)
- Pearl white bezel and handheld-console LCD screen
- Chunky press buttons
- The shell color changes with the selected flavor
"""
import streamlit as st


css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Silkscreen:wght@400;700&family=VT323&display=swap');

:root {
  --shell-rgb: __SHELL__;
  --deep-rgb: __DEEP__;
  --pearl: #F4F6F8;
  --ink: #1F2430;
  --muted: #5A6270;
  --lcd: #A9B98F;
  --lcd-ink: #26301E;
}

/* Page */
.stApp {
  background:
    radial-gradient(1100px 520px at 50% -180px, #FFFFFF 0%, rgba(255,255,255,0) 70%),
    linear-gradient(180deg, #EEF1F4 0%, #D9DFE6 100%);
  color: var(--ink);
}
header[data-testid="stHeader"] { background: transparent; }

.stApp p, .stApp li, .stApp label, .stApp input, .stApp td, .stApp th {
  font-family: 'VT323', ui-monospace, monospace;
}
.stApp p, .stApp li, .stApp label { font-size: 1.3rem; line-height: 1.25; }

/* The translucent shell */
[data-testid="stMainBlockContainer"] {
  max-width: 820px !important;
  margin: 2.5rem auto 3rem;
  padding: 1.75rem 2.25rem 2.25rem !important;
  border-radius: 56px 56px 150px 150px / 56px 56px 100px 100px;
  background:
    linear-gradient(160deg, rgba(255,255,255,.55) 0%, rgba(255,255,255,0) 34%),
    repeating-linear-gradient(0deg, rgba(var(--deep-rgb),.07) 0 2px, transparent 2px 26px),
    linear-gradient(180deg, rgba(var(--shell-rgb),.28) 0%, rgba(var(--shell-rgb),.64) 100%);
  border: 1.5px solid rgba(255,255,255,.75);
  box-shadow:
    inset 0 2px 0 rgba(255,255,255,.9),
    inset 0 -36px 70px rgba(var(--deep-rgb),.30),
    0 46px 80px -34px rgba(var(--deep-rgb),.65);
  backdrop-filter: blur(16px) saturate(140%);
  -webkit-backdrop-filter: blur(16px) saturate(140%);
}
/* Speaker grille at the bottom of the shell */
[data-testid="stMainBlockContainer"]::after {
  content: "";
  display: block;
  width: 44%;
  height: 34px;
  margin: 1.75rem auto 0;
  border-radius: 999px;
  background: radial-gradient(circle, rgba(var(--deep-rgb),.6) 1.6px, transparent 2.3px) 0 0 / 9px 9px;
  border: 1.5px solid rgba(255,255,255,.6);
  box-shadow: inset 0 2px 6px rgba(var(--deep-rgb),.25);
}

/* Pearl bezel (header) */
.bezel {
  position: relative;
  text-align: center;
  background: linear-gradient(180deg, #FFFFFF 0%, #EEF1F4 62%, #E1E6EC 100%);
  border-radius: 38px 38px 22px 22px;
  padding: 1.5rem 1.5rem 1.2rem;
  box-shadow: inset 0 -3px 0 rgba(0,0,0,.05), 0 12px 26px -16px rgba(var(--deep-rgb),.8);
  margin-bottom: 1.1rem;
}
.bezel-title {
  font-family: 'Silkscreen', ui-monospace, monospace;
  font-weight: 700;
  font-size: clamp(1.7rem, 5.4vw, 2.9rem);
  line-height: 1.05;
  margin: 0;
  color: var(--ink);
  text-shadow: 3px 3px 0 rgba(var(--shell-rgb),.45);
}
.bezel-sub { font-family: 'VT323', monospace; font-size: 1.35rem; color: var(--muted); margin: .45rem 0 0; }
.bezel-led {
  position: absolute; top: 20px; right: 26px;
  width: 12px; height: 12px; border-radius: 50%;
  background: rgb(var(--shell-rgb));
  box-shadow: 0 0 10px rgba(var(--shell-rgb),.95), inset 0 1px 1px rgba(255,255,255,.8);
}

/* Small section names */
.part-name {
  font-family: 'Silkscreen', ui-monospace, monospace;
  font-size: .85rem;
  color: var(--ink);
  margin: 1rem 0 .35rem;
}

/* LCD screen */
.lcd-frame {
  background: linear-gradient(180deg, #3A404B 0%, #262B33 100%);
  border-radius: 22px 22px 34px 22px;
  padding: 14px 14px 8px;
  box-shadow: inset 0 2px 0 rgba(255,255,255,.14), 0 6px 0 rgba(0,0,0,.18);
  margin: .25rem 0 .5rem;
}
.lcd {
  background-color: var(--lcd);
  background-image: repeating-linear-gradient(0deg, rgba(38,48,30,.07) 0 1px, transparent 1px 3px);
  border-radius: 10px;
  padding: .8rem 1.15rem 1rem;
  color: var(--lcd-ink);
  font-family: 'VT323', ui-monospace, monospace;
  box-shadow: inset 0 3px 12px rgba(0,0,0,.28);
}
.lcd-row { display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; font-size: 1.25rem; }
.lcd-caption { font-size: 1.35rem; margin-top: .7rem; }
.lcd-big { font-size: clamp(3.2rem, 12vw, 5.6rem); line-height: .95; letter-spacing: .02em; }
.lcd-feedback { font-size: 1.5rem; min-height: 1.7rem; margin-top: .35rem; }
.lcd-feedback.warn::before { content: "! "; }
.lcd-brand {
  font-family: 'Silkscreen', ui-monospace, monospace;
  font-size: .7rem; color: #9AA3B1; margin: 6px 4px 0;
  display: flex; justify-content: space-between;
}
.lcd-brand span:last-child { color: rgb(var(--shell-rgb)); }
.cells { display: flex; flex-wrap: wrap; gap: 3px; max-width: 58%; justify-content: flex-end; }
.cell { width: 10px; height: 14px; background: var(--lcd-ink); border-radius: 1px; }
.cell.used { background: rgba(38,48,30,.14); }
.lcd.win .lcd-big { animation: blink .45s steps(1) 6; }
@keyframes blink { 50% { opacity: 0; } }

/* Range scanner and heat meter */
.track {
  position: relative; height: 26px; border-radius: 999px; overflow: hidden;
  background: rgba(255,255,255,.55);
  border: 1.5px solid rgba(255,255,255,.85);
  box-shadow: inset 0 2px 6px rgba(var(--deep-rgb),.28);
}
.window {
  position: absolute; top: 3px; bottom: 3px; border-radius: 999px; min-width: 6px;
  background: linear-gradient(180deg, rgba(255,255,255,.75) 0%, rgba(var(--shell-rgb),.95) 55%, rgb(var(--deep-rgb)) 100%);
  transition: left .45s ease, width .45s ease;
}
.tick { position: absolute; top: 0; bottom: 0; width: 2px; background: var(--ink); opacity: .5; }
.tick.secret { background: #FFFFFF; width: 4px; opacity: 1; box-shadow: 0 0 0 1.5px var(--ink); }
.track-scale { display: flex; justify-content: space-between; font-family: 'VT323', monospace; font-size: 1.1rem; color: var(--ink); opacity: .75; }
.heat-fill {
  position: absolute; top: 3px; bottom: 3px; left: 3px; border-radius: 999px;
  background: linear-gradient(90deg, #5BC0EB 0%, #FDE74C 55%, #F25F5C 100%);
  background-size: 640px 100%;
  transition: width .45s ease;
}
.heat-row { display: flex; align-items: center; gap: .8rem; }
.heat-row .track { flex: 1; }
.heat-label { font-family: 'Silkscreen', monospace; font-size: .85rem; min-width: 6.5rem; text-align: right; }

/* Guess history chips */
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip {
  font-family: 'VT323', monospace; font-size: 1.3rem; padding: 1px 12px;
  border-radius: 999px; background: rgba(255,255,255,.72);
  border: 1.5px solid rgba(var(--deep-rgb),.35); color: var(--ink);
}
.chip.hit { background: rgb(var(--shell-rgb)); color: #FFFFFF; border-color: rgb(var(--deep-rgb)); }
.chip.hint { background: transparent; border-style: dashed; }
.empty-note { font-family: 'VT323', monospace; font-size: 1.25rem; opacity: .7; }

/* Buttons */
[data-testid^="stBaseButton-secondary"], [data-testid^="stBaseButton-primary"] {
  border-radius: 999px !important;
  min-height: 2.9rem;
  padding: .45rem 1.4rem !important;
  color: var(--ink) !important;
  background: linear-gradient(180deg, #FFFFFF 0%, #E6EAEF 100%) !important;
  border: 1.5px solid rgba(var(--deep-rgb),.35) !important;
  box-shadow: inset 0 1px 0 #FFFFFF, 0 4px 0 rgba(var(--deep-rgb),.35);
  transition: transform .06s ease, box-shadow .06s ease;
}
[data-testid^="stBaseButton-primary"] {
  color: #FFFFFF !important;
  background: linear-gradient(180deg, rgba(255,255,255,.45) 0%, rgb(var(--shell-rgb)) 42%, rgb(var(--deep-rgb)) 100%) !important;
  border-color: rgb(var(--deep-rgb)) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.6), 0 4px 0 rgb(var(--deep-rgb));
}
[data-testid^="stBaseButton-secondary"]:active, [data-testid^="stBaseButton-primary"]:active {
  transform: translateY(3px);
  box-shadow: inset 0 1px 0 #FFFFFF, 0 1px 0 rgba(var(--deep-rgb),.5);
}
[data-testid^="stBaseButton-secondary"]:disabled { opacity: .45; }
.stApp button p {
  font-family: 'Silkscreen', ui-monospace, monospace !important;
  font-size: .9rem !important;
}

/* Segmented controls (menus) */
[data-testid^="stBaseButton-segmented_control"] {
  background: rgba(255,255,255,.6) !important;
  border-color: rgba(var(--deep-rgb),.3) !important;
  color: var(--ink) !important;
}
[data-testid="stBaseButton-segmented_controlActive"] {
  background: linear-gradient(180deg, rgba(255,255,255,.4) 0%, rgb(var(--shell-rgb)) 50%, rgb(var(--deep-rgb)) 100%) !important;
  color: #FFFFFF !important;
}
[data-testid="stBaseButton-segmented_controlActive"] p { color: #FFFFFF !important; }

/* Inputs */
.stApp [data-baseweb="input"], .stApp [data-baseweb="base-input"] {
  background: rgba(255,255,255,.8) !important;
  border-radius: 14px !important;
}
.stApp [data-baseweb="input"] { border: 1.5px solid rgba(var(--deep-rgb),.35) !important; }
.stNumberInput input { font-size: 2rem !important; text-align: center; }
.stTextInput input { font-size: 1.5rem !important; }
[data-testid="stForm"] { border: none; padding: 0; }

/* Focus */
.stApp button:focus-visible, .stApp input:focus-visible {
  outline: 3px solid rgb(var(--deep-rgb)) !important;
  outline-offset: 2px;
}

/* Pearl panels: stats, tables, rules */
.pearl {
  background: linear-gradient(180deg, rgba(255,255,255,.92) 0%, rgba(240,243,246,.88) 100%);
  border-radius: 22px;
  padding: 1rem 1.2rem;
  box-shadow: inset 0 -2px 0 rgba(0,0,0,.05), 0 8px 18px -12px rgba(var(--deep-rgb),.7);
  margin-bottom: .8rem;
}
.stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: .6rem; }
.stat { text-align: center; padding: .7rem .4rem; }
.stat-value { font-family: 'Silkscreen', monospace; font-size: 1.35rem; color: var(--ink); overflow-wrap: anywhere; }
.stat-name { font-family: 'VT323', monospace; font-size: 1.15rem; color: var(--muted); }
@media (max-width: 640px) {
  .stats { grid-template-columns: repeat(2, 1fr); }
  [data-testid="stMainBlockContainer"] { padding: 1.25rem 1rem 1.75rem !important; border-radius: 34px 34px 80px 80px; }
}

.table-wrap { overflow-x: auto; }
.retro-table { width: 100%; border-collapse: collapse; font-family: 'VT323', monospace; font-size: 1.2rem; }
.retro-table th {
  font-family: 'Silkscreen', monospace; font-size: .72rem; font-weight: 400;
  text-align: left; padding: .35rem .5rem; color: var(--muted);
  border-bottom: 2px solid rgba(var(--deep-rgb),.35);
}
.retro-table td { padding: .25rem .5rem; border-bottom: 1px dashed rgba(31,36,48,.15); white-space: nowrap; }
.retro-table td.num, .retro-table th.num { text-align: right; }
.badge { padding: 0 10px; border-radius: 999px; }
.badge.won { background: rgb(var(--shell-rgb)); color: #FFFFFF; }
.badge.lost { background: #E3E7EC; color: var(--muted); }

.rules p, .rules li { color: var(--ink); }

@media (prefers-reduced-motion: reduce) {
  .lcd.win .lcd-big { animation: none; }
  .window, .heat-fill { transition: none; }
}
</style>
"""


def inject_style(flavor):
    shell = ",".join(str(value) for value in flavor['rgb'])
    deep = ",".join(str(value) for value in flavor['deep'])
    st.markdown(css.replace("__SHELL__", shell).replace("__DEEP__", deep), unsafe_allow_html=True)
