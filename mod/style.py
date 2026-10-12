"""
Style

- Liquid glass shell over a blurred palette background
- Lilac WordArt title
- Handheld-console LCD screen in sage and slate
- Chunky glass press buttons
- Palette: sage #99B898, peach #FECEA8, salmon #FF847C, coral #E84A5F, slate #2A363B
- The shell tint changes with the selected color
"""
import streamlit as st


css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=VT323&display=swap');

:root {
  --shell-rgb: __SHELL__;
  --deep-rgb: __DEEP__;
  --on-shell: __TEXT__;
  --sage: #99B898;
  --peach: #FECEA8;
  --salmon: #FF847C;
  --coral: #E84A5F;
  --slate: #2A363B;
  --ink: #2A363B;
  --muted: #4E5D63;
  --lcd: #99B898;
  --lcd-ink: #2A363B;
  --display: 'Archivo Black', 'Arial Black', Impact, sans-serif;
  --mono: 'VT323', ui-monospace, monospace;
}

/* Page: blurred palette backdrop */
.stApp {
  background:
    radial-gradient(520px 340px at 12% 22%, rgba(254,206,168,.55) 0%, transparent 70%),
    radial-gradient(560px 380px at 88% 48%, rgba(232,74,95,.45) 0%, transparent 70%),
    radial-gradient(620px 420px at 30% 78%, rgba(255,132,124,.40) 0%, transparent 70%),
    linear-gradient(180deg, #99B898 0%, #B9C7A6 18%, #FECEA8 38%, #FF847C 58%, #E84A5F 72%, #2A363B 100%);
  background-attachment: fixed;
  color: var(--ink);
}
header[data-testid="stHeader"] { background: transparent; }

.stApp p, .stApp li, .stApp label, .stApp input, .stApp td, .stApp th {
  font-family: var(--mono);
}
.stApp p, .stApp li, .stApp label { font-size: 1.3rem; line-height: 1.25; color: var(--ink); }

/* Liquid glass shell */
[data-testid="stMainBlockContainer"] {
  max-width: 820px !important;
  margin: 2.5rem auto 3rem;
  padding: 1.75rem 2.25rem 2.25rem !important;
  border-radius: 56px 56px 150px 150px / 56px 56px 100px 100px;
  background:
    linear-gradient(155deg, rgba(255,255,255,.70) 0%, rgba(255,255,255,.18) 30%, rgba(255,255,255,0) 52%),
    radial-gradient(120% 60% at 50% 115%, rgba(var(--shell-rgb),.55) 0%, transparent 70%),
    linear-gradient(180deg, rgba(255,255,255,.40) 0%, rgba(var(--shell-rgb),.38) 100%);
  border: 1.5px solid rgba(255,255,255,.8);
  box-shadow:
    inset 0 2px 1px rgba(255,255,255,.95),
    inset 0 -2px 1px rgba(255,255,255,.35),
    inset 0 -40px 80px rgba(var(--deep-rgb),.22),
    0 50px 90px -36px rgba(42,54,59,.75);
  backdrop-filter: blur(24px) saturate(160%);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
}
/* Speaker grille at the bottom of the shell */
[data-testid="stMainBlockContainer"]::after {
  content: "";
  display: block;
  width: 44%;
  height: 34px;
  margin: 1.75rem auto 0;
  border-radius: 999px;
  background: radial-gradient(circle, rgba(42,54,59,.55) 1.6px, transparent 2.3px) 0 0 / 9px 9px;
  border: 1.5px solid rgba(255,255,255,.65);
  box-shadow: inset 0 2px 6px rgba(42,54,59,.25);
}

/* Glass bezel (header) */
.bezel {
  position: relative;
  text-align: center;
  background: linear-gradient(180deg, rgba(255,255,255,.78) 0%, rgba(255,255,255,.48) 100%);
  border: 1.5px solid rgba(255,255,255,.9);
  border-radius: 38px 38px 22px 22px;
  padding: 1.6rem 1.5rem 1.2rem;
  box-shadow: inset 0 2px 0 #FFFFFF, 0 14px 30px -18px rgba(42,54,59,.8);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  margin-bottom: 1.1rem;
}

/* WordArt title: lilac gradient fill, purple outline, stacked 3D shadow, slight warp */
.bezel-title {
  display: inline-block;
  font-family: var(--display);
  font-size: clamp(2rem, 6.6vw, 3.7rem);
  line-height: 1.05;
  letter-spacing: -.01em;
  margin: 0;
  padding: 0 .1em .08em;
  background: linear-gradient(180deg, #F3ECFF 0%, #C9B6F2 28%, #9B82DB 52%, #B7A2EC 70%, #E4D9FB 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-stroke: 1.5px #5E46A6;
  filter:
    drop-shadow(1px 1px 0 #7C66C2)
    drop-shadow(1px 1px 0 #6B55B2)
    drop-shadow(1px 1px 0 #5A44A0)
    drop-shadow(4px 5px 0 rgba(42,54,59,.28));
  transform: perspective(520px) rotateX(14deg) skewX(-7deg);
  transform-origin: 50% 100%;
}
.bezel-sub { font-family: var(--mono); font-size: 1.35rem; color: var(--muted); margin: .55rem 0 0; }
.bezel-led {
  position: absolute; top: 20px; right: 26px;
  width: 12px; height: 12px; border-radius: 50%;
  background: rgb(var(--shell-rgb));
  box-shadow: 0 0 10px rgba(var(--shell-rgb),.95), inset 0 1px 1px rgba(255,255,255,.8);
}

/* Small section names */
.part-name {
  font-family: var(--display);
  font-size: .9rem;
  color: var(--ink);
  margin: 1rem 0 .35rem;
}

/* LCD screen */
.lcd-frame {
  background: linear-gradient(180deg, #3B4A50 0%, #2A363B 100%);
  border-radius: 22px 22px 34px 22px;
  padding: 14px 14px 8px;
  box-shadow: inset 0 2px 0 rgba(255,255,255,.16), 0 6px 0 rgba(42,54,59,.25);
  margin: .25rem 0 .5rem;
}
.lcd {
  background-color: var(--lcd);
  background-image:
    linear-gradient(160deg, rgba(255,255,255,.22) 0%, rgba(255,255,255,0) 40%),
    repeating-linear-gradient(0deg, rgba(42,54,59,.08) 0 1px, transparent 1px 3px);
  border-radius: 10px;
  padding: .8rem 1.15rem 1rem;
  color: var(--lcd-ink);
  font-family: var(--mono);
  box-shadow: inset 0 3px 12px rgba(0,0,0,.28);
}
.lcd-row { display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; font-size: 1.25rem; }
.lcd-caption { font-size: 1.35rem; margin-top: .7rem; }
.lcd-big { font-size: clamp(3.2rem, 12vw, 5.6rem); line-height: .95; letter-spacing: .02em; }
.lcd-feedback { font-size: 1.5rem; min-height: 1.7rem; margin-top: .35rem; }
.lcd-feedback.warn::before { content: "! "; }
.lcd-brand {
  font-family: var(--display);
  font-size: .68rem; color: #8FA0A6; margin: 6px 4px 0;
  display: flex; justify-content: space-between;
}
.lcd-brand span:last-child { color: var(--salmon); }
.cells { display: flex; flex-wrap: wrap; gap: 3px; justify-content: flex-end; }
.cell { width: 10px; height: 14px; background: var(--lcd-ink); border-radius: 1px; }
.cell.used { background: rgba(42,54,59,.15); }
.lcd.win .lcd-big { animation: blink .45s steps(1) 6; }
@keyframes blink { 50% { opacity: 0; } }

/* Range scanner and heat meter */
.track {
  position: relative; height: 26px; border-radius: 999px; overflow: hidden;
  background: rgba(255,255,255,.45);
  border: 1.5px solid rgba(255,255,255,.9);
  box-shadow: inset 0 2px 6px rgba(42,54,59,.25);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
.window {
  position: absolute; top: 3px; bottom: 3px; border-radius: 999px; min-width: 6px;
  background: linear-gradient(180deg, rgba(255,255,255,.8) 0%, rgba(var(--shell-rgb),.95) 50%, rgb(var(--deep-rgb)) 100%);
  transition: left .45s ease, width .45s ease;
}
.tick { position: absolute; top: 0; bottom: 0; width: 2px; background: var(--slate); opacity: .55; }
.tick.secret { background: #FFFFFF; width: 4px; opacity: 1; box-shadow: 0 0 0 1.5px var(--slate); }
.track-scale { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 1.1rem; color: var(--ink); opacity: .8; }
.heat-fill {
  position: absolute; top: 3px; bottom: 3px; left: 3px; border-radius: 999px;
  background: linear-gradient(90deg, #99B898 0%, #FECEA8 40%, #FF847C 70%, #E84A5F 100%);
  background-size: 640px 100%;
  transition: width .45s ease;
}
.heat-row { display: flex; align-items: center; gap: .8rem; }
.heat-row .track { flex: 1; }
.heat-label { font-family: var(--display); font-size: .85rem; min-width: 6.5rem; text-align: right; color: var(--ink); }

/* Guess history chips */
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip {
  font-family: var(--mono); font-size: 1.3rem; padding: 1px 12px;
  border-radius: 999px; background: rgba(255,255,255,.6);
  border: 1.5px solid rgba(255,255,255,.95); color: var(--ink);
  box-shadow: 0 2px 6px -2px rgba(42,54,59,.35);
}
.chip.hit { background: var(--slate); color: #FFFFFF; border-color: var(--slate); }
.chip.hint { background: transparent; border-style: dashed; border-color: rgba(42,54,59,.45); }
.empty-note { font-family: var(--mono); font-size: 1.25rem; opacity: .75; }

/* Buttons: glass pills */
[data-testid^="stBaseButton-secondary"], [data-testid^="stBaseButton-primary"] {
  border-radius: 999px !important;
  min-height: 2.9rem;
  padding: .45rem 1.4rem !important;
  color: var(--ink) !important;
  background: linear-gradient(180deg, rgba(255,255,255,.92) 0%, rgba(255,255,255,.55) 100%) !important;
  border: 1.5px solid rgba(255,255,255,.95) !important;
  box-shadow: inset 0 1px 0 #FFFFFF, 0 4px 0 rgba(42,54,59,.22), 0 10px 18px -10px rgba(42,54,59,.6);
  backdrop-filter: blur(10px);
  transition: transform .06s ease, box-shadow .06s ease;
}
[data-testid^="stBaseButton-primary"] {
  color: var(--on-shell) !important;
  background: linear-gradient(180deg, rgba(255,255,255,.55) 0%, rgb(var(--shell-rgb)) 45%, rgb(var(--deep-rgb)) 130%) !important;
  border-color: rgba(255,255,255,.85) !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.8), 0 4px 0 rgb(var(--deep-rgb)), 0 12px 20px -10px rgba(var(--deep-rgb),.8);
}
[data-testid^="stBaseButton-primary"] p { color: var(--on-shell) !important; }
[data-testid^="stBaseButton-secondary"]:active, [data-testid^="stBaseButton-primary"]:active {
  transform: translateY(3px);
  box-shadow: inset 0 1px 0 #FFFFFF, 0 1px 0 rgba(42,54,59,.4);
}
[data-testid^="stBaseButton-secondary"]:disabled { opacity: .45; }
.stApp button p {
  font-family: var(--display) !important;
  font-size: .9rem !important;
  color: var(--ink);
}

/* Segmented controls (menus) */
[data-testid^="stBaseButton-segmented_control"] {
  background: rgba(255,255,255,.5) !important;
  border-color: rgba(255,255,255,.9) !important;
  color: var(--ink) !important;
  backdrop-filter: blur(10px);
}
[data-testid="stBaseButton-segmented_controlActive"] {
  background: linear-gradient(180deg, rgba(255,255,255,.5) 0%, rgb(var(--shell-rgb)) 50%, rgb(var(--deep-rgb)) 140%) !important;
}
[data-testid="stBaseButton-segmented_controlActive"] p { color: var(--on-shell) !important; }

/* Inputs */
.stApp [data-baseweb="input"], .stApp [data-baseweb="base-input"] {
  background: rgba(255,255,255,.7) !important;
  border-radius: 14px !important;
}
.stApp [data-baseweb="input"] { border: 1.5px solid rgba(255,255,255,.95) !important; }
.stNumberInput input { font-size: 2rem !important; text-align: center; color: var(--ink) !important; }
.stTextInput input { font-size: 1.5rem !important; color: var(--ink) !important; }
[data-testid="stForm"] { border: none; padding: 0; }

/* Focus */
.stApp button:focus-visible, .stApp input:focus-visible {
  outline: 3px solid var(--slate) !important;
  outline-offset: 2px;
}

/* Glass panels: stats, tables, rules */
.pearl {
  background: linear-gradient(180deg, rgba(255,255,255,.78) 0%, rgba(255,255,255,.55) 100%);
  border: 1.5px solid rgba(255,255,255,.9);
  border-radius: 22px;
  padding: 1rem 1.2rem;
  box-shadow: inset 0 1px 0 #FFFFFF, 0 10px 22px -14px rgba(42,54,59,.7);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  margin-bottom: .8rem;
}
.stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: .6rem; }
.stat { text-align: center; padding: .7rem .4rem; }
.stat-value { font-family: var(--display); font-size: 1.35rem; color: var(--ink); overflow-wrap: anywhere; }
.stat-name { font-family: var(--mono); font-size: 1.15rem; color: var(--muted); }
@media (max-width: 640px) {
  .stats { grid-template-columns: repeat(2, 1fr); }
  [data-testid="stMainBlockContainer"] { padding: 1.25rem 1rem 1.75rem !important; border-radius: 34px 34px 80px 80px; }
}

.table-wrap { overflow-x: auto; }
.retro-table { width: 100%; border-collapse: collapse; font-family: var(--mono); font-size: 1.2rem; color: var(--ink); }
.retro-table th {
  font-family: var(--display); font-size: .72rem; font-weight: 400;
  text-align: left; padding: .35rem .5rem; color: var(--muted);
  border-bottom: 2px solid rgba(42,54,59,.35);
}
.retro-table td { padding: .25rem .5rem; border-bottom: 1px dashed rgba(42,54,59,.18); white-space: nowrap; }
.retro-table td.num, .retro-table th.num { text-align: right; }
.badge { padding: 0 10px; border-radius: 999px; }
.badge.won { background: rgb(var(--shell-rgb)); color: var(--on-shell); }
.badge.lost { background: var(--slate); color: #FFFFFF; }

@media (prefers-reduced-motion: reduce) {
  .lcd.win .lcd-big { animation: none; }
  .window, .heat-fill { transition: none; }
}
</style>
"""


def inject_style(flavor):
    shell = ",".join(str(value) for value in flavor['rgb'])
    deep = ",".join(str(value) for value in flavor['deep'])
    st.markdown(css.replace("__SHELL__", shell).replace("__DEEP__", deep)
                .replace("__TEXT__", flavor['text']), unsafe_allow_html=True)
