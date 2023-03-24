import re

text = input(str(""))
result = re.sub(r'fuck|shit|ass|piss|anal|ballsack|bitch|erotic|slave|blowjob|boobs|tits|penis|dick|cock|pussy|vagina|bukake|butthole|anus|clit|chink|busty|cunt|cuck|cocksuck|coon|cum|sperm|cumming|cumshot|dickhead|dildo|doggystyle|doggiestyle|dumbass|dyke|dykes|dong|ejaculate|ejakulate|erect|erection|boner|fag|fagg|faggot|faggit|fagot|fatass|felch|femdom|fisting|footjob|foreskin|retard|fuk|futa|futanari|gangbang|sex|hardcoresex|hentai|heroin|weed|herpes|homoerotic|hooker|hookah|horny|horni|horniest|incest|inbred|incel|jackass|femcel|jackoff|jerkoff|jack off|jerk off|masturbate|jizz|masterbate|masterbait|masturbait|menstruate|mesntruation|milf|motherfuck|motherfucker|motherfucka|mothafucka|motherfuker|mothafuker|mothafuka|naked|nazi|nigg|nig|nipples|nipple|nude|nudes|naked|nutsack|orgasm|pedo|pedophile|pedophilia|phuck|phuk|porn|pornography|pron|prostitute|child porn|pubes|pubic|pussi|pussies|queef|rape|rapist|raping|reetard|tard|sexual|shag|sissy|slut|whore|smegma|strip club|stripper|tesicle|testical|teste|threesome|foursome|wank|tranny|lesbo|kike', "****", text)

length = len(result)

if length > 1000:
    print("Message is too long")
else: 
    print(result)

