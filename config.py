"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY ROMANIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "ROMANIAN"
HANDLE = "@velocityromanian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'ro',
 'name': 'Romanian',
 'native_name': 'Română',
 'history_key': 'romanian',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'ro-RO-EmilNeural',
 'native_fallback_voice': 'ro-RO-AlinaNeural',
 'native_engine': 'edge',
 'native_lang_code': 'ro',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'ROMÂNĂ',
 'translit_label': 'SAY IT LIKE',
 'flag': 'ro',
 'greeting': 'Bună!',
 'encouragement': 'Minunat!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZaăâbcdefghiîjklmnopqrsștțuvwxyz'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motivație',
 'Love': 'Dragoste',
 'Success': 'Succes',
 'Wisdom': 'Înțelepciune',
 'Happiness': 'Fericire',
 'Self Improvement': 'Auto-îmbunătățire',
 'Gratitude': 'Recunoștință',
 'Friendship': 'Prietenie',
 'Hope': 'Speranță',
 'Creativity': 'Creativitate',
 'Inner Peace': 'Pace Interioară',
 'Confidence': 'Încredere',
 'Perseverance': 'Perseverență',
 'Inspiration': 'Inspirație',
 'Positive Life': 'Viață Pozitivă',
 'Courage': 'Curaj',
 'Kindness': 'Bunătate',
 'Patience': 'Răbdare',
 'Forgiveness': 'Iertare',
 'Strength': 'Forță',
 'Joy': 'Bucurie',
 'Balance': 'Echilibru',
 'Growth': 'Creștere',
 'Purpose': 'Scop',
 'Mindfulness': 'Atenție Conștientă',
 'Travel & Airport': 'Călătorii și Aeroport',
 'Ordering Food & Dining': 'Comandarea Mâncării și Mese',
 'Shopping & Prices': 'Cumpărături și Prețuri',
 'Asking for Directions': 'Cererea de Indicații',
 'Hotel & Accommodation': 'Hotel și Cazare',
 'Daily Routine': 'Rutina Zilnică',
 'Meeting People & Greetings': 'Întâlnirea Oamenilor și Saluturi',
 'Emergency & Health': 'Urgențe și Sănătate',
 'Public Transportation': 'Transport Public',
 'Work & Office': 'Muncă și Birou',
 'Weather & Small Talk': 'Vreme și Conversații Generale',
 'Coffee Shop & Bakery': 'Cafenea și Brutărie',
 'Family & Home': 'Familie și Casă',
 'Hobbies & Free Time': 'Hobby-uri și Timp Liber',
 'Dating & Romance': 'Întâlniri și Romantism',
 'Phone Calls & Messages': 'Apeluri Telefonice și Mesaje',
 'Banking & Money': 'Bancă și Bani',
 'Doctor & Pharmacy': 'Doctor și Farmacie',
 'Sports & Fitness': 'Sport și Fitness',
 'Celebrations & Parties': 'Sărbători și Petreceri',
 'Feelings & Emotions': 'Sentimente și Emoții',
 'Agreeing & Disagreeing': 'A Acordă și A Dezacordă',
 'Making Plans': 'Planificarea',
 'Common Native Slang': 'Argo Comune',
 'Cultural Traditions': 'Tradiții Culturale'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnromanian',
 '#romanianlessons',
 '#romanianforbeginners',
 '#languagelearning',
 '#romanianvocabulary',
 '#velocityromanian',
 '#dailyromanian',
 '#romanian',
 '#learnlanguages',
 '#speakromanian']
# ==== HASHTAGS END ====
